import os
from pymongo import MongoClient


db_client = MongoClient(
    "mongodb://db:27017",
    username=os.environ.get("MONGO_INITDB_ROOT_USERNAME"), 
    password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
)
try:
    db_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

scrapy_db = db_client['scrapy']