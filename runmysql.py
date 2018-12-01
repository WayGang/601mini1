from twitterAPI import *
import pymysql

file_path = '/Users/gangwei/Desktop/twitterproject/miniproject1.mp4'
name = input('Who are you:')
twitter_user = input('who you want to find:')

most_popular_disc, labels = go(twitter_user)

image_number = t(twitter_user)
print('The number of images is:',image_number)
time = time_extraction(file_path)


def user():

    db = pymysql.connect("localhost", "root", "WeiGang0502", "twitterdata")
    cursor = db.cursor()
    sql = "INSERT INTO user(name) VALUES(\'%s\')" % (
        name)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def transaction():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "twitterdata")
    cursor = db.cursor()
    sql = "INSERT INTO transaction(user,twitter_user,time) VALUES(\'%s\',\'%s\',\'%s\')" % (
        name,twitter_user,time)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def label():
    for i in range(len(labels)):
        db = pymysql.connect("localhost", "root", "WeiGang0502", "twitterdata")
        cursor = db.cursor()
        sql = "INSERT INTO label(twitter_user,label) VALUES(\'%s\',\'%s\')" % (
            twitter_user, labels[i])
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()

def twitter():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "twitterdata")
    cursor = db.cursor()
    sql = "INSERT INTO twitter(twitter_user,image_number,most_popular_disc) VALUES(\'%s\',\'%s\',\'%s\')" % (
        twitter_user,image_number,most_popular_disc)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()



user()
transaction()
label()
twitter()
