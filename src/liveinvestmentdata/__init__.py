'''

Simple to use stock, commodity, forex, and cryptocurrency market webscraper, utilizing the beautiful soup and requests libraries.
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

from liveinvestmentdata.liveinvestmentdata import *
