import smtplib
import ssl
from email.message import EmailMessage

class NotificationManager:

    def __init__(self, sender, app_password, host="smtp.gmail.com", timeout=10):
        self.sender = sender
        self.app_password = app_password
        self.host = host
        self.timeout = timeout

    def send_email_simple(self, subject: str, body_text: str, recipients: list[str]) -> None:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = ", ".join(recipients)
        msg.set_content(body_text)

        # CONNECT FIRST, then send (choose one path)
        with smtplib.SMTP(self.host, 587, timeout=self.timeout) as smtp:
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(self.sender, self.app_password)
            smtp.send_message(msg)
