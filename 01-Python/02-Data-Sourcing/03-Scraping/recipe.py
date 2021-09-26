# pylint: disable=missing-docstring,line-too-long
from os import path
import sys
import csv
import requests
from bs4 import BeautifulSoup

def parse(html):
    """ Function that returns a list of dict {name, difficulty, prep_time}"""
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    recipe_list = []
    counter = 0
    for recipe in soup.find_all('p'):
        recipe_dict = {'name' : recipe.text}
        recipe_list.append(recipe_dict)
    for difficulty in soup.find_all('span', class_="recipe-difficulty" ):
        recipe_list[counter]['difficulty'] = difficulty.text
        counter += 1
    counter = 0
    for prep_time in soup.find_all('span', class_="recipe-cooktime" ):
        recipe_list[counter]['prep_time'] = prep_time.text
        counter += 1
    return recipe_list

def write_csv(ingredient, recipes):
    """Function that dumps recipes to a CSV file `recipes/INGREDIENT.csv`"""
    with open(f"recipes/{ingredient.upper()}.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=recipes[0].keys())
        writer.writeheader()
        for recipe in recipes:
            writer.writerow(recipe)
    return True

def scrape_from_internet(ingredient, start=1):
    """ Foction uses `requests` to get the HTML page of search results for given ingredients."""
    url = f"https://recipes.lewagon.com/?search[query]={ingredient}&page={start}"
    response = requests.get(url)
    html = response.content
    #check for a bug from LeWagon recipe website
    soup = BeautifulSoup(html, "html.parser")
    check_url = soup.find('meta', property="og:url")
    returned_url = check_url["content"]
    if returned_url == 'https://recipes.lewagon.com/?page=1':
        return False
    return html


def scrape_from_file(ingredient):
    file = f"pages/{ingredient}.html"
    if path.exists(file):
        return open(file)
    print("Please, run the following command first:")
    print(f'  curl "https://recipes.lewagon.com/?search[query]={ingredient}" > pages/{ingredient}.html')
    sys.exit(1)

def main():
    if len(sys.argv) > 1:
        ingredient = sys.argv[1]
        recipes = parse(scrape_from_internet(ingredient))
        start = 1
        while len(recipes) < 30:
            # print(len(recipes))
            start += 1
            more_recipes = parse(scrape_from_internet(ingredient, start = start))
            if more_recipes == []:
                # print('the end')
                break
            for recipe in more_recipes:
                if len(recipes) < 30:
                    recipes.append(recipe)
        # print(len(recipes))
        write_csv(ingredient, recipes)
    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)

if __name__ == '__main__':
    main()
