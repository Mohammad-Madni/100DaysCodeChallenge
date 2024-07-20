import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = ""
API_KEY = ""


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
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)


dif_percent = (difference / float(yesterday_closing_price)) * 100
print(dif_percent)


if dif_percent > 1:
    news_params = {
        "apikey" : NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articals = news_response.json()["articles"]
    three_articals = articals[:3]
    print(three_articals)


    formatted_articales = [f"Headline: {artical['title']}. \nBrief: {artical['description']}" for artical in three_articals]



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.


#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

