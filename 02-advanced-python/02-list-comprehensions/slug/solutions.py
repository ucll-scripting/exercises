def slug(name):
    parts = name.split(' ')
    fname = parts[0]
    lname = parts[1:]

    return '-'.join(s.lower() for s in lname + [fname])