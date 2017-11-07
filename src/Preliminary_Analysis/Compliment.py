#####################################################
# Maximum type of compliement given to the user		#
#####################################################
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

# get the data from the User collections and add it to dataframe
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


dict1={}
usr = (getDataFrameFromTable(db.users.find(), user_cols))
for x,j in zip(usr['compliments'], usr['user_id']):
    if not x :
        dict1[j]="empty"
    else:
        dict1[j]= max(x, key=lambda i: x[i])
print(dict1)