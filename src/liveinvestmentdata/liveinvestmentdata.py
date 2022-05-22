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


from threading import Thread
import requests
from bs4 import BeautifulSoup as bs
import time


def download_url(url: str) -> object:
    '''
    Downloads the page source of the provided URL

    :function:: download_url(url: str) -> object

    Args:
        url (str):
            The url of the page you want downloaded

    Returns:
        object: A class object containing the page source code, with methods for filtering the data
    '''
    page = requests.get(url)

    return bs(page.content, 'html.parser')


####################### Price  ################################

def crypto_price(name: str) -> float:
    '''
    Pulls the price of the provided crypto name from coinmarketcap.com,
    the cryptocurrencies full name must be provided in most cases.

    :function:: crypto_price(name: str) -> float

    Args:
        name (str):
            The full name of the cryptocurrency your searching for

    Returns:
        float: The floating-point integer of the price, as provided by coinmarketcap.com

    '''
    page = download_url(f"https://coinmarketcap.com/currencies/{name}")

    #Scrapes the page source for the price
    s = page.find('div', class_='priceValue')
    try:
        price = s.find_all('span')[0].text
    except AttributeError:
        raise AttributeError('Crypto name must be spelled correctly')

    #Removes uncessary characters from the price
    for character in price:
        try:
            int(character)
        except ValueError:
            if character != '.':
                price = price.replace(character, '')
    stripped_price = float(price)

    #Either returns the price directly, or through a shared dictionary for multi-threaded use
    try:
        shared_crypto_price_dict[name] = stripped_price
    except NameError:
        return stripped_price


def multi_crypto_price(name_list: list) -> dict:
    '''
    Aquires multiple crypto prices from the 'crypto_price' function, utlizing threads
    for optimal speed and efficiency

    :function:: multi_crypto_price(symbol_list: list) -> dict

    Args:
        name_list (list):
            A list in which each item is a crypto you want the price of

    Returns:
        dict: A dicitonary in which the key is the cryptocurrency name,
        and the value is the price

    '''
    #Utilizing a global variable for shared memory amongst threads
    global shared_crypto_price_dict

    shared_crypto_price_dict = {}
    still_alive = []
    
    #Starts a new thread for each item in the list
    for name in name_list:
        t = Thread(target=crypto_price, args=(name,))
        t.start()
        still_alive.append(t)

    #Waits for all of the threads to finish before returning
    while still_alive:
        removal = [item for item in still_alive if not item.is_alive()]
        [still_alive.remove(item) for item in removal]
        time.sleep(.01)

    return shared_crypto_price_dict



def stock_price(ticker: str) -> float:
    '''
    Pulls the price of the provided stock ticker from marketwatch.com
    
    :function:: stock_price(ticker: str) -> float

    Args:
        ticker (str):
            The stock ticker you want the price

    Returns:
        float: The floating-point integer of the price, provided by marketwatch.com

    '''
    page = download_url(f"https://www.marketwatch.com/investing/stock/{ticker}")

    #Scrapes the page source for the price, and removes unecessary characters
    s = page.find('div', class_='intraday__data')
    price = s.find_all('h2')[0].text.strip()
    for character in price:
        try:
            int(character)
        except ValueError:
            if character != '.':
                price = price.replace(character, '')
    
    price = float(price)

    try:
        shared_stock_dict[ticker] = price
    except NameError:
        return price


def multi_stock_price(ticker_list: list):
    '''
    Aquires multiple stock prices from the 'stock_price' function, utlizing threads                                                                   
    for optimal speed and efficiency                                                                                             

    :function:: multi_crypto_price(symbol_list: list) -> dict                                                                                           

    Args:
        name_list (list):
            A list in which each item is a crypto you want the price of                                                                                 

    Returns:
        dict: A dicitonary in which the key is the cryptocurrency name,                                                                                 
        and the value is the price    
    '''
    #Utilizing a global variable for shared memory amongst threads
    global shared_stock_dict

    shared_stock_dict = {}
    still_alive = []
    
    #Starts a new thread for each item in the list
    for ticker in ticker_list:
        t = Thread(target=stock_price, args=(ticker,))
        t.start()
        still_alive.append(t)

    #Waits for all of the threads to finish before returning
    while still_alive:
        removal = [item for item in still_alive if not item.is_alive()]
        [still_alive.remove(item) for item in removal]
        time.sleep(.01)

    return shared_stock_dict


