from urllib.request import urlopen
import argparse
import json


base_url = 'https://api.genderize.io'


parser = argparse.ArgumentParser()
parser.add_argument('name')
args = parser.parse_args()

with urlopen(f"{base_url}/?name={args.name}") as response:
    data = json.loads(response.read().decode('utf-8'))

gender = data['gender']
probability = round(data['probability'] * 100)

print(f"{gender} ({probability}%)")
