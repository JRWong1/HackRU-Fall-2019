from pymongo import MongoClient
import pprint
import csv
import re

ingredients_list = []

with open('hack_ru3.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ingredients = row['ingredients']
        ingredients = re.sub(r'\([^)]*\)',"", ingredients)
        ingredients = ingredients.strip()
        for each in ingredients.split(", "):
            ingredients_list.append(each)
        
        
unique_ingredients = set(ingredients_list)
unique_ingredients.remove("")
print(list(unique_ingredients)[0])

#Number of unique ingredients is 9688
fields = ['', 'country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars']
for ingredient in unique_ingredients:
    if(ingredient == ''):
        continue
    fields.append(ingredient)
print(len(fields))

"""
with open('hack_ru2.csv','w', newline='') as newfile:
    with open('hack_ru3.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(newfile)
        dict_writer = csv.DictWriter(newfile, fieldnames=fields)
        counter = 0
        for row in reader:
            counter+=1
            if counter == 1:
                dict_writer.writeheader()
            a = [row[''], row['country'], row['company'], row['total_pack_size_ml_g'], row['unit_pack_size_ml_g'], row['price_per_100g_ml_dollars']]
            current_ingredients = row['ingredients']
            result = []
            for each in unique_ingredients:
                if each in row['ingredients']:
                    result.append(1)
                else:
                    result.append(0)
            for each in result:
                a.append(each)
            writer.writerow(a)
            if counter == 32:
                break
"""

fields1 = ['', 'country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars','ingredients']
"""
with open('hack_ru.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ingredients = row['ingredients']
        ingredients = re.sub(r'\([^()]+\)', lambda x: x.group().replace(',', ''), ingredients)
        """

with open('hack_ru3.csv','w', newline='') as newfile:
    with open('hack_ru.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(newfile)
        dict_writer = csv.DictWriter(newfile, fieldnames=fields1)
        counter = 0
        for row in reader:
            counter+=1
            if counter == 1:
                dict_writer.writeheader()
            a = [row[''], row['country'], row['company'], row['total_pack_size_ml_g'], row['unit_pack_size_ml_g'], row['price_per_100g_ml_dollars']]
            current_ingredients = row['ingredients']
            current_ingredients = re.sub(r'\([^)]*\)',"", current_ingredients)
            current_ingredients = current_ingredients.strip()
            #result = []
                
            a.append(current_ingredients)
                
            writer.writerow(a)

with open('hack_ru2.csv','w', newline='') as newfile:
    with open('hack_ru3.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(newfile)
        dict_writer = csv.DictWriter(newfile, fieldnames=fields)
        counter = 0
        for row in reader:
            counter+=1
            if counter == 1:
                dict_writer.writeheader()
            a = [row[''], row['country'], row['company'], row['total_pack_size_ml_g'], row['unit_pack_size_ml_g'], row['price_per_100g_ml_dollars']]
            current_ingredients = row['ingredients']
            result = []
            for each in unique_ingredients:
                if each in row['ingredients']:
                    result.append(1)
                else:
                    result.append(0)
            for each in result:
                a.append(each)
            writer.writerow(a)
'''
with open('hack_ru2.csv', newline='') as readable:
    with open('hack_ru2.csv','w', newline='') as writable:
        reader = csv.DictReader(readable)
        writer = csv.writer(writable)
        first = True
        for row in reader:
            #rewrite the first row
            first_row = set(['', 'country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars'])
            first_row.add(unique_ingredients)
            print(first_row)
            writer.writerow(list(first_row))
            if not first:
                writer.writerow( (row[''], row['country'], row['company'], row['total_pack_size_ml_g'], row['unit_pack_size_ml_g'], row['price_per_100g_ml_dollars']) )
            first = False
'''