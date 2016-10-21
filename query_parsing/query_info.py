from yahoo_finance import Share
from query_parser import *
import re

search_string = 'GPRO?'

#print(search_for_symbol(search_string))

def price_return(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_price()

def previous_closing_price(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_prev_close()

def what_info(string):
    results = []
    if re.search('how.*much|price', search_string.lower()):
        results.append('Price: ' + price_return(string))
    if re.search('(closing.* price)|(yesterday.*price)|(yesterday)', search_string.lower()):
        results.append('Yesterday\'s Closing Price: ' + previous_closing_price(string))
    return results


def key_words(string):
    word_list = splitter(stripper(string))
    return word_list

print(what_info(search_string))
