import tweepy
from tweepy import OAuthHandler


consumer_key = 'bvay7XKTdnuVg2TawE3OvY89D'
consumer_secret = '8tDJygIpj9nkmpBUENlFEG5Cxkgny9D2MOISVcdAYfOutNQ9JI'
access_token = '1040111094516404224-Wdo2WoRvvtvnEXVTD7GdqL8J8GJb6y'
access_secret = 'WV0VlSbnpIBNmGTR9nYVcsTAleB4mo48VfqplHayjcJPn'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def getTweets(screen_name):
    tweets = api.user_timeline(screen_name=screen_name,count=40,include_rts=False, exclude_replies=True)
    imageList = []
    i = 0
    for status in tweets:
        image = status.entities.get('media', [])
        if(len(image) > 0):
            image_url = status.entities['media'][0]['media_url']
            file_name = "%03d.jpg"%i
            urlretrieve(image_url, file_name)
            imageList.append(file_name)
            i = i + 1
    return imageList






