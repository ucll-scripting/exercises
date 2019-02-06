def format_time(h, m, s):
    h, m, s = (str(x).rjust(2, '0') for x in (h, m, s))
    return f"{h}:{m}:{s}"
