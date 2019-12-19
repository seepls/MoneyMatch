import pandas as pd
import numpy as np
import math
import os
from datetime import datetime



bizusers_df = pd.read_csv('bizusers_df.csv', encoding='unicode_escape')
biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')

# number of churn in each quarter 
# process_quarter 
# process_year

# whole important data in one data frame : Transx 
Transx = biztransx_df[['user_id','process_year','process_quarter']]

# 2019 
Churn_2019 = Transx.drop(Transx[Transx['process_year'] < 2019  ].index)
Churn_2019_Q = Churn_2019[['user_id','process_quarter']]
#Churn_2019_Q1 = Churn_2019_Q1.drop(Churn_2019_Q1[Churn_2019_Q1['process_quarter'] != "Q1"  ].index)


# adding Q1 to show if transax in Q1 

Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] == 'Q1' , 'Q1'] = 1
Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] != 'Q1', 'Q1'] = 0

# adding Q2 to show if transax in Q2 

Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] == 'Q2' , 'Q2'] = 1
Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] != 'Q2', 'Q2'] = 0

# adding Q3 to show if transax in Q3

Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] == 'Q3' , 'Q3'] = 1
Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] != 'Q3', 'Q3'] = 0

# adding Q4 to show if transax in Q4 

Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] == 'Q4' , 'Q4'] = 1
Churn_2019_Q.loc[Churn_2019_Q['process_quarter'] != 'Q4', 'Q4'] = 0

# dropping column = ' process_quarter'
Churn_2019_Q = Churn_2019_Q[['user_id','Q1','Q2','Q3','Q4']]
Churn_2019_Q = Churn_2019_Q.groupby(['user_id'], as_index=False).sum()

# if transx in Q1 ChurnQ1 =0 , ELSE 1
Churn_2019_Q.loc[Churn_2019_Q['Q1']== 0 , 'Churn19Q1'] = 1 
Churn_2019_Q.loc[Churn_2019_Q['Q1']!= 0 , 'Churn19Q1'] = 0

# if transx in Q2 ChurnQ1 =0 , ELSE 1
Churn_2019_Q.loc[Churn_2019_Q['Q2']== 0 , 'Churn19Q2'] = 1 
Churn_2019_Q.loc[Churn_2019_Q['Q2']!= 0 , 'Churn19Q2'] = 0

# if transx in Q1 ChurnQ1 =0 , ELSE 1
Churn_2019_Q.loc[Churn_2019_Q['Q3']== 0 , 'Churn19Q3'] = 1 
Churn_2019_Q.loc[Churn_2019_Q['Q3']!= 0 , 'Churn19Q3'] = 0

# if transx in Q1 ChurnQ1 =0 , ELSE 1
Churn_2019_Q.loc[Churn_2019_Q['Q4']== 0 , 'Churn19Q4'] = 1 
Churn_2019_Q.loc[Churn_2019_Q['Q4']!= 0 , 'Churn19Q4'] = 0


Churn_2019_Q = Churn_2019_Q[['user_id','Churn19Q1','Churn19Q2','Churn19Q3','Churn19Q4']]

bizusers_df=pd.merge(bizusers_df,Churn_2019_Q,on='user_id',how='left')




# 2018 
Churn_2018 = Transx.drop(Transx[Transx['process_year'] > 2018  ].index)
Churn_2018_Q = Churn_2018[['user_id','process_quarter']]
#Churn_2019_Q1 = Churn_2019_Q1.drop(Churn_2019_Q1[Churn_2019_Q1['process_quarter'] != "Q1"  ].index)


# adding Q1 to show if transax in Q1 

Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] == 'Q1' , 'Q1'] = 1
Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] != 'Q1', 'Q1'] = 0

# adding Q2 to show if transax in Q2 

Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] == 'Q2' , 'Q2'] = 1
Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] != 'Q2', 'Q2'] = 0

# adding Q3 to show if transax in Q3

Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] == 'Q3' , 'Q3'] = 1
Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] != 'Q3', 'Q3'] = 0

# adding Q4 to show if transax in Q4 

Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] == 'Q4' , 'Q4'] = 1
Churn_2018_Q.loc[Churn_2018_Q['process_quarter'] != 'Q4', 'Q4'] = 0

# dropping column = ' process_quarter'
Churn_2018_Q = Churn_2018_Q[['user_id','Q1','Q2','Q3','Q4']]
Churn_2018_Q = Churn_2018_Q.groupby(['user_id'], as_index=False).sum()

# if transx in Q1 ChurnQ1 =0 , ELSE 1
Churn_2018_Q.loc[Churn_2018_Q['Q1']== 0 , 'Churn18Q1'] = 1 
Churn_2018_Q.loc[Churn_2018_Q['Q1']!= 0 , 'Churn18Q1'] = 0

# if transx in Q2 ChurnQ1 =0 , ELSE 1
Churn_2018_Q.loc[Churn_2018_Q['Q2']== 0 , 'Churn18Q2'] = 1 
Churn_2018_Q.loc[Churn_2018_Q['Q2']!= 0 , 'Churn18Q2'] = 0

