#! /usr/bin/python3.5

import tweepy
import json
from keys import keys
import sys

''' 
Função que faz uso da API GET User 
coletando dados um determinado usuário 
pelo screen_name ou id.
Retorna um json com os principais atributos.
'''
def getUser(api, uname):
    user_datas = api.get_user(uname)
    user_datas = json.loads(json.dumps(user_datas._json))
    user = {}
    user.update({'nome' : user_datas[u'name']})
    user.update({'id': user_datas[u'id']})
    user.update({'screen_name' : user_datas[u'screen_name']})
    user.update({'criado_em': user_datas[u'created_at']})
    user.update({'seguindo' : user_datas[u'friends_count']})
    user.update({'tweets_total': user_datas[u'statuses_count']})
    user.update({'seguidores': user_datas[u'followers_count']})
    user.update({'descricao' : user_datas[u'description']})
    user.update({'favoritos:' : user_datas[u'favourites_count']})
    return user

'''
Funçao que retorna todos os tweets, sendo do
mais recente pro mais antigo. Retorno por padrão 
100 tweets(limitado pela api 180/15m max:3200) .
'''
def getTweets(api, uname, total=100):
    tweets = []
    [tweets.append(json.loads(json.dumps(timeline._json))[u'text']) for timeline in tweepy.Cursor(api.user_timeline , id=uname).items(total)]
    return tweets       

'''
Funçao que retorna todos os followers, sendo do
mais recente pro mais antigo. Retorno por padrão 
10 followers(limitado pela api 20/15m max:300) .
'''
def getFollowers(api, uname, total=10):
    followers = []
    [followers.append(json.loads(json.dumps(follow._json))[u'screen_name']) for follow in tweepy.Cursor(api.followers, id=uname).items(total)]
    return followers

'''
Funçao que retorna todos os friends, sendo do
mais recente pro mais antigo. Retorno por padrão 
10 friends(limitado pela api 20/15m max:300) .
'''
def getFriends(api, uname, total=10):
    friends = []
    [friends.append(json.loads(json.dumps(friend._json))[u'screen_name']) for friend in tweepy.Cursor(api.friends, id=uname).items(total)]
    return friends

'''
returna um conector com a API
'''
def connect(worl, worln):             
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    return tweepy.API(auth, wait_on_rate_limit=worl, wait_on_rate_limit_notify=worln)

if __name__ == '__main__':
    if sys.argv[4] == 1:
        api = connect(True, True)
    else:
        api = connect(False, False)