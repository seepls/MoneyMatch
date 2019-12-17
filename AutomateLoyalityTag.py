# left merge : retail users and transaction to add sensitivity tag.

import pandas as pd 
from datetime import datetime

df1 = pd.read_csv('retailtransx_df.csv', encoding='unicode_escape')
df1['process_datetime'] = pd.to_datetime(df1.process_datetime)
df1['process_month']=df1.process_datetime.dt.month
#df2 = pd.read_csv('')

#df3 = pd.merge(df1, df2 , on = 'user_id' , how = 'left' )

'''
# df3.to_csv('MergedBizUsers.csv')
for id in df2['LoyalOne'] :

	df1['LoyalityTag']= 1 

df1.to_csv('fileRetail.csv')
'''
currentMonth = datetime.now().month
currentYear = datetime.now().year
PrevQuartile = currentMonth - 3  


df1 = df1.drop(df1[df1['process_year'] < currentYear ].index)
df1 = df1.drop(df1[df1['process_month'] < PrevQuartile ].index)
df2=df1[['user_id','is_business']]
df2 = df2.groupby(['user_id'], as_index=False).count()
df3 = df2.rename(columns = { "is_business" : "NoTransQuartile" })

'''

for id1 in df2['LoyalOne']:
    for id2 in df1['user_id']:
        if id1 == id2 :
            df1['LoyalityTag'] = 1 

'''
df3.loc[df3['NoTransQuartile'] < 6, 'LoyalityTag'] = 0
df3.loc[df3['NoTransQuartile'] >= 6, 'LoyalityTag'] = 1

df4 = pd.merge(df1, df3 , on = 'user_id' , how = 'left' )
df4.to_csv('loyalTagmerged.csv')


#auto