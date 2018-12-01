#!/usr/bin/python3
from twitterAPI import *
import pymongo

file_path = input('Store path:') #/Users/gangwei/Desktop/twitterproject/miniproject1.mp4
name = input('Who are you:')
twitter_user = input('who you want to find:')

most_popular_disc, labels = go(twitter_user)

image_number = t(twitter_user)
print('The number of images is:',image_number)
time = time_extraction(file_path)

def insert():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["twitter"]
    mycol = mydb["data"]

    mydict = {"user name": name, "twitter name": twitter_user, "time": time, "most_popular_disc": most_popular_disc,}

    x = mycol.insert_one(mydict)
    print(x)

def query():
    #twho = input("who you want to find:")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["twitter"]
    mycol = mydb["data"]
    myquery = {"twitter name": "russwest44"}
    #mydoc = mycol.find(myquery)
    for x in mycol.find():
        print(x)

insert()
query()
