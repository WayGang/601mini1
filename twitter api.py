import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'bvay7XKTdnuVg2TawE3OvY89D'
consumer_secret = '8tDJygIpj9nkmpBUENlFEG5Cxkgny9D2MOISVcdAYfOutNQ9JI'
access_token = '1040111094516404224-Wdo2WoRvvtvnEXVTD7GdqL8J8GJb6y'
access_secret = 'WV0VlSbnpIBNmGTR9nYVcsTAleB4mo48VfqplHayjcJPn'


@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
