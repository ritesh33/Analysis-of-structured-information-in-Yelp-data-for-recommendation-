########################################################################
#  Get the number of maximum review done on a particular city by user  #    
########################################################################		
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


# get the data from the User collection and add it to dataframe
def getuserFromUserTable(cursor, columnList):
    df = {}
    for doc in cursor:
        tempdict = {}
        for col in columnList:
            tempdict[col] = doc[col]
        df[doc['user_id']] = tempdict
    return df
	
# get the data from the Business collection and add it to dataframe
def getbusinessFromUserTable(cursor, state):
    df = {}
    for doc in cursor:
        tempdict = {}
        tempdict[state] = doc[state]
        df[doc['business_id']] = tempdict
    return df

# this function returns the city the user reviewed the most	
def getmajorcity(df1,lst):
     dict={}
     lst1={}
     for i in lst:
         for k,v in (df1[i]).items():
             if v in dict.keys():
                dict[v]= dict[v]+1
             else:
                 dict[v]=1
     if not dict:
         return("empty")
     else:
         return(max(dict, key=lambda x: dict[x]))




revdict={}
revdict1={}
with open('d:/ritesh.json', 'r') as f:
    mydict = json.load(f)
revdict.update(mydict)
for key in revdict.keys():
    revdict[key]=list(set(revdict[key]))
df=getuserFromUserTable(db.user.find(),user_cols)
df1=getbusinessFromUserTable(db.businesses.find(),'state')
counter=0
userid = list(df.keys())
for i in userid:
    counter += 1
    if counter % 50000 == 0:
        print(counter)
    if i not in revdict1.keys():
            revdict1[i] = {}
    revdict1[i]=(getmajorcity(df1,revdict[i]))

with open('d:/riteshstate.json', 'w') as fp: #write the result to new JSON file
    json.dump(revdict1, fp)
print(revdict1)




