# import re
import requests

# 'F'
# 'Ford Motor Company'

STOCK_NAME = input("Enter stock symbol : ")
COMPANY_NAME = input("Enter Company Name : ")
STOCK_API_KEY = "3CRNLV9FHABRWRO1"
NEWS_API_KEY = "51868907a4004a31a039053fee94a833"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params = {
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]

# print(data_list[0])


yesterdays_closing_price = data_list[1]['4. close']
day_before_yesterday_closing_price = data_list[2]['4. close']
difference = float(yesterdays_closing_price) - \
             float(day_before_yesterday_closing_price)
diff_percentage = (abs(difference)/float(yesterdays_closing_price))*100
# print(diff_percentage)


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


if diff_percentage >= 1:

    sign = '🔺' if difference > 0 else '🔻'

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

    print(f"{COMPANY_NAME} : {sign}{round(diff_percentage,2)}%")
    for i in range(3):
        print("\n\nHeadline : \n" + remove_html_tags(articles[i]['title']))
        print("article : \n" + remove_html_tags(articles[i]['description']))

else:
    print("Not much difference. ")
