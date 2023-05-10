import requests
import os
from datetime import timedelta, date
from telegram.ext import Updater

yesterday = date.today() - timedelta(days=1)
two_days_ago=date.today()-timedelta(days=4)

BOT_API_KEY="5845234870:AAHwhDYa-7FPojKy3JsmlGRei2h0aR14iLU"
updater = Updater(BOT_API_KEY)
print(updater.bot)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = "b01bf72a7be44a201c1d3cae31a043be"
NEWS_API="e5ba3e83d5754a389ce591654dc2aade"



stock_params = {
    'access_key':STOCK_API,
    'symbols': STOCK_NAME,
    'date_from': two_days_ago,
    'date_to': yesterday
}

STOCK_ENDPOINT = 'http://api.marketstack.com/v1/eod'
NEWS_ENDPOINT="https://newsapi.org/v2/everything"


stock_url = 'https://www.alphavantage.co/query'
r = requests.get(url=STOCK_ENDPOINT,params=stock_params)

data = r.json()["data"]
yesterday_data=data[0]
someday_data=data[1]
yesterday_closing_price=yesterday_data["close"]
some_day_closing_price=someday_data["close"]
print(data)
difference=float(some_day_closing_price)-float(yesterday_closing_price)
upEmote=None
if difference>0:
    up_down="STOCKS UP!!"
else:
    up_down="STOCKS DOWN!!"
print(difference)
perc_diff=(difference/float(yesterday_closing_price))*100
print(perc_diff)
# data_list={}
# data_list={key:value for (key,value) in data[0].items()}
# new_data=[value for (key,value) in data_list.items()]
# new_data=data["data"]
# print(new_data)
# stock_data=[value for (key,value) in new_data[0].items()]
# print(stock_data)
if abs(perc_diff)>0:
    print("Get News")
    news_params={
        "apiKey":NEWS_API,
        "q":COMPANY_NAME,
    }

    news_response=requests.get(url=NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()['articles']
    print(articles)
    article_list=[item for item in articles[:3]]
    print(article_list)
    # article_lines=[f"{COMPANY_NAME} {up_down} {round(perc_diff)}%  Headlines:{article['title']}  Description:{article['description']}" for article in article_list]
    # print(article_lines)
    for article in article_list:
        updater.bot.sendMessage(chat_id="@TopStockNews",
                                text=f"{COMPANY_NAME} {up_down} {round(perc_diff)}%  Headlines:{article['title']}  Description:{article['description']}")