# if transx in Q1 ChurnQ1 =0 , ELSE 1
Churn_2018_Q.loc[Churn_2018_Q['Q3']== 0 , 'Churn18Q3'] = 1 
Churn_2018_Q.loc[Churn_2018_Q['Q3']!= 0 , 'Churn18Q3'] = 0

# if transx in Q1 ChurnQ1 =0 , ELSE 1
Churn_2018_Q.loc[Churn_2018_Q['Q4']== 0 , 'Churn18Q4'] = 1 
Churn_2018_Q.loc[Churn_2018_Q['Q4']!= 0 , 'Churn18Q4'] = 0


Churn_2018_Q = Churn_2018_Q[['user_id','Churn18Q1','Churn18Q2','Churn18Q3','Churn18Q4']]

bizusers_df=pd.merge(bizusers_df,Churn_2018_Q,on='user_id',how='left')


biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month

currentYear = datetime.now().year
currentMonth = datetime.now().month

biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] != currentYear ].index)
# adding monthly count of orders corresponding to each user. 

order_M1 = biztransx_df[['user_id','is_business','process_month']]
order_M1 = order_M1.drop(order_M1[order_M1['process_month'] != (currentMonth )  ].index)
order_M1=order_M1[['user_id','is_business']]
order_M1.rename(columns = {"is_business": "Order_19M1"}, inplace = True) 
order_19M1 = order_M1.groupby(['user_id'], as_index=False).count()


order_M2 = biztransx_df[['user_id','is_business','process_month']]
order_M2 = order_M2.drop(order_M2[order_M2['process_month'] != (currentMonth - 1)  ].index)
order_M2=order_M2[['user_id','is_business']]
order_M2.rename(columns = {"is_business": "Order_19M2"}, inplace = True) 
order_19M2 = order_M2.groupby(['user_id'], as_index=False).count()

order_M3 = biztransx_df[['user_id','is_business','process_month']]
order_M3 = order_M3.drop(order_M3[order_M3['process_month'] != (currentMonth - 2)  ].index)
order_M3 = order_M3[['user_id','is_business']]
order_M3.rename(columns = {"is_business": "Order_19M3"}, inplace = True) 
order_19M3 = order_M3.groupby(['user_id'], as_index=False).count()


order_M4 = biztransx_df[['user_id','is_business','process_month']]
order_M4 = order_M4.drop(order_M4[order_M4['process_month'] != (currentMonth - 3)  ].index)
order_M4 = order_M4[['user_id','is_business']]
order_M4.rename(columns = {"is_business": "Order_19M4"}, inplace = True) 
order_19M4 = order_M4.groupby(['user_id'], as_index=False).count()


order_M5 = biztransx_df[['user_id','is_business','process_month']]
order_M5 = order_M5.drop(order_M5[order_M5['process_month'] != (currentMonth - 4)  ].index)
order_M5 = order_M5[['user_id','is_business']]
order_M5.rename(columns = {"is_business": "Order_19M5"}, inplace = True)
order_19M5 = order_M5.groupby(['user_id'], as_index=False).count()



order_M6 = biztransx_df[['user_id','is_business','process_month']]
order_M6 = order_M6.drop(order_M6[order_M6['process_month'] != (currentMonth - 5)  ].index)
order_M6 = order_M6[['user_id','is_business']]
order_M6.rename(columns = {"is_business": "Order_19M6"}, inplace = True) 
order_19M6 = order_M6.groupby(['user_id'], as_index=False).count()


order_M7 = biztransx_df[['user_id','is_business','process_month']]
order_M7 = order_M7.drop(order_M7[order_M7['process_month'] != (currentMonth - 6)  ].index)
order_M7 = order_M7[['user_id','is_business']]
order_M7.rename(columns = {"is_business": "Order_19M7"}, inplace = True) 
order_19M7 = order_M7.groupby(['user_id'], as_index=False).count()



order_M8 = biztransx_df[['user_id','is_business','process_month']]
order_M8 = order_M8.drop(order_M8[order_M8['process_month'] != (currentMonth - 7)  ].index)
order_M8 = order_M8[['user_id','is_business']]
order_M8.rename(columns = {"is_business": "Order_19M8"}, inplace = True) 
order_19M8 = order_M8.groupby(['user_id'], as_index=False).count()


order_M9 = biztransx_df[['user_id','is_business','process_month']]
order_M9 = order_M9.drop(order_M9[order_M9['process_month'] != (currentMonth - 8)  ].index)
order_M9 = order_M9[['user_id','is_business']]
order_M9.rename(columns = {"is_business": "Order_19M9"}, inplace = True) 
order_19M9 = order_M9.groupby(['user_id'], as_index=False).count()


order_M10 = biztransx_df[['user_id','is_business','process_month']]
order_M10 = order_M10.drop(order_M10[order_M10['process_month'] != (currentMonth - 9)  ].index)
order_M10 = order_M10[['user_id','is_business']]
order_M10.rename(columns = {"is_business": "Order_19M10"}, inplace = True) 
order_19M10 = order_M10.groupby(['user_id'], as_index=False).count()



