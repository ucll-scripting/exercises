import urllib.request
import json
import sys
from PIL import Image


number = sys.argv[1] 

url = f"https://xkcd.com/{number}/info.0.json"


with urllib.request.urlopen(url) as input:
    data = json.loads(input.read().decode('utf-8'))
    print(data.items())
    for key, value in data.items():
        print(f'{key}: {value}')
        

    

with urllib.request.urlopen(data['img']) as image:
    img = Image.open(image)
    img.show()
 