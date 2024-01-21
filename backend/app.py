from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def index():
    return 'App Works!'

@app.route("/home")
def home():
   return render_template("home.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)