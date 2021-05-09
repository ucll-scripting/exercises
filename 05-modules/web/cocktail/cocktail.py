from urllib.request import urlopen
import argparse
import json


base_url = 'https://www.thecocktaildb.com/api/json/v1/1'

def download(url):
    with urlopen(url) as response:
        return response.read().decode('utf-8')


def find_by_name(name):
    name = name.replace(' ', '%20')
    url = f"{base_url}/search.php?s={name}"
    data = download(url)
    show(data)

def find_random():
    url = f"{base_url}/random.php"
    data = download(url)
    show(data)


def show(data):
    data = json.loads(data)
    for drink in data['drinks']:
        print(drink['strDrink'])
        for i in range(1, 16):
            ingredient = drink[f'strIngredient{i}']
            if ingredient is not None:
                measure = drink[f'strMeasure{i}']
                print(f"{ingredient}{f'({measure.strip()})' if measure else ''}")
        print()


parser = argparse.ArgumentParser()
parser.add_argument('name', nargs='?')
args = parser.parse_args()

if args.name:
    find_by_name(args.name)
else:
    find_random()
