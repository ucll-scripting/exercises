import sys
from urllib.request import urlopen
import json

name = sys.argv[1]

url = f"https://api.genderize.io/?name={name}"

def download(url):
    with urlopen(url) as f:
        return f.read().decode('utf-8')
    
data = download(url)
data = json.loads(data)

#gender probability

print(f"{data['gender']} ({int(data['probability']*100)}%) (count: {data['count']})")


