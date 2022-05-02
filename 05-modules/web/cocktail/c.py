
from urllib.request import urlopen
import sys
import json
import argparse
import re

def to_url(string):
    '''
    URLs cannot contain spaces. Replaces each space by %20.
    '''
    return re.sub(' ', '%20', string)
    
    
def createparser():
    parser = argparse.ArgumentParser(prog="cocktail")
    parser.add_argument('name',nargs='?')
    return parser

def main():
    args = createparser().parse_args()
    name = args.name
    
    if name:
        url = to_url(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}")
        printcocktailinfo(url)
            
    else:
        url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
        printcocktailinfo(url)
         
def printcocktailinfo(url):
    drinks = cocktaildict(url)["drinks"]
    for drink in drinks:
        name,ingredients, measurements = look_name_ingredients_measurements(drink)
        print(name)
        
        ingredients_measurements = zip(ingredients, measurements)
        for ingredient,measurement in ingredients_measurements:
            print(f"{ingredient} ({measurement})".rjust(50))
                
                           
def cocktaildict(url):
    with urlopen(url) as f:
        return json.loads(f.read().decode("utf-8"))
        
       
# drink is dict
def look_name_ingredients_measurements(drink):
    name = drink["strDrink"]
    ingredients = [drink[f"strIngredient{i}"] for i in range(1,16) if drink[f"strIngredient{i}"] != None ]
    measurements = [drink[f"strMeasure{i}"] for i in range(1,16) if drink[f"strMeasure{i}"] != None if drink[f"strMeasure{i}"] != ""]
    return (name,ingredients,measurements)


main()