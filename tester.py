from pymongo import MongoClient
import pprint
import csv
import re

fields = ['', 'country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars', 'ingredients']
calculated = ['predicted_price_per_100g_ml_dollars', 'difference_from_expected','predicted_total_price']
fields2 = ['country', 'company', 'total_pack_size_ml_g', 'unit_pack_size_ml_g', 'price_per_100g_ml_dollars', 'ingredients']

#Key of the ingredient and value of Ing(x)
match_ingredients = {}
with open('hack_ruLegend.csv', newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        match_ingredients = dict(row)

coefficients = {}
with open('TheOneThatTookLikeAnHour.csv', newline='') as csvfile2:
    reader = csv.DictReader(csvfile2)
    for row in reader:
        key = row[""]
        coeff = row["Estimate"]
        key = key.replace(".", " ")
        key = key.replace("country", "")
        key = key.replace("company", "")
        coefficients[key] = coeff

prices = {}

ingredient_sum=0
counter = 0       
with open('inputdata.csv', newline='') as csvfile3:
    reader = csv.DictReader(csvfile3)
    for row in reader:

        sum = 2.48879979399772
        #print(dict(row))
        ingredients = row['ingredients']
        ingredients = re.sub(r'\([^)]*\)',"", ingredients)
        ingredients = ingredients.strip()
        #print(coefficients[match_ingredients['Sorbitol']])
        keys = fields2 + ingredients.split(", ")
        for key in keys:
            key = key.strip()
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
                    elif key== "country" or key == "company":
                        weight = float(coefficients[row[key]])
                        #print(row[key])
                        value = weight
                    else:
                        weight = float(coefficients[match_ingredients[row[key]]])
                        value = weight
                    
                    sum+=value
            
            except KeyError:
                pass

        """for ingredient in ingredients.split(", "):
            
            try:
                sum += float(coefficients[match_ingredients[ingredient]])
            except KeyError:
                #print(row)
                print("IngKeyError")
                pass
        try:
            sum += float(coefficients[row['company']])
            sum += float(coefficients[row['country']])
        
            sum += float(float(coefficients['total_pack_size_ml_g']) * float(row['total_pack_size_ml_g']))
            sum += float(float(coefficients['unit_pack_size_ml_g']) * float(row['unit_pack_size_ml_g']))
        except KeyError:
            print("KeyError")
            pass"""

        
        prices[str(counter)] = {'predicted_price_per_100g_ml_dollars': sum, 'difference_from_expected': "NaN", 'predicted_total_price': sum*float(row['total_pack_size_ml_g'])/100}

        counter+=1
print(prices)

"""counter = 0
count_errors = 0
row_num = 0
with open('inputdata.csv', newline='') as csvfile4:
    reader = csv.DictReader(csvfile4)
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


print(prices)"""