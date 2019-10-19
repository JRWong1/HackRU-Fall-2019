from pymongo import MongoClient
import pprint


id = "10006546"

#print('hello world')

username = 'Sai'
password  = 'saisrinivas1'

client = MongoClient("mongodb://Sai:saisrinivas1@cluster0-shard-00-00-vaulk.mongodb.net:27017,cluster0-shard-00-01-vaulk.mongodb.net:27017,cluster0-shard-00-02-vaulk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")


airbnb = client.get_database("sample_airbnb")
airbnb_records = airbnb.listingsAndReviews

num_docs = airbnb_records.count_documents({})
print(num_docs)