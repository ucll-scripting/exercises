from urllib.request import urlopen
import json


def download(url):
    with urlopen(url) as response:
        return response.read().decode('utf-8')


data = download('https://www.boredapi.com/api/activity')
data = json.loads(data)

print(data['activity'])