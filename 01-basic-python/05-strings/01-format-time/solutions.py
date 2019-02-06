def format_time(h, m, s):
    def format(x):
        return str(x).rjust(2, '0')

    h = format(h)
    m = format(m)
    s = format(s)

    return f"{h}:{m}:{s}"
