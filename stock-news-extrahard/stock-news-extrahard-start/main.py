import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = 'AC3d1bf4faa7a08e15c8bae6afa06f2fc5'
auth_token = '495ac29417777e6b837ebbf795ab941a'
percentage_change = 0

ALPHAVANTAGE_PARAMETERS = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": STOCK,
    # "interval": "60min",
    "apikey": "LH6YX6P03MPRMJXO"
}

NEWSAPI_PARAMETERS = {
    "q": COMPANY_NAME,
    "apiKey": "75b7e97681e64070afff396992b4a411"
}


def send_sms(news):
    global percentage_change
    client = Client(account_sid, auth_token)
    emoji = ""
    if percentage_change > 0:
        emoji = "🔺"
    else:
        percentage_change*=-1
        emoji = "🔻"
    for news in news:
        message = client.messages.create(
            body=f"{STOCK}: {emoji}{percentage_change}"
                 f"Headline: {news[0]}"
                 f"Brief: {news[1]}",
            from_="+12707137151",
            to="+48730342138"
        )

def get_news():

    response_news = requests.get("https://newsapi.org/v2/everything", params=NEWSAPI_PARAMETERS)
    response_news.raise_for_status()
    data_news = response_news.json()["articles"][:3]
    news = []
    for row in data_news:
        title = row["title"]
        description = row["description"]
        news.append([title, description])
    return news

def get_stock_change():
    global percentage_change
    response_alpha = requests.get("https://www.alphavantage.co/query", params=ALPHAVANTAGE_PARAMETERS)
    response_alpha.raise_for_status()
    data_alpha = response_alpha.json()["Weekly Time Series"]
    yesterday = list(data_alpha.keys())[0]
    day_before_yesterday = list(data_alpha.keys())[1]
    yesterday_price = float(data_alpha[yesterday]["4. close"])
    day_before_yesterday_price = float(data_alpha[day_before_yesterday]["4. close"])
    increase = day_before_yesterday_price * 1.05
    decrease = day_before_yesterday_price * 0.95
    if yesterday_price >= increase or yesterday_price<=decrease:
        percentage_change = round((1-(day_before_yesterday_price/yesterday_price))*100)
        return True

if get_stock_change():
    get_news()
    send_sms(get_news())

