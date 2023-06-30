import requests
from twilio.rest import Client
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now().date()

# Calculate the previous day's date
previous_day = current_date - timedelta(days=1)


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_VAN_API =  'MG60OY4OJMXUNNTS'
ALPHA_VAN_PARA = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK_NAME,
    "apikey":ALPHA_VAN_API
}

NEWS_API = 'ba766d7d2ab347ceba48cabaaedcfeea'
NEWS_API_PARA = {
    "q":STOCK_NAME,
    "apikey":NEWS_API
}

api= "3f501dc7e591dec3fa31916aa2df4a66"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
price_data = requests.get(STOCK_ENDPOINT,params=ALPHA_VAN_PARA)
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]


#TODO 2. - Get the day before yesterday's closing stock price

stock_prices = {
    "day-1":
        {
            "open":list(price_data.json()["Time Series (Daily)"].values())[0]['1. open'],
            "close":list(price_data.json()["Time Series (Daily)"].values())[0]['4. close']
        },
    "day-2":
        {
            "open":list(price_data.json()["Time Series (Daily)"].values())[1]['1. open'],
            "close":list(price_data.json()["Time Series (Daily)"].values())[1]['4. close']
        }
}


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
day_1_clp = float(stock_prices["day-1"]["close"])
day_2_clp = float(stock_prices["day-2"]["close"])

price_differ = abs(day_1_clp-day_2_clp)


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
differ_percent = 6;
print(differ_percent)


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if differ_percent>5:
    print("Get News\n YOU HAVE SUCESSFULLT COMPLETED THE FIRST PART OF THE PROJECT")
   
   
   
   
   
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    new_data = requests.get(NEWS_ENDPOINT,params=NEWS_API_PARA)


    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_data = new_data.json()["articles"][0:3]


        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    headline_msg = {}
    d=1
    for data in news_data:
        
        headline_msg[f"msg_{d}"]={
            "title":data["title"],
            "description":data["description"]
        }
        d+=1
        
        

    t_1=headline_msg["msg_1"]["title"]
    t_2=headline_msg["msg_3"]["title"]
    t_3=headline_msg["msg_2"]["title"]
    d_1=headline_msg["msg_1"]["description"]
    d_2=headline_msg["msg_2"]["description"]
    d_3=headline_msg["msg_3"]["description"]

    msg = f"⚠️STOCK ALERT⚠️::TSLA\n\nHeadline::{t_1}\nBrief::{d_1}\n\nHeadline::{t_2}\nBrief::{d_2}\n\nHeadline::{t_3}\nBrief::{d_3}\n\n❤️Thanking You for making this project❤️"
    #TODO 9. - Send each article as a separate message via Twilio. 

    account_sid = 'ACccebce4624138adbb55598b6a44902e1'
    auth_token = '26209503132199ea67f5181852dc5bd0'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='+19784875876',
      body=msg,
      to='+918056528918'
    )

    # print(message.sid)
    print("message sent to your mobile")
    # # #Optional TODO: Format the message like this: 
    # """
    # TSLA: 🔺2%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    # or
    # "TSLA: 🔻5%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    # """

