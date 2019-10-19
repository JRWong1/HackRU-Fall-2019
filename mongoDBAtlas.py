from pymongo import MongoClient
import pprint
import csv

'''
id = "10006546"

#print('hello world')

username = 'Sai'
password  = 'saisrinivas1'

client = MongoClient("mongodb://Sai:saisrinivas1@cluster0-shard-00-00-vaulk.mongodb.net:27017,cluster0-shard-00-01-vaulk.mongodb.net:27017,cluster0-shard-00-02-vaulk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")


airbnb = client.get_database("sample_airbnb")
airbnb_records = airbnb.listingsAndReviews

num_docs = airbnb_records.count_documents({})
pprint.pprint(airbnb_records.find_one({"_id": id}))
'''

client = MongoClient("mongodb://Sai:saisrinivas1@cluster0-shard-00-00-vaulk.mongodb.net:27017,cluster0-shard-00-01-vaulk.mongodb.net:27017,cluster0-shard-00-02-vaulk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
colgate_db = client.get_database("colgate_database")
pricing = colgate_db.pricing

with open('hack_ru.csv', newline='') as csvfile:
    spam_reader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    reader = csv.DictReader(csvfile)
    counter = 0
    for row in reader:
        #ignore first row with the titles
        dict = row
        pricing.insert_one(dict).inserted_id
        break

print("finished")