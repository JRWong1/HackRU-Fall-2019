from pymongo import MongoClient
import pprint
import csv
import re

fields = ['', 'country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars', 'ingredients']
calculated = ['predicted_price_per_100g_ml_dollars', 'difference_from_expected','predicted_total_price']


coefficients = {}
with open('TheOneThatTookLikeAnHour.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        key = row[""]
        coeff = row["Estimate"]
        key = key.replace(".", " ")
        key = key.replace("country", "")
        key = key.replace("company", "")
        coefficients[key] = coeff

prices = {}


counter = 0
count_errors = 0
row_num = 0
with open('hack_ru2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sum = 2.48879979399772
        for thing in row.keys():
            key = thing.strip()
            if key == "":
                continue
            try:
                
                if key == "" or key == "price_per_100g_ml_dollars":
                    continue
                else:
                    value = 0
                    weight = 0
                    if key == "total_pack_size_ml_g" or key == "unit_pack_size_ml_g" or key not in fields:
                        weight = float(coefficients[key])
                        try:
                            value = float(weight * float(row[key]))
                        except ValueError:
                            value = 0
                    else:
                        weight = float(coefficients[row[key]])
                        value = weight
                    
                    sum+=value
            
            except KeyError:
                pass

        row_num+=1

        difference = abs(sum - float(row['price_per_100g_ml_dollars']))
        try:
            prices[str(counter)] = {'predicted_price_per_100g_ml_dollars': sum, 'difference_from_expected': difference, 'predicted_total_price': sum*float(row['total_pack_size_ml_g'])/100}
        #Total pack size is NAN
        except ValueError:
            prices[str(counter)] = {'predicted_price_per_100g_ml_dollars': sum, 'difference_from_expected': difference, 'predicted_total_price': "NaN"}
        counter+=1
        

all_fields = fields + calculated
'''
for key, value in prices.items():
    print(key)
    print(value)
'''


with open('hack_ru.csv', newline='') as csvfile:
    with open('hack_ru copy.csv','w', newline='') as newfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(newfile)
        dict_writer = csv.DictWriter(newfile, fieldnames=all_fields)
        counter = 0
        for row in reader:
            counter+=1
            if counter == 1:
                dict_writer.writeheader()
            a = []
            for key in row.keys():
                a.append(row[key])
            new_column = prices[str(counter - 1)]
            for key in calculated:
                a.append(new_column[key])

            writer.writerow(a)
            

print('finished')
                
'''
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
'''
'''
