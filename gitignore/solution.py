import requests
import sys


ids = ",".join(sys.argv[1:])

response = requests.get(f'https://www.gitignore.io/api/{ids}').text

with open('.gitignore', 'w') as out:
    out.write(response)
