from urllib.request import urlopen
import re




def url(suffix):
    base_url = "http://127.0.0.1:5000/"
    return base_url + suffix

def data(url):
    with urlopen(url) as f:
        return f.read().decode("utf-8")

def findurls(string):
    return re.findall(r'href="(.*?)"', string)


queue = ['index.html']
s = set()

while queue:
    next = queue.pop()
    if next not in s:
        s.add(next)
        link = url(next)
        stream = data(link)
        for i in findurls(stream):
            queue.append(i)

l = list(s)
l = sorted(l)
for i in l:
    print(i)
        
        

 
