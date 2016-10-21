from yahoo_finance import Share
from query_parser import *
import re

search_string = 'AAPL?'

#print(search_for_symbol(search_string))

def price_return(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_price()

def previous_closing_price(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_prev_close()

def stock_info(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_info()

def what_info(string):
    results = []
    if re.search('how.*much|price', search_string.lower()):
        results.append('Price: ' + price_return(string))
    if re.search('(closing.* price)|(yesterday.*price)|(yesterday)', search_string.lower()):
        results.append('Yesterday\'s Closing Price: ' + previous_closing_price(string))
    if stripper(search_string).isupper:
        symbol = search_for_symbol(string)
        local_list = []
        local_list.append('Price: ' + Share(symbol).get_price())
        local_list.append('P/E Ratio: ' + Share(symbol).get_price_earnings_ratio())
        local_list.append('Change: ' + Share(symbol).get_change())
        local_list.append('Days High: ' + Share(symbol).get_days_high())
        local_list.append('Days Low: ' + Share(symbol).get_days_low())
        results.append(local_list)
    return results


def key_words(string):
    word_list = splitter(stripper(string))
    return word_list

print(what_info(search_string))
