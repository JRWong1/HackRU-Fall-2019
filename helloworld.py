from pymongo import MongoClient


#print('hello world')

username = 'sai'
password  = 'saisrinivas1'

client = MongoClient("mongodb://sai:saisrinivas1@cluster0-shard-00-00-vaulk.mongodb.net:27017,cluster0-shard-00-01-vaulk.mongodb.net:27017,cluster0-shard-00-02-vaulk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

database_name = client.db_name



print(database_name)
#testgit