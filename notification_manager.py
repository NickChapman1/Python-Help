import contextlib
import smtplib
from typing import Iterable
from email.message import EmailMessage
# This class is responsible for sending notifications with the deal flight details.

# [ADDED]
import ssl
import socket
import time
import logging


class NotificationManager:

    def __init__(
        self,
        sender: str,
        app_password: str,
        host: str = "smtp.gmail.com",
        port: int = 465,
        use_ssl: bool = True,
        timeout: int = 10,
    ) -> None:  # [FIXED: unescaped '->']
        self.sender = sender
        self.app_password = app_password
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.timeout = timeout

    def _connect(self):
        if self.use_ssl:
            smtp = smtplib.SMTP_SSL(self.host, self.port, timeout=self.timeout)
        else:
            smtp = smtplib.SMTP(self.host, self.port, timeout=self.timeout)
            smtp.starttls()
        smtp.login(self.sender, self.app_password)
        return smtp

    # [ADDED] Explicit STARTTLS connection helper (587 recommended across networks)
    def _connect_starttls(self):
        """
        Prefer STARTTLS on 587 (often passes corporate/AV inspection better than implicit SSL on 465).
        """
        context = ssl.create_default_context()
        smtp = smtplib.SMTP(self.host, 587, timeout=self.timeout)
        try:
            smtp.ehlo()
            smtp.starttls(context=context)
            smtp.ehlo()
            smtp.login(self.sender, self.app_password)
            return smtp
        except Exception:
            # Ensure cleanup on failure
            with contextlib.suppress(Exception):
                smtp.quit()
            raise

    # [ADDED] Resilient wrapper: try your original config first, then fallback to STARTTLS if needed
    def _connect_resilient(self):
        """
        Try original _connect() first (respects self.use_ssl/self.port),
        then fallback to STARTTLS if the server/AV/VPN drops the SSL handshake (WinError 10054, etc.).
        """
        try:
            return self._connect()
        except (ConnectionResetError, smtplib.SMTPServerDisconnected, ssl.SSLError, socket.timeout) as e:
            logging.getLogger("travel").warning(
                "Primary SMTP connect failed (%s). Falling back to STARTTLS: host=%s port=%s use_ssl=%s",
                repr(e), self.host, self.port, self.use_ssl
            )
            return self._connect_starttls()

    # [ADDED] Optional retry/backoff
    def _with_retry(self, func, retries: int = 2, backoff: float = 0.5):
        for attempt in range(1, retries + 2):  # attempts = retries + 1
            try:
                return func()
            except (smtplib.SMTPException, ssl.SSLError, socket.timeout, ConnectionResetError) as e:
                if attempt > retries:
                    raise
                time.sleep(backoff * (2 ** (attempt - 1)))

    def send(
        self,
        subject: str,
        body_text: str | None,
        recipients: Iterable[str],
        *,
        body_html: str | None = None,
        cc: Iterable[str] | None = None,
        bcc: Iterable[str] | None = None,
        reply_to: str | None = None,
    ) -> None:  # [FIXED: unescaped '->']
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.sender

        to_list = list(recipients)
        cc_list = list(cc) if cc else []
        bcc_list = list(bcc) if bcc else []

        msg["To"] = ", ".join(to_list)
        if cc_list:
            msg["Cc"] = ", ".join(cc_list)
        if reply_to:
            msg["Reply-To"] = reply_to

        if body_html:
            # Multipart with plain fallback (generate plain if missing)
            msg.set_content(body_text or "This message contains HTML content.")
            msg.add_alternative(body_html, subtype="html")
        else:
            msg.set_content(body_text or "")

        all_recipients = to_list + cc_list + bcc_list

        # === Your original line kept exactly, but wrapped with fallback+retry ===
        def _send_once():
            try:
                with self._connect() as smtp:  # [KEPT]
                    smtp.send_message(msg, to_addrs=all_recipients)
            except (ConnectionResetError, smtplib.SMTPServerDisconnected, ssl.SSLError, socket.timeout):
                # Fallback path: STARTTLS(587)
                with self._connect_starttls() as smtp:  # [ADDED]
                    smtp.send_message(msg, to_addrs=all_recipients)

        # Optionally add retry for transient hiccups
        self._with_retry(_send_once, retries=1, backoff=0.6)

    # Option A: instance method using instance state (simple)
    def send_email_text2(
        self,
        subject: str,
        body: str,
        recipients: list[str],
    ) -> None:  # [FIXED: unescaped '->']
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = ", ".join(recipients)
        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=self.timeout) as smtp:
            smtp.starttls()
            smtp.login(self.sender, self.app_password)
            smtp.send_message(msg)

    # Option B: uncomment this version instead if you want it as a static “no self” demo
    # @staticmethod
    # def send_email_text2(
    #     subject: str,
    #     body: str,
    #     sender: str,
    #     recipients: list[str],
    #     app_password: str,
    #     *,
    #     smtp_host: str = "smtp.gmail.com",
    #     smtp_port: int = 587,
    #     timeout: int = 10,
    # ) -> None:
    #     msg = EmailMessage()
    #     msg["Subject"] = subject
    #     msg["From"] = sender
    #     msg["To"] = ", ".join(recipients)
    #     msg.set_content(body)
    #
    #     with smtplib.SMTP(smtp_host, smtp_port, timeout=timeout) as smtp:
    #         smtp.starttls()
    #         smtp.login(sender, app_password)
    #         smtp.send_message(msg)