order_M11 = biztransx_df[['user_id','is_business','process_month']]
order_M11 = order_M11.drop(order_M11[order_M11['process_month'] != (currentMonth - 10)  ].index)
order_M11 = order_M11[['user_id','is_business']]
order_M11.rename(columns = {"is_business": "Order_19M11"}, inplace = True) 
order_19M11 = order_M11.groupby(['user_id'], as_index=False).count()


order_M12 = biztransx_df[['user_id','is_business','process_month']]
order_M12 = order_M12.drop(order_M12[order_M12['process_month'] != (currentMonth - 11)  ].index)
order_M12 = order_M12[['user_id','is_business']]
order_M12.rename(columns = {"is_business": "Order_19M12"}, inplace = True) 
order_19M12 = order_M12.groupby(['user_id'], as_index=False).count()




bizusers_df=pd.merge(bizusers_df,order_19M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M7,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M8,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M9,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M10,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M11,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_19M12,on='user_id',how='left')




biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')
biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month
biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] != currentYear-1 ].index)

# adding monthly count of orders corresponding to each user. 

order_M1 = biztransx_df[['user_id','is_business','process_month']]
order_M1 = order_M1.drop(order_M1[order_M1['process_month'] != (currentMonth )  ].index)
order_M1=order_M1[['user_id','is_business']]
order_M1.rename( columns = {"is_business": "Order_18M1"}, inplace = True) 
order_18M1 = order_M1.groupby(['user_id'], as_index=False).count()


order_M2 = biztransx_df[['user_id','is_business','process_month']]
order_M2 = order_M2.drop(order_M2[order_M2['process_month'] != (currentMonth - 1)  ].index)
order_M2=order_M2[['user_id','is_business']]
order_M2.rename(columns = {"is_business": "Order_18M2"}, inplace = True) 
order_18M2 = order_M2.groupby(['user_id'], as_index=False).count()

order_M3 = biztransx_df[['user_id','is_business','process_month']]
order_M3 = order_M3.drop(order_M3[order_M3['process_month'] != (currentMonth - 2)  ].index)
order_M3 = order_M3[['user_id','is_business']]
order_M3.rename(columns = {"is_business": "Order_18M3"}, inplace = True) 
order_18M3 = order_M3.groupby(['user_id'], as_index=False).count()


order_M4 = biztransx_df[['user_id','is_business','process_month']]
order_M4 = order_M4.drop(order_M4[order_M4['process_month'] != (currentMonth - 3)  ].index)
order_M4 = order_M4[['user_id','is_business']]
order_M4.rename(columns = {"is_business": "Order_18M4"}, inplace = True) 
order_18M4 = order_M4.groupby(['user_id'], as_index=False).count()


order_M5 = biztransx_df[['user_id','is_business','process_month']]
order_M5 = order_M5.drop(order_M5[order_M5['process_month'] != (currentMonth - 4)  ].index)
order_M5 = order_M5[['user_id','is_business']]
order_M5.rename(columns = {"is_business": "Order_18M5"}, inplace = True) 
order_18M5 = order_M5.groupby(['user_id'], as_index=False).count()



order_M6 = biztransx_df[['user_id','is_business','process_month']]
order_M6 = order_M6.drop(order_M6[order_M6['process_month'] != (currentMonth - 5)  ].index)
order_M6 = order_M6[['user_id','is_business']]
order_M6.rename(columns = {"is_business": "Order_18M6"}, inplace = True) 
order_18M6 = order_M6.groupby(['user_id'], as_index=False).count()


order_M7 = biztransx_df[['user_id','is_business','process_month']]
order_M7 = order_M7.drop(order_M7[order_M7['process_month'] != (currentMonth - 6)  ].index)
order_M7 = order_M7[['user_id','is_business']]
order_M7.rename(columns = {"is_business": "Order_18M7"}, inplace = True) 
order_18M7 = order_M7.groupby(['user_id'], as_index=False).count()



order_M8 = biztransx_df[['user_id','is_business','process_month']]
order_M8 = order_M8.drop(order_M8[order_M8['process_month'] != (currentMonth - 7)  ].index)
order_M8 = order_M8[['user_id','is_business']]
order_M8.rename(columns = {"is_business": "Order_18M8"}, inplace = True) 
order_18M8 = order_M8.groupby(['user_id'], as_index=False).count()


order_M9 = biztransx_df[['user_id','is_business','process_month']]
order_M9 = order_M9.drop(order_M9[order_M9['process_month'] != (currentMonth - 8)  ].index)
order_M9 = order_M9[['user_id','is_business']]
order_M9.rename(columns = {"is_business": "Order_18M9"}, inplace = True) 
order_18M9 = order_M9.groupby(['user_id'], as_index=False).count()


