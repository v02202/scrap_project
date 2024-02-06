from flask import Flask, render_template, request, session, g
import requests, os, json
from werkzeug.middleware.proxy_fix import ProxyFix
from bson import json_util
from snstwitter import twitter, form, bookwalker
import auth


app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.jinja_env.filters['zip'] = zip


# blueprint register
app.register_blueprint(auth.bp)
app.register_blueprint(twitter.tw, url_prefix='/tw')
app.register_blueprint(form.fm)
app.register_blueprint(bookwalker.sc)
app.wsgi_app = ProxyFix(app.wsgi_app)




@app.route('/')
def index():
    if session.get('user_id') is not None:
        session_user_id = json.loads(session.get('user_id'))
        if isinstance(session_user_id, str):
            g.user_id = session_user_id
        elif isinstance(session_user_id, dict):
            g.user_id = session_user_id['$oid']
            
    else:
        oauth_verifier = request.args.get('oauth_verifier')
        print('oauth_verifier: ', oauth_verifier)
        if oauth_verifier is not None:
            session['user_id'] = json_util.dumps(oauth_verifier)
            g.user_id = oauth_verifier
    return render_template("home.html")




if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)