import urllib.request
import json
import sys
import re


def to_url(string):
    '''
    URLs cannot contain spaces. Replaces each space by %20.
    '''
    return re.sub(' ', '%20', string)


artist, title = sys.argv[1:]
title = to_url(title)
artist = to_url(artist)

url = f"https://api.lyrics.ovh/v1/{artist}/{title}"

with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])