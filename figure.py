Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import yfinance as yf                       
... import matplotlib.pyplot as plt             
... import sentiment as sent
... df = yf.Ticker("GOOG").history(period="7d") 
...                                                               
... price = []                                  
... for i in range(len(df)) :                   
...     print(df.Close[i])                      
...     price.append(df.Close[i])               
...                                             
... plt.figure(figsize=(8, 8))                  
... plt.subplot(211)                            
... plt.plot(price)                             
... plt.title('last 7 days price')              
...                                             
...                                             
... plt.subplot(212)                            
... plt.plot(senti)                             
... plt.title('last 7 days sentiment')          
