import csv

#df = pd.read_csv('mdl_logstore_standard_log.csv', low_memory=False)

#df.head()

import pandas as pd
#chunksize = 20000

cols = ['username', 'eventname']
event_names = []

df = pd.read_csv('mdl_logstore_standard_log.csv', usecols=cols)


df = df[df.eventname == ('\mod_forum\event\discussion_viewed' or '\mod_forum\event\post_created' or '\mod_forum\event\discussion_subscription_created' or '\mod_forum\event\discussion_created' or '\mod_forum\event\post_updated')]

print(df)

userlist = {}

for index, row in df.iterrows():
    if row['username'] in userlist:
        userlist[row['username']] += 1
    else:
        userlist[row['username']] = 1

print('done')
userlist =  sorted(userlist.items(), key=lambda kv: kv[1], reverse=True)

with open('forum.csv', 'w') as f:
    f.write('username,forum_interactions\n')
    for user in userlist:
        f.write(user[0]+','+str(user[1])+'\n')
