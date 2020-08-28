"""Scrapes Data from hackersnews using API hnagnolia"
# Imports
import pandas as pd
import json
import requests
import time
from datetime import datetime
from pandas.io.json import json_normalize
# Set current time to start
ts = int(time.time())
hitsPerPage = 1000
print(ts) #feedback
num_processed = 0
# End at this time. 
date_time_str = '31/12/2010'

# conert to datetime for calculations
timelimit = date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y')
print(timelimit)
time2 = datetime.timestamp(timelimit)
# checks current time still greateer than last time
assert ts > time2
# Counts number of processed 
num_processed = 0
# empty dataframe
df = pd.DataFrame()
# MOre Printing of processed time
print("Current Time: ",datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
print("Limit Time: ",timelimit)
# Loop to  go over iteration since API only shows 1000 at a time. 
while ts > time2:
    
  url = 'https://hn.algolia.com/api/v1/search_by_date?tags=comment&hitsPerPage=%s&numericFilters=created_at_i<%s,points>1' % (hitsPerPage, ts)
  print (url)
  req = requests.get(url)
  data = req.json()
  comments = data['hits']
  df = df.append(comments)
  print("Num of comments", data['nbHits'])
  print("Comments this page",len(comments))

  ts = comments[-1 + len(comments)]['created_at_i']
  print("new time:",ts)
  print("NewCommentTime:",datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
  print(url)
  num_processed +=hitsPerPage
  print("Processed:",num_processed)
  print("total_left",data['nbHits'])
  print("remaining: ",ts - time2)
#  time.sleep(3600/10000)
  #print(len(jsonarr))

# for item in jsonarr:
#   df =  df.append(comments)
# print(df.shape)
# df.head()
# Saves final df to csv
df.to_csv('data.csv',index=False)
