#######################################################
# Get the number of mutual frined between the users   #
#######################################################
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

# returns the number of mutual frineds between the users
def mutual(user1,user2):
    count=0
    usr1 = (getDataFrameFromTable(db.users.find({"user_id":user1}), user_cols))
    usr2 = (getDataFrameFromTable(db.users.find({"user_id":user2}), user_cols))
    for i,j in zip(usr1['friends'],usr2['friends']):
        for x in i:
            for y in j:
                if x in y:
                    count=count+1
    print(count)


mutual("SIBCL7HBkrP4llolm4SC2A","fHtTaujcyKvXglE33Z5yIw")