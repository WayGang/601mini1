import tweepy
from tweepy import OAuthHandler
import os
import io
import urllib.request

consumer_key = 'bvay7XKTdnuVg2TawE3OvY89D'
consumer_secret = '8tDJygIpj9nkmpBUENlFEG5Cxkgny9D2MOISVcdAYfOutNQ9JI'
access_token = '1040111094516404224-Wdo2WoRvvtvnEXVTD7GdqL8J8GJb6y'
access_secret = 'WV0VlSbnpIBNmGTR9nYVcsTAleB4mo48VfqplHayjcJPn'

def get_images(inputName):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=inputName,count=30, include_rts=False,exclude_replies=True)
    images = []
    i = 0
    for status in tweets:
        image = status.entities.get('media', [])
        if(len(image) > 0):
            image_url = status.entities['media'][0]['media_url']
            file_name = "%03d.jpg"%i
            urllib.request.urlretrieve(image_url, file_name)
            images.append(file_name)
            i = i+1

    return images
def conver_mp4():
    command0 = 'ffmpeg -y -r 0.5 -i %03d.jpg -vf scale=-600:600 -y -r 30 -t 60 test.mp4'
    os.system(command0)

if __name__ == '__main__':
    get_images('kobebryant')
    conver_mp4()

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()