from pymongo import MongoClient
import pprint
import csv
import re

ingredients_list = []

with open('hack_ru.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ingredients = row['ingredients']
        ingredients = re.sub(r'\([^()]+\)', lambda x: x.group().replace(',', ''), ingredients)
        for each in ingredients.split(", "):
            ingredients_list.append(each)
        
        
unique_ingredients = set(ingredients_list)

#Number of unique ingredients is 9688
fields = ['', 'country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars']
for ingredient in unique_ingredients:
    if(ingredient == ''):
        continue
    fields.append(ingredient)
print(len(fields))


with open('hack_ru2.csv','w', newline='') as newfile:
    with open('hack_ru.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(newfile)
        dict_writer = csv.DictWriter(newfile, fieldnames=fields)
        counter = 0
        for row in reader:
            counter+=1
            if counter == 1:
                dict_writer.writeheader()
                continue
            a = [row[''], row['country'], row['company'], row['total_pack_size_ml_g'], row['unit_pack_size_ml_g'], row['price_per_100g_ml_dollars']]
            current_ingredients = row['ingredients']
            result = []
            for each in unique_ingredients:
                if each in row['ingredients']:
                    result.append(1)
                else:
                    result.append(0)
            a = a.
            writer.writerow( (row[''], row['country'], row['company'], row['total_pack_size_ml_g'], row['unit_pack_size_ml_g'], row['price_per_100g_ml_dollars']) )

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