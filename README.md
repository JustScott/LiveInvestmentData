# <p align='center'>LiveInvestmentData</p>
<h3 align='center'> Simple to use stock, commodity, forex, and cryptocurrency market webscraper, utilizing the beautiful soup and requests libraries. Easily pull live market prices, news, financial information, and more with simple to use functions. </h3>

<br>
<h4>*Disclaimer*</h4
<h5>- Some of the aforementioned features above have yet to be implemented.<h5>
<br>

# Example Use

<h4>Prices</h4>

```python

>>> from liveinvestmentdata import stock_price, multi_stock_price, crypto_price, multi_crypto_price
>>> 
>>> stock_price('aapl')
137.6
>>> multi_stock_price(['aapl','tsla','amzn'])
{'tsla': 665.4, 'aapl': 137.6, 'amzn': 2159.37}
>>> 
>>> crypto_price('ethereum')
2035.99
>>> multi_crypto_price(['ethereum','bitcoin','dogecoin'])
{'dogecoin': 0.08623, 'bitcoin': 30355.87, 'ethereum': 2038.41}
>>>
```
<h4>News</h4>

```python
>>> from liveinvestment data import marketwatch_news, stock_news, coinmarketcap_news
>>>
>>> marketwatch_news('aapl')
{'apple looks closer at india and vietnam to boost production: report': 'https://www.marketwatch.com/articles/apple-china-production-iphone-india-vietnam-51653152645?mod=mw_quote_news', 'apple tells suppliers it wants more production in india and southeast asia, outside of china': 'https://www.marketwatch.com/story/apple-tells-suppliers-it-wants-more-production-in-india-and-southeast-asia-outside-of-china-11653148553?mod=mw_quote_news',..}
>>>
>>> stock_news('aapl') #Will provide more news sources than 'marketwatch' in the future
{'marketwatch': {'apple looks closer at india and vietnam to boost production: report': 'https://www.marketwatch.com/articles/apple-china-production-iphone-india-vietnam-51653152645?mod=mw_quote_news', 'apple tells suppliers it wants more production in india and southeast asia, outside of china': 'https://www.marketwatch.com/story/apple-tells-suppliers-it-wants-more-production-in-india-and-southeast-asia-outside-of-china-11653148553?mod=mw_quote_news',...}
>>>
>>> coinmarketcap_news('ethereum')
{'Ethereum Ropsten Testnet to Merge in June': 'https://coinmarketcap.com/alexandria/article/ethereum-ropsten-testnet-to-merge-in-june', 'Cloudflare to Support Ethereum by Launching Validator Nodes': 'https://coinmarketcap.com/alexandria/article/cloudflare-to-support-ethereum-by-launching-validator-nodes',...}
>>>
```

<h4>Financials</h4>

```python

>>> from liveinvestmentdata import marketwatch_income_statement, marketwatch_balance_sheet, marketwatch_cash_flow
>>>
>>> marketwatch_income_statement('aapl', key_data_only=True, time_period='annual')
{'Sales/Revenue': ['228.57B', '265.81B', '259.97B', '274.15B', '365.82B'], 'Net Income': ['48.35B', '59.53B', '55.26B', '57.41B', '94.68B']}
>>>
>>> marketwatch_balance_sheet('aapl', key_data_only=True, time_period='annual')
{'Total Current Assets': ['128.65B', '131.34B', '162.82B', '143.71B', '134.84B'], 'Total Assets': ['375.32B', '365.73B', '338.52B', '323.89B', '351B'], 'Total Current Liabilities': ['100.81B', '116.87B', '105.72B', '105.39B', '125.48B'], 'Total Liabilities': ['241.27B', '258.58B', '248.03B', '258.55B', '287.91B'], "Liabilities & Shareholders' Equity": ['375.32B', '365.73B', '338.52B', '323.89B', '351B']}
>>>
>>> marketwatch_cash_flow('aapl', key_data_only=True, time_period='annual')
{'Net Operating Cash Flow': ['63.6B', '77.43B', '69.39B', '80.67B', '104.04B'], 'Net Investing Cash Flow': ['(46.45B)', '16.07B', '45.9B', '(4.29B)', '(14.55B)'], 'Net Financing Cash Flow': ['(17.35B)', '(87.88B)', '(90.98B)', '(86.82B)', '(93.35B)']}
>>>
```

<br>

<h2>Required Dependences From PyPi</h2>

<h4>beautifulsoup4==4.11.1</h4>

- <a href="https://github.com/il-vladislav/BeautifulSoup4">beautifulsoup4 on GitHub</a>

- <a href="https://pypi.org/project/beautifulsoup4/">beautifulsoup4 on PyPi</a>

<h4>requests==2.27.1</h4>

- <a href="https://github.com/psf/requests">requests on GitHub</a>

- <a href="https://pypi.org/project/requests/">requests on PyPi</a>


# Documentation
```python
'''

Simple to use stock market and crypto webscraper, utilizing the beautiful soup and requests libraries.
Easily pull live market prices, news, financial information, and more with simple to use functions.

Functions:
    download_url(url: str) -> object
        Downloads the page source of the provided URL
    

    #### Prices ####

    crypto_price(name: str) -> float
        Pulls the price of the provided crypto name from coinmarketcap.com,
        the cryptocurrencies full name must be provided in most cases.
    multi_crypto_price(symbol_list: list) -> dict
        Aquires multiple crypto prices from the 'crypto_price' function, utlizing threads
        for optimal speed and efficiency
    stock_price(ticker: str) -> float
        Pulls the price of the provided stock ticker from marketwatch.com
    multi_crypto_price(symbol_list: list) -> dict
        Aquires multiple stock prices from the 'stock_price' function, utlizing threads                                                                         for optimal speed and efficiency

    ##############

    #### News ####

    coinmarketcap_news(name: str) -> dict
        Pulls news from coinmarketcap.com for the provided cryptocurrency name
    marketwatch_news(ticker: str) -> dict
        Pulls news from marketwatch.com for the provided stock ticker
    stock_news(ticker: str) -> dict
        Pulls news for a stock from multiple sources, and filters out repeats

    ####################

    #### Financials ####
    
    marketwatch_income_statement(ticker: str, key_data_only=False, time_period='quarter') -> dict
        Pulls the income statement table from marketwatch.com for a stock
    marketwatch_balance_sheet(ticker: str, key_data_only=False, time_period='quarter') -> dict
        Pulls the balance sheet table from marketwatch.com for a stock
    marketwatch_cash_flow(ticker: str, key_data_only=False, time_period='quarter') -> dict
        Pulls the cash flow table from marketwatch.com for a stock
    stock_financial_data(ticker: str, key_data_only=False, time_period='quarter') -> dict
        Pulls the Income Statement, Balance Sheet, and Cash Flow tables from marketwatch.com for a stock
    
    ####################

'''
```