#############################################################





######################### News #############################



def coinmarketcap_news(name: str) -> dict:
    '''
    Pulls news from coinmarketcap.com for the provided cryptocurrency name
    
    :function:: coinmarketcap_news(name: str) -> dict

    Args:
        name (str):
            The name of the cryptocurrency you want news for

    Returns:
        dict: The key is the news headline and the value is the link

    '''
    crypto_news = {}

    page = download_url(f"https://coinmarketcap.com/currencies/{name}")

    #Scrapes the page source for all new articles relating the said cryptp
    s = page.find('div', class_='sc-101ku0o-2 exKUGw')
    loaded_news = s.find_all('a')
    for news in loaded_news:
        crypto_news[news.text.strip()] = news.get('href')

    return crypto_news


def marketwatch_news(ticker: str) -> dict:
    '''
    Pulls news from marketwatch.com for the provided stock ticker

    :function:: marketwatch_news(ticker: str) -> dict

    Args:
        ticker (str):
            The ticker of the stock you want news for

    Returns:
        dict: The key is the news headline and the value is the link

    '''
    stock_news = {}

    page = download_url(f"https://www.marketwatch.com/investing/stock/{ticker}")

    s = page.find('div', class_='collection__elements')
    loaded_news = s.find_all('h3')

    for news in loaded_news:
        try:
            text = news.find('a').text.strip().lower()
            stock_news[text] = news.find('a').get('href')
        except AttributeError:
            pass

    return stock_news



def stock_news(ticker: str) -> dict:
    '''
    Pulls news for a stock from multiple sources, and filters out repeats
    
    :function:: stock_news(ticker: str) -> dict

    Args:
        ticker (str):
            The ticker of the stock you want news for

    Returns:
        dict: The key is the news headline and the value is the link

    '''
    stock_news_dict = {}

    stock_news_dict['marketwatch'] = marketwatch_news(ticker)


    return stock_news_dict

##############################################################





####################### Financials ##########################


