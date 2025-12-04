import requests
import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.header import Header


# Load environment variables from .env file
load_dotenv()
alpha_api_key = os.getenv("ALPHA_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
MyEmailSend = os.getenv("SEND_EMAIL")
app_password = os.getenv("APP_PW_GMAIL")
api_key = os.getenv("OWM_API_KEY")
MyEmailRecieve = os.environ.get("RECIEVE_EMAIL")
Alpha_Endpoint = "https://www.alphavantage.co/query"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#Potential functions to use

def get_top_articles(NewsData, count=3):
    articles = NewsData.get("articles", [])[:count]
    result = []
    for article in articles:
        result.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "url": article.get("url")
        })
    return result

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Make the GET request
stock_params = {
    "function": 'TIME_SERIES_DAILY',
    "symbol":STOCK,
    #"interval": '5min',
    "apikey": alpha_api_key,

}
response = requests.get(Alpha_Endpoint,params=stock_params)
#below will raise an expection if it doesn't get the 200 code
response.raise_for_status()
NewsData = response.json()#convert response to python dict
# Parse daily time series
daily_data = NewsData.get("Time Series (Daily)")
#Catch for if it can't find it
if not daily_data:
    print("Error: No daily data found.")
    exit()

#Sorts the data which is returned from newest to oldest, starting with yesterdays data.
dates = sorted(daily_data.keys(), reverse=True)
yesterday = dates[0]
day_before = dates[1]
#close is the key pulling in the value from the end of day, casting as a float
yesterday_close = float(daily_data[yesterday]["4. close"])
day_before_close = float(daily_data[day_before]["4. close"])
#Difference of the two over the prior start times 100
percent_change = ((yesterday_close - day_before_close) / day_before_close) * 100
direction = "🔺" if percent_change > 0 else "🔻"
#.2f is the amount of decimals to print out
print(f"{STOCK}: {direction}{abs(percent_change):.2f}%")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# Format GET https://newsapi.org/v2/everything?q=Apple&from=2025-12-01&sortBy=popularity&apiKey=API_KEY
# Make the GET request
NewsEndpoint = "https://newsapi.org/v2/everything"
NewsParams = {
    "q": "Tesla",
    "from": "2025-12-01",
    "sortBy":"popularity",
    "apiKey": news_api_key
}
response = requests.get(NewsEndpoint, params=NewsParams, verify=False)
#Use these lines for testing when building out to see what is getting passed
# print(response.status_code) # print(response.url) # print(response.text)
NewsData = response.json()
# Usage of function, could've done see below ex1:
top_three = get_top_articles(NewsData)
#Email Body Build
email_message= f"{STOCK}: {direction}{abs(percent_change):.2f}%\n\n"
for a in top_three:
    email_message+= f"Headline: {a['title']}\n ({a['source']})\n{a['url']}\n\n"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Send email with UTF-8 encoding
msg = MIMEText(email_message, "plain", "utf-8")
msg["Subject"] = Header("Tesla Stock Update", "utf-8")
msg["From"] = MyEmailSend
msg["To"] = MyEmailRecieve

with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as g_connection:
    g_connection.starttls()
    g_connection.login(user=MyEmailSend, password=app_password)
    g_connection.sendmail(
        from_addr=MyEmailSend,
        to_addrs=MyEmailRecieve,
        msg=msg.as_string()
    )
    g_connection.close()

#Examples and other ways to write

#1. Instead of doing a function could've done
# articles = data.get("articles", [])[:3]  # Slice the first 3 safely
#
# for i, article in enumerate(articles, start=1):
#     print(f"Article {i}:")
#     print(f"Title: {article.get('title')}")
#     print(f"Source: {article.get('source', {}).get('name')}")
#     print(f"URL: {article.get('url')}")
#     print()