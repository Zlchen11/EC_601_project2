# EC_601_project2

The user story is at git Wiki.

Acknowledgement :
Codes in get_recent_tweet.py and sentiment.py are referenced from Twitter API sample code and Google NLP sentiment analysis.

get_recent_tweet.py : First enter your own token, then you can enter the name on twitter you want. After executed, it would generate a list that contains last 100 tweets of the account you entered. 

sentiment.py : First enter your own token, and decide how you want to sort the data. In this file, I joined ten tweets into one element and used sentiment analysis to generate score & magnitude. Besides, this file would also generate 'data.txt', which you can check what you actually got from get_recent_tweet.py. 


figure.py : In this file, use yfinance library to crawl the stock data you want to observe. It will generate a figure to compare the trend. Because twitter API can only catch last 100 tweets, it may not be enough data to evaluate the relationship with stock price. In the future, maybe add more parameters into consideration to compare the trend.
