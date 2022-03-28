import requests
import json
from twilio.rest import Client
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

list_of_days = ["01", "02", "03", "04", "05", "06", "07"]

def get_news():
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # news_api
    date = "2022-03-28"
    sort_by = "popularity"
    NEWS_API_KEY = "22cb6a3ff24547f28438b3747a828462"
    NEWS_URL = "https://newsapi.org/v2/everything"
    parametre_news = {
        "q": COMPANY_NAME,
        "from": date,
        "sortBy": sort_by,
        "apiKey": NEWS_API_KEY
    }
    response_news = requests.get(url=NEWS_URL, params=parametre_news)
    response_news.raise_for_status()
    data_news = response_news.json()
    data = data_news["articles"]
    data = data[:3]
    articles = []
    for i in range(len(data)):
        articles_tupple = (data[i]["title"], data[i]["description"])
        articles.append(articles_tupple)
    return articles




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# alpha_api
TIME_SERIES_DAILY = "TIME_SERIES_DAILY"
ALPHAVANTAGE_API_KEY = "WWTXC29I7TMXOVUH"
ALPHA_URL = "https://www.alphavantage.co/query"
parametre_alpha = {
    "function": TIME_SERIES_DAILY,
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}
response_alpha = requests.get(url=ALPHA_URL, params=parametre_alpha)
response_alpha.raise_for_status()
data_alpha = response_alpha.json()
data_alpha["Time Series (Daily)"]
list_data = [value for (key, value) in data_alpha["Time Series (Daily)"].items()]
yesterday_data = list_data[0]["4. close"]
day_before_yesterday_data = list_data[1]["4. close"]
diff = float(yesterday_data) - float(day_before_yesterday_data)
direction = ""
diff_percent = (diff/float(yesterday_data)) * 100
notify = False
if diff > 0 and diff_percent > 5:
    notify = True
    direction = "🔺"
    article = get_news()

    print(article)
elif diff < 0 and abs(diff_percent) > 5:
    notify = True
    direction = "🔻"
    article = get_news()


if notify:
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    # latter to stop annoyint message
    account_sid = "AC3d5697b0c7e520f48d66fd1492755370"
    auth_token = "bd6d31d367ce85ed828d7c3252721ef2"
    number = "+19048778332"
    for i in range(len(article)):
        message_text = f"{STOCK}: {direction}{diff_percent}% \n Headline: {article[i][0]} \n Brief: {article[i][0]}"
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=message_text,
            from_=number,
            to='+61460707773'
        )

        print(message.sid)






#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

