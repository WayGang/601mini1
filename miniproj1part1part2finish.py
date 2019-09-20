import tweepy
from tweepy import OAuthHandler
import os
import io
import wget
import urllib3.request
from google.cloud import vision
from google.cloud.vision import types

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def get_images(inputName):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='inputName',count=30, include_rts=False,exclude_replies=True)
    images = []
    i = 0
    for status in tweets:
        image = status.entities.get('media', [])
        if(len(image) > 0):
            image_url = status.entities['media'][0]['media_url']
            file_name = "%03d.jpg"%i
            urllib3.request.urlretrieve(image_url, file_name)
            images.append(file_name)
            i = i+1

    return images

get_images('kobebryant')

'''def conver_mp4():
    command0 = 'ffmpeg -y -r 0.5 -i %03d.jpg -vf scale=-600:600 -y -r 30 -t 60 test.mp4'
    os.system(command0)

def descript():


    client = vision.ImageAnnotatorClient()


    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/wakeupcat.jpg')

    for image in image_file
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)



'''
