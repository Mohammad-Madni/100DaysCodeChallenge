import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = ""

API_KEY = ""

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY

}

response = requests.get(STOCK_ENDPOINT,params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]

yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


dif_percent = round((difference / float(yesterday_closing_price)) * 100)


if abs(dif_percent) > 1:
    news_params = {
        "apikey" : NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articals = news_response.json()["articles"]
    three_articals = articals[:3]


    formatted_articales = [f"{STOCK_NAME}: {up_down}{dif_percent}%\nHeadline: {artical['title']}. \nBrief: {artical['description']}" for artical in three_articals]

    for articale in formatted_articales:
        message = client.messages.create(
            body= articale,
            from_='your twilio number',
            to='your number'
        )
