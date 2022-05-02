# Write your code here
from slugify import slugify

def slug(name):
    r = slugify(name)
    list = r.split('-')
    if len(list)==1:
        return r
    else:
            firstE = list[0]
            listE = list[1:]
            listE.append(firstE)
            return "-".join(listE)