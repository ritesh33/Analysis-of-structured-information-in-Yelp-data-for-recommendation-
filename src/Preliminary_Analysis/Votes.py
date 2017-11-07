####################################################
# Get the maximum type of vote given to the user   #
####################################################

import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt
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

# get the data from the collection and add it to dataframe
def getDataFrameFromTable(cursor, columnList):
    df=pd.DataFrame()
    ls=[]
    for doc in cursor:
        temp_ls=[]
        for col in columnList:
            temp_ls.append(doc[col])
        ls.append(temp_ls)
    df=pd.DataFrame(ls,columns=columnList)
    return df

# gets the type of major vote given to the user 
def major_votes(user):
    rev = db.reviews.find({"user_id":user})
    for j in rev[:1]:
        return(max(j['votes'], key=lambda k: j['votes'][k]))

usr=db.user.find(no_cursor_timeout=True)
for i in usr:
    db.user.update({"user_id":i['user_id']}, {"$set": {"major_votes": major_votes(i['user_id'])}})
print("end")

