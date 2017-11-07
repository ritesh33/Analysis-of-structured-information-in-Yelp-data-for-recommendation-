##############################################################################################
#  Return the Dictonary with userId as key with the category name the user reveiwed the most #
##############################################################################################							

import numpy as np
import pandas as pd
import collections
import json
from pymongo import MongoClient
#DATABASE CONNECTIVITY
client = MongoClient()
db = client.yelp

#Global variable declarations
business_cols= ['type','business_id','name','neighborhoods','full_address','city','state','latitude','longitude','stars','review_count','categories','open','hours','attributes']
review_cols= ['type','business_id','user_id','stars','date','votes']
user_cols= ['type','user_id','name','review_count','average_stars','votes','friends','elite','yelping_since','compliments','fans']
checkin_cols= ['type','business_id','checkin_info']
tip_cols= ['type','text','business_id','user_id','date','likes']
lst3=['Food','Nightlife','Restaurants','Shopping','Active Life','Arts & Entertainment','Automotive','Beauty & Spas','Education','Event Planning & Services','Health & Medical','Home Services','Local Services','Financial Services','Hotels & Travel','Local Flavor','Mass Media','Pets','Professional Services','Public Services & Government','Real Estate','Religious Organizations']


# get the data from the User Colections
def getuserFromUserTable(cursor, columnList):
    df = {}
    for doc in cursor:
        tempdict = {}
        for col in columnList:
            tempdict[col] = doc[col]
        df[doc['user_id']] = tempdict
    return df
	
#get the data from the Business collections
def getbusinessFromUserTable(cursor, state):
    df = {}
    for doc in cursor:
        tempdict = {}
        tempdict[state] = doc[state]
        df[doc['business_id']] = tempdict
    return df

#function used in finding the major category the user is reviewing
def major_cat(df1,lst):
    dict1={}
    for i in lst:
        for t in df1[i]['categories']:
            if t in lst3:
                if t in dict1.keys():
                    dict1[t]=dict1[t]+1
                else:
                    dict1[t]=1
    if not dict1:
        return "empty"
    else:
        return(max(dict1, key=lambda i: dict1[i]))


revdict={}
revdict1={}
with open('d:/ritesh.json', 'r') as f:
    mydict = json.load(f)
revdict.update(mydict)
for key in revdict.keys():
    revdict[key]=list(set(revdict[key]))
df=getuserFromUserTable(db.user.find(),user_cols)
df1=getbusinessFromUserTable(db.businesses.find(),'categories')
counter=0
userid = list(df.keys())
for i in userid:
    counter += 1
    if counter % 50000 == 0:
        print(counter)
    if i not in revdict1.keys():
            revdict1[i] = {}
    revdict1[i]=(major_cat(df1,revdict[i]))

with open('d:/riteshcategory.json', 'w') as fp: #create a new JSON file and add the result to the file
    json.dump(revdict1, fp)
print(revdict1)




