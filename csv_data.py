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

#Number of unique ingredients is 9688

with open('hack_ru2.csv','w', newline='') as newfile:
    with open('hack_ru.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(newfile)
        counter = 0
        for row in reader:
            counter+=1
            if counter == 1:
                writer.writerow(row)
                continue
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