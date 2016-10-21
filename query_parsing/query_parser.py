from yahoo_finance import Share


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
