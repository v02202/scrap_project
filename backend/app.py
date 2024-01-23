from flask import Flask, render_template
import requests, os
from werkzeug.middleware.proxy_fix import ProxyFix
from pymongo import MongoClient


app = Flask(__name__, instance_relative_config=True)
db_client = MongoClient(
    'db', 27017, 
    username=os.environ.get("MONGO_INITDB_ROOT_USERNAME"), 
    password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
)
scrapy_db = db_client['scrapy']
twitter_tb = scrapy_db['twitter_tb']
twitter_tb.insert_one({'title': 'Morning Notes', 'description': 'Wake up early and do excercise', 'status': 'doing'})

app.wsgi_app = ProxyFix(app.wsgi_app)
@app.route('/')
def index():
    return 'App Works!'

@app.route("/home")
def home():
   return render_template("home.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)