def marketwatch_income_statement(ticker: str, key_data_only=False, time_period='quarter') -> dict:
    '''
    Pulls the income statement table from marketwatch.com for a stock

    :function:: marketwatch_income_statement(ticker: str, key_data_only=False, time_period='quarter') -> dict

    Args:
        ticker (str):
            The ticker of the stock you want financial data for

        key_data_only (bool, *optional):
            Only pulls key data from the income statement, which marketwatch highlights

        time_period (str, *optional):
            Can either pull the data from the 'quarter' or 'annual' table, default is set to 'quarter'             

    Returns:
        dict: 
            The key is the financial metric title, and the value is a list of financial
            data

    '''
    if time_period == 'annual':
        page = download_url(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/income')
    if time_period == 'quarter':
        page = download_url(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/income/quarter')
    
    vals = []

    s = page.find_all('div', class_='element__body')
    for x in s:
        if key_data_only:
            row = x.find_all('tr', class_="is-highlighted")
        else:
            row = x.find_all('tr', class_="table__row")
        for x in row:
            y = x.text.split('\n\n')
            for i in y:
                a = i.split('\n')
                if '' in a:
                    a.remove('')
                if ' ' in a:
                    a.remove(' ')
                if a:
                    vals.append(a)

    data = {}

    for x in range(len(vals)):
        if x % 2 == 0:
            data[vals[x][0]] = vals[x+1]

    #Checks whether to pass new to thread operation, or just to return the value
    try:
        financial_data['Income Statement'] = data
    except:
        return data



def marketwatch_balance_sheet(ticker: str, key_data_only=False, time_period='quarter') -> dict:
    '''
    Pulls the balance sheet table from marketwatch.com for a stock

    :function:: marketwatch_balance_sheet(ticker: str, key_data_only=False, time_period='quarter') -> dict

    Args:
        ticker (str):
            The ticker of the stock you want financial data for
                
        key_data_only (bool, *optional):
            Only pulls key data from the balance sheet, which marketwatch highlights

        time_period (str, *optional):
            Can either pull the data from the 'quarter' or 'annual' table, default is set to 'quarter'

    Returns:
        dict: 
            The key is the financial metric title, and the value is a list of financial
            data

    '''
    if time_period == 'annual':
        page = download_url(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/balance-sheet')
    if time_period == 'quarter':
        page = download_url(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/balance-sheet/quarter')


    vals = []

    s = page.find_all('div', class_='element__body')
    for x in s:
        if key_data_only:
            row = x.find_all('tr', class_="is-highlighted")
        else:
            row = x.find_all('tr', class_="table__row")
        for x in row:
            y = x.text.split('\n\n')
            for i in y:
                a = i.split('\n')
                if '' in a:
                    a.remove('')
                if ' ' in a:
                    a.remove(' ')
                if a:
                    vals.append(a)

    data = {}

    for x in range(len(vals)):
        if x % 2 == 0:
            data[vals[x][0]] = vals[x+1]

    #Checks whether to pass new to thread operation, or just to return the value
    try:
        financial_data['Balance Sheet'] = data
    except:
        return data


def marketwatch_cash_flow(ticker: str, key_data_only=False, time_period='quarter') -> dict:
    '''
    Pulls the cash flow table from marketwatch.com for a stock

    :function:: marketwatch_cash_flow(ticker: str, key_data_only=False, time_period='quarter') -> dict

    Args:
        ticker (str):
            The ticker of the stock you want financial data for

        key_data_only (bool, *optional):
            Only pulls key data from the cash flow, which marketwatch highlights

        time_period (str, *optional):
            Can either pull the data from the 'quarter' or 'annual' table, default is set to 'quarter'

    Returns:
        dict: 
            The key is the financial metric title, and the value is a list of financial
            data

    '''
    if time_period == 'annual':
        page = download_url(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/cash-flow')
    if time_period == 'quarter':
        page = download_url(f'https://www.marketwatch.com/investing/stock/{ticker}/financials/cash-flow/quarter')


    vals = []

    s = page.find_all('div', class_='element__body')
    for x in s:
        if key_data_only:
            row = x.find_all('tr', class_="is-highlighted")
        else:
            row = x.find_all('tr', class_="table__row")
        for x in row:
            y = x.text.split('\n\n')
            for i in y:
                a = i.split('\n')
                if '' in a:
                    a.remove('')
                if ' ' in a:
                    a.remove(' ')
                if a:
                    vals.append(a)

    data = {}

    for x in range(len(vals)):
        if x % 2 == 0:
            data[vals[x][0]] = vals[x+1]

    #Checks whether to pass new to thread operation, or just to return the value
    try:
        financial_data['Cash Flow'] = data
    except:
        return data


def stock_financial_data(ticker: str, key_data_only=False, time_period='quarter') -> dict:
    '''
    Pulls the Income Statement, Balance Sheet, and Cash Flow tables from marketwatch.com for a stock

    :function:: stock_financial_data(ticker: str, key_data_only=False, time_period='quarter') -> dict

    Args:
        ticker (str):
            The ticker of the stock you want financial data for

        key_data_only (bool, *optional):
            Only pulls key data from financial tables, which marketwatch highlights

        time_period (str, *optional):
            Can either pull the data from the 'quarter' or 'annual' table, default is set to 'quarter'

    Returns:
        dict: 
            The key is the table type, and the value is dictionaries of the return value from the function above

    '''
    global financial_data

    documents = [marketwatch_income_statement, marketwatch_balance_sheet, marketwatch_cash_flow]

    financial_data = {'Income Statement':None,
                      'Balance Sheet':None,
                      'Cash Flow':None,
                     }

    still_alive = []

    for document in documents:
        t = Thread(target=document, args=(ticker, key_data_only, time_period))
        t.start()
        still_alive.append(t)

    while still_alive:
        removal = [item for item in still_alive if not item.is_alive()]
        [still_alive.remove(item) for item in removal]
        time.sleep(.01)


    return financial_data