order_M10 = biztransx_df[['user_id','is_business','process_month']]
order_M10 = order_M10.drop(order_M10[order_M10['process_month'] != (currentMonth - 9)  ].index)
order_M10 = order_M10[['user_id','is_business']]
order_M10.rename(columns = {"is_business": "Order_18M10"}, inplace = True) 
order_18M10 = order_M10.groupby(['user_id'], as_index=False).count()



order_M11 = biztransx_df[['user_id','is_business','process_month']]
order_M11 = order_M11.drop(order_M11[order_M11['process_month'] != (currentMonth - 10)  ].index)
order_M11 = order_M11[['user_id','is_business']]
order_M11.rename(columns = {"is_business": "Order_18M11"}, inplace = True) 
order_18M11 = order_M11.groupby(['user_id'], as_index=False).count()


order_M12 = biztransx_df[['user_id','is_business','process_month']]
order_M12 = order_M12.drop(order_M12[order_M12['process_month'] != (currentMonth - 11)  ].index)
order_M12 = order_M12[['user_id','is_business']]
order_M12.rename(columns = {"is_business": "Order_18M12"}, inplace = True) 
order_18M12 = order_M12.groupby(['user_id'], as_index=False).count()




bizusers_df=pd.merge(bizusers_df,order_18M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M7,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M8,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M9,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M10,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M11,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,order_18M12,on='user_id',how='left')




# volume every month 



biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')

biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month

biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] != 2019 ].index)

volume_M1 = biztransx_df[['user_id','amount','process_month']]
volume_M1 = volume_M1.drop(volume_M1[volume_M1['process_month'] != (currentMonth )  ].index)
volume_M1 = volume_M1[['user_id','amount']]
volume_M1.rename(columns = {"amount": "Volume_19M1"}, inplace = True) 
volume_19M1 = volume_M1.groupby(['user_id'], as_index=False).sum()

volume_M2 = biztransx_df[['user_id','amount','process_month']]
volume_M2 = volume_M2.drop(volume_M2[volume_M2['process_month'] != (currentMonth - 1)  ].index)
volume_M2 = volume_M2[['user_id','amount']]
volume_M2.rename(columns = {"amount": "Volume_19M2"}, inplace = True) 
volume_19M2 = volume_M2.groupby(['user_id'], as_index=False).sum()

volume_M3 = biztransx_df[['user_id','amount','process_month']]
volume_M3 = volume_M3.drop(volume_M3[volume_M3['process_month'] != (currentMonth - 2)  ].index)
volume_M3 = volume_M3[['user_id','amount']]
volume_M3.rename(columns = {"amount": "Volume_19M3"}, inplace = True) 
volume_19M3 = volume_M3.groupby(['user_id'], as_index=False).sum()


volume_M4 = biztransx_df[['user_id','amount','process_month']]
volume_M4 = volume_M4.drop(volume_M4[volume_M4['process_month'] != (currentMonth - 3)  ].index)
volume_M4 = volume_M4[['user_id','amount']]
volume_M4.rename(columns = {"amount": "Volume_19M4"}, inplace = True)
volume_19M4 = volume_M4.groupby(['user_id'], as_index=False).sum()


volume_M5 = biztransx_df[['user_id','amount','process_month']]
volume_M5 = volume_M5.drop(volume_M5[volume_M5['process_month'] != (currentMonth - 4)  ].index)
volume_M5 = volume_M5[['user_id','amount']]
volume_M5.rename(columns = {"amount": "Volume_19M5"}, inplace = True)
volume_19M5 = volume_M5.groupby(['user_id'], as_index=False).sum()



volume_M6 = biztransx_df[['user_id','amount','process_month']]
volume_M6 = volume_M6.drop(volume_M6[volume_M6['process_month'] != (currentMonth - 5)  ].index)
volume_M6 = volume_M6[['user_id','amount']]
volume_M6.rename(columns = {"amount": "Volume_19M6"}, inplace = True)
volume_19M6 = volume_M6.groupby(['user_id'], as_index=False).sum()


volume_M7 = biztransx_df[['user_id','amount','process_month']]
volume_M7 = volume_M7.drop(volume_M7[volume_M7['process_month'] != (currentMonth - 6)  ].index)
volume_M7 = volume_M7[['user_id','amount']]
volume_M7.rename(columns = {"amount": "Volume_19M7"}, inplace = True)
volume_19M7 = volume_M7.groupby(['user_id'], as_index=False).sum()


volume_M8 = biztransx_df[['user_id','amount','process_month']]
volume_M8 = volume_M8.drop(volume_M8[volume_M8['process_month'] != (currentMonth - 7)  ].index)
volume_M8 = volume_M8[['user_id','amount']]
volume_M8.rename(columns = {"amount": "Volume_19M8"}, inplace = True)
volume_19M8 = volume_M8.groupby(['user_id'], as_index=False).sum()

volume_M9 = biztransx_df[['user_id','amount','process_month']]
volume_M9 = volume_M9.drop(volume_M9[volume_M9['process_month'] != (currentMonth - 8)  ].index)
volume_M9 = volume_M9[['user_id','amount']]
volume_M9.rename(columns = {"amount": "Volume_19M9"}, inplace = True)
volume_19M9 = volume_M9.groupby(['user_id'], as_index=False).sum()


