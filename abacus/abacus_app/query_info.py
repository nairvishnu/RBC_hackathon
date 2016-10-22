from yahoo_finance import Share
import re
import pandas as pd

src = "abacus_app/static/other_info.csv"
df = pd.read_csv(src)
exchanges = ['NYSE', 'NASDAQ', 'LSE', 'Japan SE', 'Shanghai SE', 'Hong Kong SE', 'Euronext', 'Shenzen SE', 'TMX Group', 'Deutsche Borse']

def stripper(string): #Function to strip punctuation from string
    return string.replace(',',''
                ).replace('.',''
                ).replace('?',''
                ).replace('!',''
                )

def splitter(string):
    string_list = string.split()
    return string_list

def search_for_symbol(string):
    stripped_string = stripper(string)
    split_string = splitter(stripped_string)
    stock_symbol = ''

    for word in split_string:
        if word.isupper():
            stock_symbol = word
            return stock_symbol

def price_return(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_price()

def volume_return(string):
    symbol = search_for_symbol(string)
    return Share(symbol).get_volume()

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

    if re.search('time.*NYSE.*MOC', string):
        x = df[df['Exchange'] == 'NYSE']['MOC'].as_matrix()[0]
        results.append('Stop Accepting MOC At: 16:00')

    elif re.search('(yesterday.*price)|(yesterday)', string.lower()):
        results.append('Yesterday\'s Closing Price: ' + previous_closing_price(string))

    elif re.search('how.*much.*sold|selling.*price|price|sold', string.lower()):
        results.append('Price: ' + price_return(string))

    elif re.search('how.*much.*traded.*in|volume', string.lower()):
        results.append('Volume: ' + volume_return(string))

    elif stripper(string).isupper():
        symbol = search_for_symbol(string)
        local_list = []
        local_list.append('Price: ' + Share(symbol).get_price())
        local_list.append('P/E Ratio: ' + Share(symbol).get_price_earnings_ratio())
        local_list.append('Change: ' + Share(symbol).get_change())
        local_list.append('Days High: ' + Share(symbol).get_days_high())
        local_list.append('Days Low: ' + Share(symbol).get_days_low())
        results.append(local_list)

    for exchange in exchanges:
        if re.search(exchange, string):
            if re.search('head-quarter.', string.lower()):
                x = df[df['Exchange'] == exchange]['Head-Quarters'].as_matrix()[0]
                results.append('Head-Quartered At: ' + str(x))
            if re.search('market.* cap', string.lower()):
                x = df[df['Exchange'] == exchange]['Market Cap'].as_matrix()[0]
                results.append('Market Cap: ' + str(x))
            if re.search('open.|opening', string.lower()):
                x = df[df['Exchange'] == exchange]['Open'].as_matrix()[0]
                results.append('Opens At: ' + str(x))
            if re.search('close|closing', string.lower()):
                x = df[df['Exchange'] == exchange]['Close'].as_matrix()[0]
                results.append('Closes At: ' + str(x))
            return results

    if re.search('market.*cap', string.lower()):
        results.append('Market Cap: ' + market_cap(string))

    elif re.search('tickers', string.lower()):
        results.append('Amount of Tickers: 2800')

    elif re.search('dividend', string.lower()):
        results.append('Dividend Yield: ' + dividend_yield(string))
        results.append('Dividend Share: ' + dividend_share(string))

    elif re.search('earnings.*share', string.lower()):
        results.append('Earnings Share: ' + earnings_share(string))



    elif string.split()[0] == 'history':
        return historical_data(string)

    return results
