def card_value(string):
    if string == 'J':
        return 11
    elif string == 'Q':
        return 12
    elif string == 'K':
        return 13
    elif string == 'A':
        return 1
    else:
        return int(string)