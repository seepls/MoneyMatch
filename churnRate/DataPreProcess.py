import pandas as pd
import numpy as np
import math
import os
from datetime import datetime


bizusers_df = pd.read_csv('bizusers_df.csv', encoding='unicode_escape')
biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')
biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month

#add 6 column for total number of orders in each prev 6 month
currentYear = datetime.now().year
currentMonth = datetime.now().month

biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] < currentYear ].index)

order_M1 = biztransx_df[['user_id','is_business','process_month']]
order_M1 = order_M1.drop(order_M1[order_M1['process_month'] != (currentMonth - 1)  ].index)
order_M1=order_M1[['user_id','is_business']]
order_M1 = order_M1.groupby(['user_id'], as_index=False).count()

order_M2 = biztransx_df[['user_id','is_business','process_month']]
order_M2 = order_M2.drop(order_M2[order_M2['process_month'] != (currentMonth - 2)  ].index)
order_M2 = order_M2[['user_id','is_business']]
order_M2 = order_M2.groupby(['user_id'], as_index=False).count()


order_M3 = biztransx_df[['user_id','is_business','process_month']]
order_M3 = order_M3.drop(order_M3[order_M3['process_month'] != (currentMonth - 3)  ].index)
order_M3 = order_M3[['user_id','is_business']]
order_M3 = order_M3.groupby(['user_id'], as_index=False).count()


order_M4 = biztransx_df[['user_id','is_business','process_month']]
order_M4 = order_M4.drop(order_M4[order_M4['process_month'] != (currentMonth - 4)  ].index)
order_M4 = order_M4[['user_id','is_business']]
order_M4 = order_M4.groupby(['user_id'], as_index=False).count()



order_M5 = biztransx_df[['user_id','is_business','process_month']]
order_M5 = order_M5.drop(order_M5[order_M5['process_month'] != (currentMonth - 5)  ].index)
order_M5 = order_M5[['user_id','is_business']]
order_M5 = order_M5.groupby(['user_id'], as_index=False).count()


order_M6 = biztransx_df[['user_id','is_business','process_month']]
order_M6 = order_M6.drop(order_M6[order_M6['process_month'] != (currentMonth - 6)  ].index)
order_M6 = order_M6[['user_id','is_business']]
order_M6 = order_M6.groupby(['user_id'], as_index=False).count()



# add 6  column for total volumne of orders in each month

volume_M1 = biztransx_df[['user_id','amount','process_month']]
volume_M1 = volume_M1.drop(volume_M1[volume_M1['process_month'] != (currentMonth - 1)  ].index)
volume_M1 = volume_M1[['user_id','amount']]
volume_M1 = volume_M1.groupby(['user_id'], as_index=False).sum()

volume_M2 = biztransx_df[['user_id','amount','process_month']]
volume_M2 = volume_M2.drop(volume_M2[volume_M2['process_month'] != (currentMonth - 2)  ].index)
volume_M2 = volume_M2[['user_id','amount']]
volume_M2 = volume_M2.groupby(['user_id'], as_index=False).sum()


volume_M3 = biztransx_df[['user_id','amount','process_month']]
volume_M3 = volume_M3.drop(volume_M3[volume_M3['process_month'] != (currentMonth - 3)  ].index)
volume_M3 = volume_M3[['user_id','amount']]
volume_M3 = volume_M3.groupby(['user_id'], as_index=False).sum()


volume_M4 = biztransx_df[['user_id','amount','process_month']]
volume_M4 = volume_M4.drop(volume_M4[volume_M4['process_month'] != (currentMonth - 4)  ].index)
volume_M4 = volume_M4[['user_id','amount']]
volume_M4 = volume_M4.groupby(['user_id'], as_index=False).sum()



volume_M5 = biztransx_df[['user_id','amount','process_month']]
volume_M5 = volume_M5.drop(volume_M5[volume_M5['process_month'] != (currentMonth - 5)  ].index)
volume_M5 = volume_M5[['user_id','amount']]
volume_M5 = volume_M5.groupby(['user_id'], as_index=False).sum()


volume_M6 = biztransx_df[['user_id','amount','process_month']]
volume_M6 = volume_M6.drop(volume_M6[volume_M6['process_month'] != (currentMonth - 6)  ].index)
volume_M6 = volume_M6[['user_id','amount']]
volume_M6 = volume_M6.groupby(['user_id'], as_index=False).sum()


# add 6 column for total type of currency in each month

currency_M1 = biztransx_df[['user_id','target_currency','process_month']]
currency_M1 = currency_M1.drop(currency_M1[currency_M1['process_month'] != (currentMonth - 2)  ].index)
currency_M1 = currency_M1[['user_id','target_currency']]
currency_M1=currency_M1.groupby('user_id',as_index=True).target_currency.nunique()
currency_M1=currency_M1.reset_index(drop=False)

currency_M2 = biztransx_df[['user_id','target_currency','process_month']]
currency_M2 = currency_M2.drop(currency_M2[currency_M2['process_month'] != (currentMonth - 3)  ].index)
currency_M2 = currency_M2[['user_id','target_currency']]
currency_M2=currency_M2.groupby('user_id',as_index=True).target_currency.nunique()
currency_M2=currency_M2.reset_index(drop=False)

currency_M3 = biztransx_df[['user_id','target_currency','process_month']]
currency_M3 = currency_M3.drop(currency_M3[currency_M3['process_month'] != (currentMonth - 4)  ].index)
currency_M3 = currency_M3[['user_id','target_currency']]
currency_M3=currency_M3.groupby('user_id',as_index=True).target_currency.nunique()
currency_M3=currency_M3.reset_index(drop=False)

currency_M4 = biztransx_df[['user_id','target_currency','process_month']]
currency_M4 = currency_M4.drop(currency_M4[currency_M4['process_month'] != (currentMonth - 5)  ].index)
currency_M4 = currency_M4[['user_id','target_currency']]
currency_M4=currency_M4.groupby('user_id',as_index=True).target_currency.nunique()
currency_M4=currency_M4.reset_index(drop=False)

currency_M5 = biztransx_df[['user_id','target_currency','process_month']]
currency_M5 = currency_M5.drop(currency_M5[currency_M5['process_month'] != (currentMonth - 6)  ].index)
currency_M5 = currency_M5[['user_id','target_currency']]
currency_M5=currency_M5.groupby('user_id',as_index=True).target_currency.nunique()
currency_M5=currency_M5.reset_index(drop=False)

currency_M6 = biztransx_df[['user_id','target_currency','process_month']]
currency_M6 = currency_M6.drop(currency_M6[currency_M6['process_month'] != (currentMonth - 6)  ].index)
currency_M6 = currency_M6[['user_id','target_currency']]
currency_M6=currency_M6.groupby('user_id',as_index=True).target_currency.nunique()
currency_M6=currency_M6.reset_index(drop=False)

for col in bizusers_df.columns:
    print(col)


bizusers_df=pd.merge(bizusers_df,volume_M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_M2,on='user_id',how='left')

bizusers_df=pd.merge(bizusers_df,currency_M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_M1,on='user_id',how='left')

bizusers_df=pd.merge(bizusers_df,order_M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_M2,on='user_id',how='left')

for col in bizusers_df.columns:
    print(col)

bizusers_df.to_csv('BusinessAnalysis.csv')

'''
for col in bizusers_df.columns :
    print(col)
   
for col in biztransx_df.columns :
    print(col)
'''