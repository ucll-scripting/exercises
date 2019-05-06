from urllib.request import urlopen
import re


def download(url):
    with urlopen(url) as response:
        return response.read().decode('utf-8')


def build_url(page):
    return f"http://127.0.0.1:5000/{page}"


def fetch(page):
    return download(build_url(page))


def find_hrefs(html):
    return re.findall(r'href="([^"]+)"', html)


visited = set()
queue = [ 'index.html' ]

while queue:
    next = queue.pop()

    if next not in visited:
        visited.add(next)
        html = fetch(next)
        queue += find_hrefs(html)

print("\n".join(sorted(list(visited))))