volume_M10 = biztransx_df[['user_id','amount','process_month']]
volume_M10 = volume_M10.drop(volume_M10[volume_M10['process_month'] != (currentMonth - 9)  ].index)
volume_M10 = volume_M10[['user_id','amount']]
volume_M10.rename(columns = {"amount": "Volume_19M10"}, inplace = True)
volume_19M10 = volume_M10.groupby(['user_id'], as_index=False).sum()


volume_M11 = biztransx_df[['user_id','amount','process_month']]
volume_M11 = volume_M11.drop(volume_M11[volume_M11['process_month'] != (currentMonth - 10)  ].index)
volume_M11 = volume_M11[['user_id','amount']]
volume_M11.rename(columns = {"amount": "Volume_19M11"}, inplace = True)
volume_19M11 = volume_M11.groupby(['user_id'], as_index=False).sum()



volume_M12 = biztransx_df[['user_id','amount','process_month']]
volume_M12 = volume_M12.drop(volume_M12[volume_M12['process_month'] != (currentMonth - 11)  ].index)
volume_M12 = volume_M12[['user_id','amount']]
volume_M12.rename(columns = {"amount": "Volume_19M12"}, inplace = True)
volume_19M12 = volume_M12.groupby(['user_id'], as_index=False).sum()


bizusers_df=pd.merge(bizusers_df,volume_19M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M7,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M8,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M9,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M10,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M11,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_19M12,on='user_id',how='left')



# Volume for 2018 each month 

biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')

biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month

biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] != 2018 ].index)

volume_M1 = biztransx_df[['user_id','amount','process_month']]
volume_M1 = volume_M1.drop(volume_M1[volume_M1['process_month'] != (currentMonth )  ].index)
volume_M1 = volume_M1[['user_id','amount']]
volume_M1.rename(columns = {"amount": "Volume_18M1"}, inplace = True)
volume_18M1 = volume_M1.groupby(['user_id'], as_index=False).sum()

volume_M2 = biztransx_df[['user_id','amount','process_month']]
volume_M2 = volume_M2.drop(volume_M2[volume_M2['process_month'] != (currentMonth - 1)  ].index)
volume_M2 = volume_M2[['user_id','amount']]
volume_M2.rename(columns = {"amount": "Volume_18M2"}, inplace = True)
volume_18M2 = volume_M2.groupby(['user_id'], as_index=False).sum()

volume_M3 = biztransx_df[['user_id','amount','process_month']]
volume_M3 = volume_M3.drop(volume_M3[volume_M3['process_month'] != (currentMonth - 2)  ].index)
volume_M3 = volume_M3[['user_id','amount']]
volume_M3.rename(columns = {"amount": "Volume_18M3"}, inplace = True)
volume_18M3 = volume_M3.groupby(['user_id'], as_index=False).sum()


volume_M4 = biztransx_df[['user_id','amount','process_month']]
volume_M4 = volume_M4.drop(volume_M4[volume_M4['process_month'] != (currentMonth - 3)  ].index)
volume_M4 = volume_M4[['user_id','amount']]
volume_M4.rename(columns = {"amount": "Volume_18M4"}, inplace = True)
volume_18M4 = volume_M4.groupby(['user_id'], as_index=False).sum()


volume_M5 = biztransx_df[['user_id','amount','process_month']]
volume_M5 = volume_M5.drop(volume_M5[volume_M5['process_month'] != (currentMonth - 4)  ].index)
volume_M5 = volume_M5[['user_id','amount']]
volume_M5.rename(columns = {"amount": "Volume_18M5"}, inplace = True)
volume_18M5 = volume_M5.groupby(['user_id'], as_index=False).sum()



volume_M6 = biztransx_df[['user_id','amount','process_month']]
volume_M6 = volume_M6.drop(volume_M6[volume_M6['process_month'] != (currentMonth - 5)  ].index)
volume_M6 = volume_M6[['user_id','amount']]
volume_M6.rename(columns = {"amount": "Volume_18M6"}, inplace = True)
volume_18M6 = volume_M6.groupby(['user_id'], as_index=False).sum()


volume_M7 = biztransx_df[['user_id','amount','process_month']]
volume_M7 = volume_M7.drop(volume_M7[volume_M7['process_month'] != (currentMonth - 6)  ].index)
volume_M7 = volume_M7[['user_id','amount']]
volume_M7.rename(columns = {"amount": "Volume_18M7"}, inplace = True)
volume_18M7 = volume_M7.groupby(['user_id'], as_index=False).sum()


volume_M8 = biztransx_df[['user_id','amount','process_month']]
volume_M8 = volume_M8.drop(volume_M8[volume_M8['process_month'] != (currentMonth - 7)  ].index)
volume_M8 = volume_M8[['user_id','amount']]
volume_M8.rename(columns = {"amount": "Volume_18M8"}, inplace = True)
volume_18M8 = volume_M8.groupby(['user_id'], as_index=False).sum()

