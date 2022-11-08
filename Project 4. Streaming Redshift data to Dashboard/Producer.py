#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas as pd
# from sqlalchemy import create_engine

# connstr = 'redshift+psycopg2://awsuser:Shanya#1214@redshift-cluster-1.cccg7kqejxio.us-east-1.redshift.amazonaws.com:5439/dev'

# engine = create_engine(connstr) 
# with engine.connect() as conn, conn.begin():
#    df = pd.read_sql("select * from calls", conn)


# In[2]:


# pip install sqlalchemy


# In[3]:


# pip install sqlalchemy-redshift


# In[8]:



#Temporary code, once cluster is operating, need to inactivate this portion of code

import pandas as pd
df = pd.read_csv('911_Calls_for_Service_(Last_30_Days).csv')
df = df.drop(columns={'X','Y','ObjectId'})


# In[9]:


import time
import json

file_dict = df.to_dict('index')

n = 0
b = 10
for i in file_dict.values():
    with open("for_kinesis/json_file.txt", "a") as f:
        f.write(json.dumps(i)+"\n")
    n+=1
    if n == b:
        b+=10
        time.sleep(1)
    else:
        continue


# In[ ]:




