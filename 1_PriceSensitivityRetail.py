
#Importing Libraries
import numpy as np
import pandas as pd
import math
import os
from matplotlib import pyplot as plt

#Importing Dataset (Train set contains cleaned purpose of teansactions for old customers, 
#retailtransx nd retailusers are updates merged tranx and user files)'''

CleanTxnData=pd.read_csv('Train.csv', encoding='unicode_escape')
CleanStateData=pd.read_csv('State_Cleaned.csv')
RetailTxn_df=pd.read_csv('retailtransx_df.csv', encoding='unicode_escape')
RetailUser_df=pd.read_csv('retailusers_df.csv', encoding='unicode_escape')

#Mergig Purpose of Transaction on new data
for col in CleanTxnData.columns:
    print(col)

NewPoT=CleanTxnData[['transfer_order_id', 'purpose_of_transaction_new']]

RetailTxn_df=pd.merge(RetailTxn_df, NewPoT, on='transfer_order_id', how='left')

# Completing purpose of transaction new column
RetailTxn_df.purpose_of_transaction_new.value_counts()
RetailTxn_df.purpose_of_transaction_new.fillna(RetailTxn_df.purpose_of_transaction, inplace=True)
del RetailTxn_df['purpose_of_transaction']
RetailTxn_df.rename(columns={'purpose_of_transaction_new':'purpose_of_transaction'}, inplace=True)

#StatesCleaned
for col in CleanStateData.columns:
    print(col)
    
NewState=CleanStateData[['user_id', 'state']]

RetailUser_df=pd.merge(RetailUser_df, NewState, on='user_id', how='left')

for col in RetailUser_df.columns:
    print(col)
    
# Completing Clean state column
RetailUser_df.state_y.value_counts()
RetailUser_df.state_y.fillna(RetailUser_df.state_x, inplace=True)
RetailUser_df.state_y.value_counts()
del RetailUser_df['state_x']
RetailUser_df.rename(columns={'state_y':'state'}, inplace=True)

# Deletig entries with zero interbank rate
RetailTxn_df=RetailTxn_df.drop(RetailTxn_df[RetailTxn_df['interbank_rate']==0].index)

#Calculating Price Sensitivity proxy
RetailTxn_df['PSProxy'] = RetailTxn_df['interbank_rate']- RetailTxn_df['midrate'] 
RetailTxn_df['PSProxy']=RetailTxn_df['PSProxy']/RetailTxn_df['interbank_rate']
RetailTxn_df['PSProxy']=RetailTxn_df['PSProxy']*100

#To analyse the statistic of PSProxy
#RetailTxn_df.to_csv('Stats.csv')
RetailTxn_df['PSProxy'].describe()

#Removing Outlier
RetailTxn_df=RetailTxn_df.drop(RetailTxn_df[RetailTxn_df['PSProxy']>17].index)

#Columns in Retail Txn
for col in RetailTxn_df.columns:
    print(col)

#Deleting negative coupon entries
RetailTxn_df.coupon_amount_myr.value_counts()
RetailTxn_df=RetailTxn_df.drop(RetailTxn_df[RetailTxn_df['coupon_amount_myr']<0].index)

#Making a new database with average of the Proxy over all transactions for every customer
PS_df=RetailTxn_df[['user_id', 'PSProxy' ]]
PS_df=PS_df.groupby(['user_id'], as_index=False).mean()

#Making a new database with sum of coupon amount and count over all transactions
CoupAmt_df=RetailTxn_df[['user_id', 'coupon_amount_myr','coupon_used' ]]
CoupAmt_df=CoupAmt_df.groupby(['user_id'], as_index=False).sum()

#Merging the coupon detail and Proxy detail
RetailPS_df=pd.merge(PS_df,CoupAmt_df,on='user_id', how='left')

#Merging user data on this to create our base
RetailBase_df=pd.merge(RetailPS_df, RetailUser_df,on='user_id', how='left')

#Statistics of Avg PS Proxy
RetailBase_df.PSProxy.describe()

#Division on the basis of Quartiles
RetailBase_df.loc[RetailBase_df['PSProxy']<=0.45, 'SensitivityTag'] = 'H'
RetailBase_df.loc[(RetailBase_df['PSProxy']>0.45)&(RetailBase_df['PSProxy']<=0.65), 'SensitivityTag'] = 'M'
RetailBase_df.loc[(RetailBase_df['PSProxy']>0.65), 'SensitivityTag'] = 'L'


#Finding mean and variance of the Proxy for classifying it into different categories
'''Mean=df1.loc[:,'PSProxyNew'].mean()
Vairance=df1.loc[:,'PSProxyNew'].var()
StdD=math.sqrt(Vairance)'''

#Division on basis of variance (25%,50%,75% and above)
'''def f(df1):
    if (df1['PSProxyNew'] <= Mean+0.25*StdD and df1['PSProxyNew']>=Mean-0.25*StdD):
        val = 'H'
    elif(df1['PSProxyNew'] <= Mean+0.5*StdD and df1['PSProxyNew']>=Mean-0.5*StdD):
        val = 'M'
    else:
        val = 'L'
    return val

df1['SensitivityTag'] = df1.apply(f, axis=1)'''

RetailBase_df.to_csv('PriceSensitivity.csv')
RetailBase_df.SensitivityTag.value_counts()