volume_M9 = biztransx_df[['user_id','amount','process_month']]
volume_M9 = volume_M9.drop(volume_M9[volume_M9['process_month'] != (currentMonth - 8)  ].index)
volume_M9 = volume_M9[['user_id','amount']]
volume_M9.rename(columns = {"amount": "Volume_18M9"}, inplace = True)
volume_18M9 = volume_M9.groupby(['user_id'], as_index=False).sum()


volume_M10 = biztransx_df[['user_id','amount','process_month']]
volume_M10 = volume_M10.drop(volume_M10[volume_M10['process_month'] != (currentMonth - 9)  ].index)
volume_M10 = volume_M10[['user_id','amount']]
volume_M10.rename(columns = {"amount": "Volume_18M10"}, inplace = True)
volume_18M10 = volume_M10.groupby(['user_id'], as_index=False).sum()


volume_M11 = biztransx_df[['user_id','amount','process_month']]
volume_M11 = volume_M11.drop(volume_M11[volume_M11['process_month'] != (currentMonth - 10)  ].index)
volume_M11 = volume_M11[['user_id','amount']]
volume_M11.rename(columns = {"amount": "Volume_18M11"}, inplace = True)
volume_18M11 = volume_M11.groupby(['user_id'], as_index=False).sum()



volume_M12 = biztransx_df[['user_id','amount','process_month']]
volume_M12 = volume_M12.drop(volume_M12[volume_M12['process_month'] != (currentMonth - 11)  ].index)
volume_M12 = volume_M12[['user_id','amount']]
volume_M12.rename(columns = {"amount": "Volume_18M12"}, inplace = True)
volume_18M12 = volume_M12.groupby(['user_id'], as_index=False).sum()



bizusers_df=pd.merge(bizusers_df,volume_18M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M7,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M8,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M9,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M10,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M11,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,volume_18M12,on='user_id',how='left')




##########
# adding type of currecny used each month for the past 2 years 

# add 6 column for total type of currency in each month
biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')

biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month

biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] != 2019 ].index)

currency_M1 = biztransx_df[['user_id','target_currency','process_month']]
currency_M1 = currency_M1.drop(currency_M1[currency_M1['process_month'] != (currentMonth )  ].index)
currency_M1 = currency_M1[['user_id','target_currency']]
currency_M1 = currency_M1.groupby('user_id',as_index=True).target_currency.nunique()
currency_M1.rename(columns = {"target_currency": "Currency_19M1"}, inplace = True)
currency_19M1=currency_M1.reset_index(drop=False)

currency_M2 = biztransx_df[['user_id','target_currency','process_month']]
currency_M2 = currency_M2.drop(currency_M2[currency_M2['process_month'] != (currentMonth - 1)  ].index)
currency_M2 = currency_M2[['user_id','target_currency']]
currency_M2=currency_M2.groupby('user_id',as_index=True).target_currency.nunique()
currency_M2.rename(columns = {"target_currency": "currency_19M2"}, inplace = True)
currency_19M2=currency_M2.reset_index(drop=False)

currency_M3 = biztransx_df[['user_id','target_currency','process_month']]
currency_M3 = currency_M3.drop(currency_M3[currency_M3['process_month'] != (currentMonth - 2)  ].index)
currency_M3 = currency_M3[['user_id','target_currency']]
currency_M3=currency_M3.groupby('user_id',as_index=True).target_currency.nunique()
currency_M3.rename(columns = {"target_currency": "currency_19M3"}, inplace = True)
currency_19M3=currency_M3.reset_index(drop=False)

currency_M4 = biztransx_df[['user_id','target_currency','process_month']]
currency_M4 = currency_M4.drop(currency_M4[currency_M4['process_month'] != (currentMonth - 3)  ].index)
currency_M4 = currency_M4[['user_id','target_currency']]
currency_M4=currency_M4.groupby('user_id',as_index=True).target_currency.nunique()
currency_M4.rename(columns = {"target_currency": "currency_19M4"}, inplace = True)
currency_19M4=currency_M4.reset_index(drop=False)

currency_M5 = biztransx_df[['user_id','target_currency','process_month']]
currency_M5 = currency_M5.drop(currency_M5[currency_M5['process_month'] != (currentMonth - 4)  ].index)
currency_M5 = currency_M5[['user_id','target_currency']]
currency_M5=currency_M5.groupby('user_id',as_index=True).target_currency.nunique()
currency_M5.rename(columns = {"target_currency": "currency_19M5"}, inplace = True)
currency_19M5=currency_M5.reset_index(drop=False)

currency_M6 = biztransx_df[['user_id','target_currency','process_month']]
currency_M6 = currency_M6.drop(currency_M6[currency_M6['process_month'] != (currentMonth - 5)  ].index)
currency_M6 = currency_M6[['user_id','target_currency']]
currency_M6=currency_M6.groupby('user_id',as_index=True).target_currency.nunique()
currency_M6.rename(columns = {"target_currency": "currency_19M6"}, inplace = True)
currency_19M6=currency_M6.reset_index(drop=False)


