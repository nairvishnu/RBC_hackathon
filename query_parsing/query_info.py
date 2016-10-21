from yahoo_finance import Share
from query_parser import *

search_string = 'How much was traded in AAPL?'

#print(search_for_symbol(search_string))

def price_return(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_price()


def what_info(string):
    if 'how much' in search_string.lower():
        return price_return(string)


def key_words(string):
    word_list = splitter(stripper(string))
    return word_list

print (what_info(search_string))
