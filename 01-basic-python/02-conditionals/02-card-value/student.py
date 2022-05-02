
def card_value(string):
    if string == 'Jack':
        return 11
    elif string == 'Queen':
        return 12
    elif string == 'Ace':
        return 1
    elif string == 'King':
        return 13
    else:
        return int(string)