currency_M7 = biztransx_df[['user_id','target_currency','process_month']]
currency_M7 = currency_M7.drop(currency_M7[currency_M7['process_month'] != (currentMonth - 6 )  ].index)
currency_M7 = currency_M7[['user_id','target_currency']]
currency_M7 = currency_M7.groupby('user_id',as_index=True).target_currency.nunique()
currency_M7.rename(columns = {"target_currency": "currency_19M7"}, inplace = True)
currency_19M7=currency_M7.reset_index(drop=False)

currency_M8 = biztransx_df[['user_id','target_currency','process_month']]
currency_M8 = currency_M8.drop(currency_M8[currency_M8['process_month'] != (currentMonth - 7)  ].index)
currency_M8 = currency_M8[['user_id','target_currency']]
currency_M8=currency_M8.groupby('user_id',as_index=True).target_currency.nunique()
currency_M8.rename(columns = {"target_currency": "currency_19M8"}, inplace = True)
currency_19M8=currency_M8.reset_index(drop=False)

currency_M9 = biztransx_df[['user_id','target_currency','process_month']]
currency_M9 = currency_M9.drop(currency_M9[currency_M9['process_month'] != (currentMonth - 8)  ].index)
currency_M9 = currency_M9[['user_id','target_currency']]
currency_M9=currency_M9.groupby('user_id',as_index=True).target_currency.nunique()
currency_M9.rename(columns = {"target_currency": "currency_19M9"}, inplace = True)
currency_19M9=currency_M9.reset_index(drop=False)

currency_M10 = biztransx_df[['user_id','target_currency','process_month']]
currency_M10 = currency_M10.drop(currency_M10[currency_M10['process_month'] != (currentMonth - 9)  ].index)
currency_M10 = currency_M10[['user_id','target_currency']]
currency_M10 =currency_M10.groupby('user_id',as_index=True).target_currency.nunique()
currency_M10.rename(columns = {"target_currency": "currency_19M10"}, inplace = True)
currency_19M10=currency_M10.reset_index(drop=False)

currency_M11 = biztransx_df[['user_id','target_currency','process_month']]
currency_M11 = currency_M11.drop(currency_M11[currency_M11['process_month'] != (currentMonth - 10)  ].index)
currency_M11 = currency_M11[['user_id','target_currency']]
currency_M11=currency_M11.groupby('user_id',as_index=True).target_currency.nunique()
currency_M11.rename(columns = {"target_currency": "currency_19M11"}, inplace = True)
currency_19M11=currency_M11.reset_index(drop=False)

currency_M12 = biztransx_df[['user_id','target_currency','process_month']]
currency_M12 = currency_M12.drop(currency_M12[currency_M12['process_month'] != (currentMonth - 11)  ].index)
currency_M12 = currency_M12[['user_id','target_currency']]
currency_M12=currency_M12.groupby('user_id',as_index=True).target_currency.nunique()
currency_M12.rename(columns = {"target_currency": "currency_M12"}, inplace = True)
currency_19M12=currency_M12.reset_index(drop=False)




bizusers_df=pd.merge(bizusers_df,currency_19M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M7,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M8,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M9,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M10,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M11,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_19M12,on='user_id',how='left')



## currency count for each month for 2018
biztransx_df = pd.read_csv('biztransx_df.csv', encoding='unicode_escape')

biztransx_df['process_datetime'] = pd.to_datetime(biztransx_df.process_datetime)
biztransx_df['process_month']= biztransx_df.process_datetime.dt.month

biztransx_df = biztransx_df.drop(biztransx_df[biztransx_df['process_year'] != 2018 ].index)

currency_M1 = biztransx_df[['user_id','target_currency','process_month']]
currency_M1 = currency_M1.drop(currency_M1[currency_M1['process_month'] != (currentMonth )  ].index)
currency_M1 = currency_M1[['user_id','target_currency']]
currency_M1 = currency_M1.groupby('user_id',as_index=True).target_currency.nunique()
currency_M1.rename(columns = {"target_currency": "currency_18M1"}, inplace = True)
currency_18M1=currency_M1.reset_index(drop=False)

currency_M2 = biztransx_df[['user_id','target_currency','process_month']]
currency_M2 = currency_M2.drop(currency_M2[currency_M2['process_month'] != (currentMonth - 1)  ].index)
currency_M2 = currency_M2[['user_id','target_currency']]
currency_M2=currency_M2.groupby('user_id',as_index=True).target_currency.nunique()
currency_M2.rename(columns = {"target_currency": "currency_18M2"}, inplace = True)
currency_18M2=currency_M2.reset_index(drop=False)

currency_M3 = biztransx_df[['user_id','target_currency','process_month']]
currency_M3 = currency_M3.drop(currency_M3[currency_M3['process_month'] != (currentMonth - 2)  ].index)
currency_M3 = currency_M3[['user_id','target_currency']]
currency_M3=currency_M3.groupby('user_id',as_index=True).target_currency.nunique()
currency_M3.rename(columns = {"target_currency": "currency_18M3"}, inplace = True)
currency_18M3=currency_M3.reset_index(drop=False)

