from yahoo_finance import Share
from query_parser import *
import re
import pandas as pd

search_string = 'earnings poop share AAPL?'

#print(search_for_symbol(search_string))

def price_return(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_price()

def previous_closing_price(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_prev_close()

def historical_data(string):
    symbol = search_for_symbol(string)
    word_list = string.split()
    start_date = word_list[1]
    end_date = word_list[2]
    return Share(symbol).get_historical(start_date, end_date)

def market_cap(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_market_cap()

def dividend_yield(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_dividend_yield()

def dividend_share(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_dividend_share()

def earnings_share(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_earnings_share()

def what_info(string):
    results = []
    if re.search('(closing.* price)|(yesterday.*price)|(yesterday)', search_string.lower()):
        results.append('Yesterday\'s Closing Price: ' + previous_closing_price(string))

    if re.search('how.*much|price', search_string.lower()):
        results.append('Price: ' + price_return(string))

    if stripper(search_string).isupper():
        symbol = search_for_symbol(string)
        local_list = []
        local_list.append('Price: ' + Share(symbol).get_price())
        local_list.append('P/E Ratio: ' + Share(symbol).get_price_earnings_ratio())
        local_list.append('Change: ' + Share(symbol).get_change())
        local_list.append('Days High: ' + Share(symbol).get_days_high())
        local_list.append('Days Low: ' + Share(symbol).get_days_low())
        results.append(local_list)

    if re.search('market.*cap', search_string.lower()):
        results.append('Market Cap: ' + market_cap(string))

    if re.search('dividend', search_string.lower()):
        results.append('Dividend Yield: ' + dividend_yield(string))
        results.append('Dividend Share: ' + dividend_share(string))

    if re.search('earnings.*share', search_string.lower()):
        results.append('Earnings Share: ' + earnings_share(string))

    if string.split()[0] == 'history':
        return historical_data(string)
    return results



print(what_info(search_string))
