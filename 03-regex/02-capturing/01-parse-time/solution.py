import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)
    #match = re.fullmatch(r'([01][0-9]|[2][0-3])\:([0-5][0-9])\:([0-5][0-9])(?:\.([0-9]{3}))?', string)

    if match:
        return tuple( [ int(x) for x in match.groups('000') ] )
    else:
        return None
