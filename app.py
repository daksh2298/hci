from flask import *
import tweepy
import json

app = Flask(__name__)
CONSUMER_KEY = 'o6mEPsrK6p646e15PXpo5Le6K'
CONSUMER_SECRET = 'TD6pZD871HODoEisFsea13ncIc96gL2TDU6Y6uHXNggszQmCo6'
OAUTH_TOKEN = '3192285595-GogD8gSEWVEqXHbMM8T7RkYmgbveWkqwnSffzMk'
OAUTH_TOKEN_SECRET = 'HDqt9yA52HKsgmWSyNGYLwrCXzrtwOQSoCzcWN5gkbnij'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# filename=open(argfile,'r')
# f=filename.readlines()
# filename.close()

trends1 = api.trends_place('2295405')

# d=api.trends_available()
# dic_woeid={}
# for x in d:
#     dic_woeid[x['name'].lower()]=x['woeid']

trends_woeid=[]
for x in trends1[0]['trends']:
    if x['name'].startswith('#'):
        # print(x)
        temp={}
        temp['name'],temp['query']=(x['name'], x['name'][1:])
        trends_woeid.append(temp)



@app.route('/')
def index():
    return render_template("index.html",trends=trends_woeid)

@app.route('/<hashtag>')
def view_hashtag(hashtag):
    query='#'+hashtag
    searched_tweets = [status._json for status in tweepy.Cursor(api.search, q=query).items(100)]
    # tweets = [json.dumps(json_obj) for json_obj in searched_tweets]
    # print(type(tweets))
    for tweet in searched_tweets:
        print(type(tweet))
    return render_template('view_hashtags.html',tweets=searched_tweets,trends=trends_woeid,hashtag=hashtag)

