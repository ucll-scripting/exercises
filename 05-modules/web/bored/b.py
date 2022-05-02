import urllib.request
import sys
import json

with urllib.request.urlopen("http://www.boredapi.com/api/activity/") as input:
    contents = input.read()
    dict = json.loads(contents)
    print(dict["activity"])
