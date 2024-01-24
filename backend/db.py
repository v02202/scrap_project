import os
from pymongo import MongoClient


db_client = MongoClient(
    'db', 27017, 
    username=os.environ.get("MONGO_INITDB_ROOT_USERNAME"), 
    password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
)
scrapy_db = db_client['scrapy']