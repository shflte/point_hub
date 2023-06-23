from flask_oauthlib.client import OAuth
from dotenv import load_dotenv

oauth = OAuth()

google = oauth.remote_app(
    'google',
    consumer_key=load_dotenv("GOOGLE_CLIENT_ID"),
    consumer_secret=load_dotenv("GOOGLE_CLIENT_SECRET"),
    request_token_params={
        'scope': 'email profile'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth'
)

def init_oauth(app):
    oauth.init_app(app)
