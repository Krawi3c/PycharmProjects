import requests
from twilio.rest import Client

ALP_URL = "https://www.alphavantage.co/query?"
ALP_KEY = "WF335TEMQ3EMYU8H"

NEWS_API = "https://newsapi.org/v2/everything?"
NEWS_KEY = "75b7e97681e64070afff396992b4a411"

TWILIO_RECOVERY_CODE = "8G3JWEK9QVYKJWS6G3QG45ZV"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_difference():
    alp_params={
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "apikey": ALP_KEY,
    }
    response = requests.get(ALP_URL, params=alp_params)
    response.raise_for_status()
    data = response.json()

    day_before = data["Time Series (Daily)"]["2024-03-21"]["4. close"]
    yesterday = data["Time Series (Daily)"]["2024-03-22"]["4. close"]
    day_before = round(float(day_before), 2)
    yesterday = round(float(yesterday), 2)
    difference = int(yesterday/day_before)
    if difference < 0:
        difference *= -1
    return difference

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def news():
    news_params = {
        "qInTitle": "tesla",
        "apiKey": NEWS_KEY,
    }
    response = requests.get(NEWS_API, params=news_params)
    response.raise_for_status()
    data = response.json()
    news_list = [news for news in data["articles"]]
    news_messages = []
    for x in range(0, 3):
        message = "TESLA: 🔺2%\n"
        message += f"Headline: {news_list[x]['title']}\n"
        message += f"Brief: {news_list[x]['description']}"
        news_messages.append(message)
    print(news_messages)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
account_sid = "ACd81ca0f25bc13ee2f5150cdd7c1314fc"
auth_token = "ffaa1dd97920f5276b8f11ae423385ca"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+447700104998',
                     to='+447600104998'
                 )

print(message.sid)




news()




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