currency_M4 = biztransx_df[['user_id','target_currency','process_month']]
currency_M4 = currency_M4.drop(currency_M4[currency_M4['process_month'] != (currentMonth - 3)  ].index)
currency_M4 = currency_M4[['user_id','target_currency']]
currency_M4=currency_M4.groupby('user_id',as_index=True).target_currency.nunique()
currency_M4.rename(columns = {"target_currency": "currency_18M4"}, inplace = True)
currency_18M4=currency_M4.reset_index(drop=False)

currency_M5 = biztransx_df[['user_id','target_currency','process_month']]
currency_M5 = currency_M5.drop(currency_M5[currency_M5['process_month'] != (currentMonth - 4)  ].index)
currency_M5 = currency_M5[['user_id','target_currency']]
currency_M5=currency_M5.groupby('user_id',as_index=True).target_currency.nunique()
currency_M5.rename(columns = {"target_currency": "currency_18M5"}, inplace = True)
currency_18M5=currency_M5.reset_index(drop=False)

currency_M6 = biztransx_df[['user_id','target_currency','process_month']]
currency_M6 = currency_M6.drop(currency_M6[currency_M6['process_month'] != (currentMonth - 5)  ].index)
currency_M6 = currency_M6[['user_id','target_currency']]
currency_M6=currency_M6.groupby('user_id',as_index=True).target_currency.nunique()
currency_M6.rename(columns = {"target_currency": "currency_18M6"}, inplace = True)
currency_18M6=currency_M6.reset_index(drop=False)


currency_M7 = biztransx_df[['user_id','target_currency','process_month']]
currency_M7 = currency_M7.drop(currency_M7[currency_M7['process_month'] != (currentMonth - 6 )  ].index)
currency_M7 = currency_M7[['user_id','target_currency']]
currency_M7 = currency_M7.groupby('user_id',as_index=True).target_currency.nunique()
currency_M7.rename(columns = {"target_currency": "currency_18M7"}, inplace = True)
currency_18M7=currency_M7.reset_index(drop=False)

currency_M8 = biztransx_df[['user_id','target_currency','process_month']]
currency_M8 = currency_M8.drop(currency_M8[currency_M8['process_month'] != (currentMonth - 7)  ].index)
currency_M8 = currency_M8[['user_id','target_currency']]
currency_M8=currency_M8.groupby('user_id',as_index=True).target_currency.nunique()
currency_M8.rename(columns = {"target_currency": "currency_18M8"}, inplace = True)
currency_18M8=currency_M8.reset_index(drop=False)

currency_M9 = biztransx_df[['user_id','target_currency','process_month']]
currency_M9 = currency_M9.drop(currency_M9[currency_M9['process_month'] != (currentMonth - 8)  ].index)
currency_M9 = currency_M9[['user_id','target_currency']]
currency_M9=currency_M9.groupby('user_id',as_index=True).target_currency.nunique()
currency_M9.rename(columns = {"target_currency": "currency_18M9"}, inplace = True)
currency_18M9=currency_M9.reset_index(drop=False)

currency_M10 = biztransx_df[['user_id','target_currency','process_month']]
currency_M10 = currency_M10.drop(currency_M10[currency_M10['process_month'] != (currentMonth - 9)  ].index)
currency_M10 = currency_M10[['user_id','target_currency']]
currency_M10 =currency_M10.groupby('user_id',as_index=True).target_currency.nunique()
currency_M10.rename(columns = {"target_currency": "currency_18M10"}, inplace = True)
currency_18M10=currency_M4.reset_index(drop=False)

currency_M11 = biztransx_df[['user_id','target_currency','process_month']]
currency_M11 = currency_M11.drop(currency_M11[currency_M11['process_month'] != (currentMonth - 10)  ].index)
currency_M11 = currency_M11[['user_id','target_currency']]
currency_M11=currency_M11.groupby('user_id',as_index=True).target_currency.nunique()
currency_M11.rename(columns = {"target_currency": "currency_18M11"}, inplace = True)
currency_18M11=currency_M11.reset_index(drop=False)


currency_M12 = biztransx_df[['user_id','target_currency','process_month']]
currency_M12 = currency_M12.drop(currency_M12[currency_M12['process_month'] != (currentMonth - 11)  ].index)
currency_M12 = currency_M12[['user_id','target_currency']]
currency_M12=currency_M12.groupby('user_id',as_index=True).target_currency.nunique()
currency_M12.rename(columns = {"target_currency": "currency_18M12"}, inplace = True)
currency_18M12=currency_M12.reset_index(drop=False)




bizusers_df=pd.merge(bizusers_df,currency_18M1,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M2,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M3,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M4,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M5,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M6,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M7,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M8,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M9,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M10,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M11,on='user_id',how='left')
bizusers_df=pd.merge(bizusers_df,currency_18M12,on='user_id',how='left')


bizusers_df.to_csv('BusinessAnalysisComplete.csv')


