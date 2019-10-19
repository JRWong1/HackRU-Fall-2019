from pymongo import MongoClient
import pprint
import csv

ingredients_list = []

with open('hack_ru.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ingredients = row['ingredients']
        for each in ingredients.split(", "):
            ingredients_list.append(each)
        
        
unique_ingredients = set(ingredients_list)

print(unique_ingredients)
print(len(unique_ingredients))