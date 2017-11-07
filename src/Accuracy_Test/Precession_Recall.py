##################################################################
#  Calculate the presssion and the recall to test the accuracy   #
##################################################################

import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt
from pymongo import MongoClient
import json
import math
import operator
from collections import OrderedDict
from operator import itemgetter
#DATABASE CONNECTIVITY
client = MongoClient()
db = client.yelp
user_cols= ['type','user_id','name','review_count','average_stars','votes','friends','elite','yelping_since','compliments','fans']

# read the collection and add it to the dataframe
def getDictionaryFromUserTable(cursor, columnList):
    df = {}
    for doc in cursor:
        tempdict = {}
        for col in columnList:
            tempdict[col] = doc[col]
        df[doc['user_id']] = tempdict
    return df

# get the mutual friends between the users
def getfriendsandfriendsoffriends(df, userid):
    ls = df[userid]['friends']
    for l in ls:
        ls = list(set().union(df[l]['friends'], ls))
    return(ls)

# This function is used to calculate the Hamming distance between the users
def significance(user1, g, df,revdict,revdict1,revdict2):
    dict1 = {}
    for r in g:
        count = 0
        percentage = 0
        i = df[user1]
        j = df[r]
        if revdict[user1] == revdict[r]:
            count=count+1
        if revdict1[user1] == revdict1[r]:
            count=count+1
        if revdict2[user1] == revdict2[r]:
            count=count+1
        if math.ceil(i['average_stars']) == math.ceil(j['average_stars']):
            count = count + 1
        if i['review_count'] == j['review_count']:
            count = count + 1
        fri = 0
        for x in i['friends']:
            for y in j['friends']:
                if x in y:
                    fri = fri + 1
        if fri <= 0:
            percentage = 0
        else:
            percentage = ((fri / (len(i['friends']) + len(j['friends']))) * 100)
        if (percentage > 30):
            count = count + 1

        dict1[r] = count
    return ((sorted(dict1, key=dict1.get,reverse=True))[:20])
revdict={}
revdict1={}
revdict2={}

with open('d:/riteshfans.json', 'r') as f: # read the fans collection and add it to the dataframe
    mydict = json.load(f)
revdict.update(mydict)

with open('d:/riteshcategory.json', 'r') as f: # read the category collection and add it to the dataframe
    mydict = json.load(f)
revdict1.update(mydict)

with open('d:/riteshcity.json', 'r') as f: # read the data from the major_city JSON file calculated by City.py and add it to the dataframe
    mydict = json.load(f)
revdict2.update(mydict)

df={}
df= (getDictionaryFromUserTable(db.user.find(), user_cols))
precession=0
recall=0
count1=0
for i in range(1, 100):
    res=0
    userid = list(df.keys())[i]
    lst=(getfriendsandfriendsoffriends(df, userid))
    lst3= significance(userid,lst,df,revdict,revdict1,revdict2)
    for f in lst3:
        for c in df[userid]['friends']:
            if f == c:
                res=res+1
    if res != 0 :
        count1=count1+1
        precession= precession+ (res/5)
        recall=recall+ (res/len(lst))

print((precession/count1),(recall/count1))


