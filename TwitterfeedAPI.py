import tweepy
from tweepy import OAuthHandler
import os
import io
import urllib.request
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageFont
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/gangwei/Downloads/MyProject-08c6d528bd01.json"


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
            image_name = "%03d.jpg"%i
            urllib.request.urlretrieve(image_url, image_name)
            images.append(image_name)
            i = i+1
    lenth = len(images)
    return images, lenth

def conver_mp4():
    command0 = 'ffmpeg -y -r 0.5 -i %03d.jpg -vf scale=-600:600 -y -r 30 -t 60 miniproject1.mp4'
    os.system(command0)

def descript(images):
    client = vision.ImageAnnotatorClient()
    every = {}
    all = []
    for image in images:
        with io.open(image, 'rb') as images:
            image_content = images.read()
        image_descript = types.Image(content=image_content)

        response = client.label_detection(image=image_descript)
        labels = response.label_annotations

        imagelabel = Image.open(image)
        (w,h) = imagelabel.size

        thelabel = ''
        for label in labels:
            #thelabel = thelabel + label.description + '\n'
            #print(thelabel)
            all.append(label.description)
            if label.description in every:
                every[label.description] += 1
            else:
                every[label.description] = 1

        font = ImageFont.truetype('/library/Fonts/Trattatello.ttf',32)
        draw = ImageDraw.Draw(imagelabel)
        draw.text(
            (w / 8, h / 8),
            thelabel,
            fill='yellow',
            font=font
        )
        imagelabel.save(image)
    most_popular_disc = max(every, key=every.get)
    print(most_popular_disc)
    print(all)
    return most_popular_disc,all

def go(a):
    l, t = get_images(a)
    m, a = descript(l)
    conver_mp4()
    return m,a

def t(a):
    l, t = get_images(a)
    return t


def time_extraction(file_path):

    t = os.path.getctime(file_path)
    timeStruct = time.localtime(t)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

