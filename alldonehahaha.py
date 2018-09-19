import tweepy
from tweepy import OAuthHandler
import os
import io
import urllib.request
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageFont

consumer_key = 'bvay7XKTdnuVg2TawE3OvY89D'
consumer_secret = '8tDJygIpj9nkmpBUENlFEG5Cxkgny9D2MOISVcdAYfOutNQ9JI'
access_token = '1040111094516404224-Wdo2WoRvvtvnEXVTD7GdqL8J8GJb6y'
access_secret = 'WV0VlSbnpIBNmGTR9nYVcsTAleB4mo48VfqplHayjcJPn'

print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

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
    return images

def conver_mp4():
    command0 = 'ffmpeg -y -r 0.5 -i %03d.jpg -vf scale=-600:600 -y -r 30 -t 60 miniproject1.mp4'
    os.system(command0)

def descript(images):
    client = vision.ImageAnnotatorClient()
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
            thelabel = thelabel + label.description + '\n'
            # print(thelabel)
        font = ImageFont.truetype('/usr/share/fonts/truetype/Gargi/Gargi.ttf',32)
        draw = ImageDraw.Draw(imagelabel)
        draw.text(
            (w / 8, h / 8),
            thelabel,
            fill='yellow',
            font=font
        )
        imagelabel.save(image)

if __name__ == '__main__':
    l = get_images('russwest44')
    descript(l)
    conver_mp4()


