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

# get the data from the Users collection and add it to dataframe
def getuserFromUserTable(cursor, columnList):
    df = {}
    for doc in cursor:
        tempdict = {}
        for col in columnList:
            tempdict[col] = doc[col]
        df[doc['user_id']] = tempdict
    return df

revdict={}
revdict1={}
df=getuserFromUserTable(db.user.find(),user_cols)
counter=0
userid = list(df.keys())
for i in userid:
    counter += 1
    if counter % 50000 == 0:
        print(counter)
    if i not in revdict1.keys():
            revdict1[i] = {}
    if df[i]['fans'] == 0:
        revdict1[i] = "0"
    elif df[i]['fans'] >0 and df[i]['fans']<=100:
        revdict1[i] = "1-100"
    elif df[i]['fans'] > 100 and df[i]['fans'] <= 200:
        revdict1[i] ="101-200"
    elif df[i]['fans'] > 200 and df[i]['fans'] <= 300:
        revdict1[i] ="201-300"
    elif df[i]['fans'] > 300 and df[i]['fans'] <= 400:
        revdict1[i] ="301-400"
    elif df[i]['fans'] > 400 and df[i]['fans'] <= 500:
        revdict1[i] ="401-500"
    elif df[i]['fans'] > 500 and df[i]['fans'] <= 600:
        revdict1[i] ="501-600"
    elif df[i]['fans'] > 600 and df[i]['fans'] <= 700:
        revdict1[i] ="601-700"
    elif df[i]['fans'] > 700 and df[i]['fans'] <= 800:
        revdict1[i] ="701-800"
    elif df[i]['fans'] > 800 and df[i]['fans'] <= 900:
        revdict1[i] = "801-900"
    elif df[i]['fans'] > 900 and df[i]['fans'] <= 1000:
        revdict1[i] ="901-1000"
    elif df[i]['fans'] >1000 and df[i]['fans']<=1100:
        revdict1[i] = "1001-1100"
    elif df[i]['fans'] >1100 and df[i]['fans']<=1200:
        revdict1[i] ="1101-1200"
    elif df[i]['fans'] > 1200 and df[i]['fans'] <= 1300:
        revdict1[i] ="1201-1300"
    elif df[i]['fans'] > 1300 and df[i]['fans'] <= 1400:
        revdict1[i] ="1301-1400"
    elif df[i]['fans'] > 1400 and df[i]['fans'] <= 1500:
        revdict1[i] ="1401-1500"
    elif df[i]['fans'] > 1500 and df[i]['fans'] <= 1600:
        revdict1[i] ="1501-1600"
    elif df[i]['fans'] > 1600 and df[i]['fans'] <= 1700:
        revdict1[i] ="1601-1700"
    elif df[i]['fans'] > 1700 and df[i]['fans'] <= 1800:
        revdict1[i] ="1701-1800"
    elif df[i]['fans'] > 1800 and df[i]['fans'] <= 1900:
        revdict1[i] ="1801-1900"
    elif df[i]['fans'] > 1900 and df[i]['fans'] <= 2000:
        revdict1[i] ="1901-2000"
    elif df[i]['fans'] > 2000 and df[i]['fans'] <= 2100:
        revdict1[i] ="2001-2100"
    elif df[i]['fans'] >2100 and df[i]['fans']<=2200:
        revdict1[i] ="2101-2200"
    elif df[i]['fans'] >2200 and df[i]['fans']<=2300:
        revdict1[i] ="2201-2300"
    elif df[i]['fans'] > 2300 and df[i]['fans'] <= 2400:
        revdict1[i] ="2301-2400"
    elif df[i]['fans'] > 2400 and df[i]['fans'] <= 2500:
        revdict1[i] ="2401-2500"
    elif df[i]['fans'] > 2500 and df[i]['fans'] <= 2600:
        revdict1[i] = "2501-2600"
    elif df[i]['fans'] > 2600 and df[i]['fans'] <= 2700:
        revdict1[i] ="2601-2700"
    elif df[i]['fans'] > 2700 and df[i]['fans'] <= 2800:
        revdict1[i] = "2701-2800"
    elif df[i]['fans'] > 2800 and df[i]['fans'] <= 2900:
        revdict1[i] = "2801-2900"
    elif df[i]['fans'] > 2900 and df[i]['fans'] <= 3000:
        revdict1[i] ="2901-3000"
    elif df[i]['fans'] > 3000:
        revdict1[i] = ">3001"

with open('d:/riteshfans.json', 'w') as fp: # Write the result to the new JSON file
    json.dump(revdict1, fp)
print(revdict1)




