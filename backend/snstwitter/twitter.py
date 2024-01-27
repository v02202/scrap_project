import os, requests
from flask import Blueprint, redirect, url_for
from requests_oauthlib.oauth1_auth import Client


tw = Blueprint('tw', __name__, url_prefix='/twitter')


oauth = Client(os.getenv('TWITTER_API_KEY'), client_secret=os.getenv('TWITTER_API_SECRET'))

@tw.route("/login", methods=['GET'])
def twitter_login():


    uri, headers, body = oauth.sign('https://twitter.com/oauth/request_token')
    res = requests.get(uri, headers=headers, data=body)
    
    print(res.status_code, res.text)
    res_split = res.text.split('&') 
   
    oauth_token = res_split[0].split('=')[1] # Pulling our APPS OAuth token from the response.
    # Now we have to redirect to the login URL using our OAuth Token
    return redirect('https://api.twitter.com/oauth/authenticate?oauth_token=' + oauth_token, 302)