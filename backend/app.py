from flask import Flask, render_template
import requests, os
from werkzeug.middleware.proxy_fix import ProxyFix
# from snstwitter import twitter
import auth


app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


# blueprint register
app.register_blueprint(auth.bp)
# app.register_blueprint(twitter)
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