#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:53:22 2019

@author: smrititiwari
"""


# making file 1 
# 19Q3 :
# 19M1,19M2,19M3,19M4,19M5
# for currency , for volume , for number of order  


import pandas as pd
import numpy as np
import math
import os
from datetime import datetime



bizChurnFile = pd.read_csv('BusinessAnalysisComplete.csv', encoding='unicode_escape')


# TOTAL FILES 5  
df1 = pd.DataFrame() 
df2 = pd.DataFrame() 
df3 = pd.DataFrame() 
df4 = pd.DataFrame() 
df5 = pd.DataFrame() 


df1['user_id'] = bizChurnFile['user_id'] 
df2['user_id'] = bizChurnFile['user_id'] 
df3['user_id'] = bizChurnFile['user_id'] 
df4['user_id'] = bizChurnFile['user_id'] 
df5['user_id'] = bizChurnFile['user_id'] 


currentYear = 2019
currentMonth = 2

if currentYear == 2019 :
    if currentMonth <= 3 :
        Quarter = "Q1"
        df1['Churn19Q1'] = bizChurnFile['Churn19Q1']
    elif currentMonth <=6 :
        df2['Churn19Q2'] = bizChurnFile['Churn19Q2']
        Quarter = "Q2"
    elif currentMonth <= 9 :
        df3['Churn19Q3'] = bizChurnFile['Churn19Q3']
        Quarter = "Q3"
    else :
        Quarter = "Q4"
if currentYear == 2018 :
    if currentMonth <= 3 :
        Quarter = "Q1"
    elif currentMonth <=6 :
        Quarter = "Q2"
    elif currentMonth <= 9 :
        
        df4['Churn18Q3'] = bizChurnFile['Churn18Q3']
        Quarter = "Q3"
    else :
        
        df5['Churn18Q4'] = bizChurnFile['Churn18Q4']
        Quarter = "Q4"


if Quarter == "Q1" :
    if currentYear == 2019 :
              # ADDING ORDERS OF PREV SIX MONTHS FROM THE QUARTER 
        df1['Order_18M7'] = bizChurnFile['Order_18M7']
        df1['Order_18M8'] = bizChurnFile['Order_18M8']
        df1['Order_18M9'] = bizChurnFile['Order_18M9']
        df1['Order_18M10'] = bizChurnFile['Order_18M10']
        df1['Order_18M11'] = bizChurnFile['Order_18M11']
        df1['Order_18M12'] = bizChurnFile['Order_18M12']
       
        
    
        df1['Order_18M7'].fillna(0,inplace=True)
        df1['Order_18M8'].fillna(0,inplace=True)
        df1['Order_18M9'].fillna(0,inplace=True)
        df1['Order_18M10'].fillna(0,inplace=True)
        df1['Order_18M11'].fillna(0,inplace=True)
        df1['Order_18M12'].fillna(0,inplace=True)
        
        
        
        df1["diffOM1_2"] = df1['Order_18M12'] - df1['Order_18M11']    
        df1["diffOM2_3"] = df1['Order_18M11'] - df1['Order_18M10']
        df1["diffOM3_4"] = df1['Order_18M10'] - df1['Order_18M9']
        df1["diffOM4_5"] = df1['Order_18M9'] - df1['Order_18M8']
        df1["diffOM5_6"] = df1['Order_18M8'] - df1['Order_18M7']
        
        
        df1.loc[df1['diffOM1_2'] == 0 ,'diffOM1_2'] = 0
        df1.loc[df1['diffOM1_2'] < 0 ,'diffOM1_2'] = -1
        df1.loc[df1['diffOM1_2'] > 0 ,'diffOM1_2'] = 1
        
  
        df1.loc[df1['diffOM2_3'] == 0 ,'diffOM2_3'] = 0
        df1.loc[df1['diffOM2_3'] < 0 ,'diffOM2_3'] = -1
        df1.loc[df1['diffOM2_3'] > 0 ,'diffOM2_3'] = 1
        
        df1.loc[df1['diffOM3_4'] == 0 ,'diffOM3_4'] = 0
        df1.loc[df1['diffOM3_4'] < 0 ,'diffOM3_4'] = -1
        df1.loc[df1['diffOM3_4'] > 0 ,'diffOM3_4'] = 1
        
        df1.loc[df1['diffOM4_5'] == 0 ,'diffOM4_5'] = 0
        df1.loc[df1['diffOM4_5'] < 0 ,'diffOM4_5'] = -1
        df1.loc[df1['diffOM4_5'] > 0 ,'diffOM4_5'] = 1
        
        df1.loc[df1['diffOM5_6'] == 0 ,'diffOM5_6'] = 0
        df1.loc[df1['diffOM5_6'] < 0 ,'diffOM5_6'] = -1
        df1.loc[df1['diffOM5_6'] > 0 ,'diffOM5_6'] = 1
         
        
        df1["OrderTag"] = df1["diffOM1_2"] + df1["diffOM2_3"]+  df1["diffOM3_4"]+ df1["diffOM4_5"]+  df1["diffOM5_6"]
        df1 = df1.drop(["diffOM1_2","diffOM2_3","diffOM3_4","diffOM4_5","diffOM5_6"],axis =1)
        df1 = df1.drop(["Order_18M7","Order_18M8","Order_18M9","Order_18M10","Order_18M11","Order_18M12"],axis =1)
        
        
        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df1['Volume_18M7'] = bizChurnFile['Volume_18M7']
        df1['Volume_18M8'] = bizChurnFile['Volume_18M8']
        df1['Volume_18M9'] = bizChurnFile['Volume_18M9']
        df1['Volume_18M10'] = bizChurnFile['Volume_18M10']
        df1['Volume_18M11'] = bizChurnFile['Volume_18M11']
        df1['Volume_18M12'] = bizChurnFile['Volume_18M12']
                
                 
        df1['Volume_18M7'].fillna(0,inplace=True)
        df1['Volume_18M8'].fillna(0,inplace=True)
        df1['Volume_18M9'].fillna(0,inplace=True)
        df1['Volume_18M10'].fillna(0,inplace=True)
        df1['Volume_18M11'].fillna(0,inplace=True)
        df1['Volume_18M12'].fillna(0,inplace=True)
        
        
        df1["diffVM1_2"] = df1['Volume_18M12'] - df1['Volume_18M11']    
        df1["diffVM2_3"] = df1['Volume_18M11'] - df1['Volume_18M10']
        df1["diffVM3_4"] = df1['Volume_18M10'] - df1['Volume_18M9']
        df1["diffVM4_5"] = df1['Volume_18M9'] - df1['Volume_18M8']
        df1["diffVM5_6"] = df1['Volume_18M8'] - df1['Volume_18M7']
        
        
        df1.loc[df1['diffVM1_2'] == 0 ,'diffVM1_2'] = 0
        df1.loc[df1['diffVM1_2'] < 0 ,'diffVM1_2'] = -1
        df1.loc[df1['diffVM1_2'] > 0 ,'diffVM1_2'] = 1
        
  
        df1.loc[df1['diffVM2_3'] == 0 ,'diffVM2_3'] = 0
        df1.loc[df1['diffVM2_3'] < 0 ,'diffVM2_3'] = -1
        df1.loc[df1['diffVM2_3'] > 0 ,'diffVM2_3'] = 1
        
        
        df1.loc[df1['diffVM3_4'] == 0 ,'diffVM3_4'] = 0
        df1.loc[df1['diffVM3_4'] < 0 ,'diffVM3_4'] = -1
        df1.loc[df1['diffVM3_4'] > 0 ,'diffVM3_4'] = 1
        
        
        df1.loc[df1['diffVM4_5'] == 0 ,'diffVM4_5'] = 0
        df1.loc[df1['diffVM4_5'] < 0 ,'diffVM4_5'] = -1
        df1.loc[df1['diffVM4_5'] > 0 ,'diffVM4_5'] = 1
        
        
        df1.loc[df1['diffVM5_6'] == 0 ,'diffVM5_6'] = 0
        df1.loc[df1['diffVM5_6'] < 0 ,'diffVM5_6'] = -1
        df1.loc[df1['diffVM5_6'] > 0 ,'diffVM5_6'] = 1
        
        
        df1["VolumeTag"] = df1["diffVM1_2"] + df1["diffVM2_3"]+  df1["diffVM3_4"]+ df1["diffVM4_5"]+  df1["diffVM5_6"]
        df1 = df1.drop(["diffVM1_2","diffVM2_3","diffVM3_4","diffVM4_5","diffVM5_6"],axis =1)
        df1 = df1.drop(["Volume_18M7","Volume_18M8","Volume_18M9","Volume_18M10","Volume_18M11","Volume_18M12"],axis =1)
        
        
        
        
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df1['currency_18M7'] = bizChurnFile['currency_18M7']
        df1['currency_18M8'] = bizChurnFile['currency_18M8']
        df1['currency_18M9'] = bizChurnFile['currency_18M9']
        df1['currency_18M10'] = bizChurnFile['currency_18M10']
        df1['currency_18M11'] = bizChurnFile['currency_18M11']
        df1['currency_18M12'] = bizChurnFile['currency_18M12']
        
        
        
        df1['currency_18M7'].fillna(0,inplace=True)
        df1['currency_18M8'].fillna(0,inplace=True)
        df1['currency_18M9'].fillna(0,inplace=True)
        df1['currency_18M10'].fillna(0,inplace=True)
        df1['currency_18M11'].fillna(0,inplace=True)
        df1['currency_18M12'].fillna(0,inplace=True)
        
        
         #Difference for currency 
        df1["diffCM1_2"] = df1['currency_18M12'] - df1['currency_18M11']    
        df1["diffCM2_3"] = df1['currency_18M11'] - df1['currency_18M10']
        df1["diffCM3_4"] = df1['currency_18M10'] - df1['currency_18M9']
        df1["diffCM4_5"] = df1['currency_18M9'] - df1['currency_18M8']
        df1["diffCM5_6"] = df1['currency_18M8'] - df1['currency_18M7']
        
        df1.loc[df1['diffCM1_2'] == 0 ,'diffCM1_2'] = 0
        df1.loc[df1['diffCM1_2'] < 0 ,'diffCM1_2'] = -1
        df1.loc[df1['diffCM1_2'] > 0 ,'diffCM1_2'] = 1
        
  
        df1.loc[df1['diffCM2_3'] == 0 ,'diffCM2_3'] = 0
        df1.loc[df1['diffCM2_3'] < 0 ,'diffCM2_3'] = -1
        df1.loc[df1['diffCM2_3'] > 0 ,'diffCM2_3'] = 1
        
        df1.loc[df1['diffCM3_4'] == 0 ,'diffCM3_4'] = 0
        df1.loc[df1['diffCM3_4'] < 0 ,'diffCM3_4'] = -1
        df1.loc[df1['diffCM3_4'] > 0 ,'diffCM3_4'] = 1
        
        df1.loc[df1['diffCM4_5'] == 0 ,'diffCM4_5'] = 0
        df1.loc[df1['diffCM4_5'] < 0 ,'diffCM4_5'] = -1
        df1.loc[df1['diffCM4_5'] > 0 ,'diffCM4_5'] = 1
        
        df1.loc[df1['diffCM5_6'] == 0 ,'diffCM5_6'] = 0
        df1.loc[df1['diffCM5_6'] < 0 ,'diffCM5_6'] = -1
        df1.loc[df1['diffCM5_6'] > 0 ,'diffCM5_6'] = 1
         
        
        df1["CurrencyTag"] = df1["diffCM1_2"] + df1["diffCM2_3"]+  df1["diffCM3_4"]+ df1["diffCM4_5"]+  df1["diffCM5_6"]
        df1 = df1.drop(["diffCM1_2","diffCM2_3","diffCM3_4","diffCM4_5","diffCM5_6"],axis =1)
        df1 = df1.drop(["currency_18M12","currency_18M11","currency_18M10","currency_18M9","currency_18M8","currency_18M7"],axis =1)
        
        
        df1.to_csv('F19Q1.csv')
        
        
        
if Quarter == "Q2" :
    if currentYear == 2019 :
              # ADDING ORDERS OF PREV SIX MONTHS FROM THE QUARTER 
        df2['Order_19M1'] = bizChurnFile['Order_19M1']
        df2['Order_19M2'] = bizChurnFile['Order_19M2']
        df2['Order_19M3'] = bizChurnFile['Order_19M3']
        df2['Order_18M10'] = bizChurnFile['Order_18M10']
        df2['Order_18M11'] = bizChurnFile['Order_18M11']
        df2['Order_18M12'] = bizChurnFile['Order_18M12']
       
        df2['Order_18M10'].fillna(0,inplace=True)
        df2['Order_18M11'].fillna(0,inplace=True)
        df2['Order_18M12'].fillna(0,inplace=True)
        df2['Order_19M3'].fillna(0,inplace=True)
        df2['Order_19M2'].fillna(0,inplace=True)
        df2['Order_19M1'].fillna(0,inplace=True)
        
        #Difference for orders 
        df2["diffOM1_2"] = df2['Order_19M3'] - df2['Order_19M2']    
        df2["diffOM2_3"] = df2['Order_19M2'] - df2['Order_19M1']
        df2["diffOM3_4"] = df2['Order_19M1'] - df2['Order_18M12']
        df2["diffOM4_5"] = df2['Order_18M12'] - df2['Order_18M11']
        df2["diffOM5_6"] = df2['Order_18M11'] - df2['Order_18M10']
        
        
        df2.loc[df2['diffOM1_2'] == 0 ,'diffOM1_2'] = 0
        df2.loc[df2['diffOM1_2'] < 0 ,'diffOM1_2'] = -1
        df2.loc[df2['diffOM1_2'] > 0 ,'diffOM1_2'] = 1
        
  
        df2.loc[df2['diffOM2_3'] == 0 ,'diffOM2_3'] = 0
        df2.loc[df2['diffOM2_3'] < 0 ,'diffOM2_3'] = -1
        df2.loc[df2['diffOM2_3'] > 0 ,'diffOM2_3'] = 1
        
        df2.loc[df2['diffOM3_4'] == 0 ,'diffOM3_4'] = 0
        df2.loc[df2['diffOM3_4'] < 0 ,'diffOM3_4'] = -1
        df2.loc[df2['diffOM3_4'] > 0 ,'diffOM3_4'] = 1
        
        df2.loc[df2['diffOM4_5'] == 0 ,'diffOM4_5'] = 0
        df2.loc[df2['diffOM4_5'] < 0 ,'diffOM4_5'] = -1
        df2.loc[df2['diffOM4_5'] > 0 ,'diffOM4_5'] = 1
        
        df2.loc[df2['diffOM5_6'] == 0 ,'diffOM5_6'] = 0
        df2.loc[df2['diffOM5_6'] < 0 ,'diffOM5_6'] = -1
        df2.loc[df2['diffOM5_6'] > 0 ,'diffOM5_6'] = 1
         
        df2["OrderTag"] = df2["diffOM1_2"] + df2["diffOM2_3"]+  df2["diffOM3_4"]+ df2["diffOM4_5"]+  df2["diffOM5_6"]
        df2 = df2.drop(["diffOM1_2","diffOM2_3","diffOM3_4","diffOM4_5","diffOM5_6"],axis =1)
        df2 = df2.drop(["Order_19M1","Order_19M2","Order_19M3","Order_18M12","Order_18M11","Order_18M10"],axis =1)
        
        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df2['Volume_19M1'] = bizChurnFile['Volume_19M1']
        df2['Volume_19M2'] = bizChurnFile['Volume_19M2']
        df2['Volume_19M3'] = bizChurnFile['Volume_19M3']
        df2['Volume_18M10'] = bizChurnFile['Volume_18M10']
        df2['Volume_18M11'] = bizChurnFile['Volume_18M11']
        df2['Volume_18M12'] = bizChurnFile['Volume_18M12']
        
                 
        df2['Volume_19M1'].fillna(0,inplace=True)
        df2['Volume_19M2'].fillna(0,inplace=True)
        df2['Volume_19M3'].fillna(0,inplace=True)
        df2['Volume_18M12'].fillna(0,inplace=True)
        df2['Volume_18M11'].fillna(0,inplace=True)
        df2['Volume_18M10'].fillna(0,inplace=True)
        
        
        df2["diffVM1_2"] = df2['Volume_19M3'] - df2['Volume_19M2']    
        df2["diffVM2_3"] = df2['Volume_19M2'] - df2['Volume_19M1']
        df2["diffVM3_4"] = df2['Volume_19M1'] - df2['Volume_18M12']
        df2["diffVM4_5"] = df2['Volume_18M12'] - df2['Volume_18M11']
        df2["diffVM5_6"] = df2['Volume_18M11'] - df2['Volume_18M10']
        
        df2.loc[df2['diffVM1_2'] == 0 ,'diffVM1_2'] = 0
        df2.loc[df2['diffVM1_2'] < 0 ,'diffVM1_2'] = -1
        df2.loc[df2['diffVM1_2'] > 0 ,'diffVM1_2'] = 1
        
  
        df2.loc[df2['diffVM2_3'] == 0 ,'diffVM2_3'] = 0
        df2.loc[df2['diffVM2_3'] < 0 ,'diffVM2_3'] = -1
        df2.loc[df2['diffVM2_3'] > 0 ,'diffVM2_3'] = 1
        
        df2.loc[df2['diffVM3_4'] == 0 ,'diffVM3_4'] = 0
        df2.loc[df2['diffVM3_4'] < 0 ,'diffVM3_4'] = -1
        df2.loc[df2['diffVM3_4'] > 0 ,'diffVM3_4'] = 1
        
        df2.loc[df2['diffVM4_5'] == 0 ,'diffVM4_5'] = 0
        df2.loc[df2['diffVM4_5'] < 0 ,'diffVM4_5'] = -1
        df2.loc[df2['diffVM4_5'] > 0 ,'diffVM4_5'] = 1
        
        df2.loc[df2['diffVM5_6'] == 0 ,'diffVM5_6'] = 0
        df2.loc[df2['diffVM5_6'] < 0 ,'diffVM5_6'] = -1
        df2.loc[df2['diffVM5_6'] > 0 ,'diffVM5_6'] = 1
        
        df2["VolumeTag"] = df2["diffVM1_2"] + df2["diffVM2_3"]+  df2["diffVM3_4"]+ df2["diffVM4_5"]+  df2["diffVM5_6"]
        df2 = df2.drop(["diffVM1_2","diffVM2_3","diffVM3_4","diffVM4_5","diffVM5_6"],axis =1)
        df2 = df2.drop(["Volume_19M1","Volume_19M2","Volume_19M3","Volume_18M12","Volume_18M11","Volume_18M10"],axis =1)

        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df2['currency_19M1'] = bizChurnFile['currency_19M1']
        df2['currency_19M2'] = bizChurnFile['currency_19M2']
        df2['currency_19M3'] = bizChurnFile['currency_19M3']
        df2['currency_18M10'] = bizChurnFile['currency_18M10']
        df2['currency_18M11'] = bizChurnFile['currency_18M11']
        df2['currency_18M12'] = bizChurnFile['currency_18M12']
        
        df2['currency_19M1'].fillna(0,inplace=True)
        df2['currency_19M2'].fillna(0,inplace=True)
        df2['currency_19M3'].fillna(0,inplace=True)
        df2['currency_18M10'].fillna(0,inplace=True)
        df2['currency_18M11'].fillna(0,inplace=True)
        df2['currency_18M12'].fillna(0,inplace=True)
        
        #Difference for currency 
        df2["diffCM1_2"] = df2['currency_19M3'] - df2['currency_19M2']    
        df2["diffCM2_3"] = df2['currency_19M2'] - df2['currency_19M1']
        df2["diffCM3_4"] = df2['currency_19M1'] - df2['currency_18M12']
        df2["diffCM4_5"] = df2['currency_18M12'] - df2['currency_18M11']
        df2["diffCM5_6"] = df2['currency_18M11'] - df2['currency_18M10']
        

        df2.loc[df2['diffCM1_2'] == 0 ,'diffCM1_2'] = 0
        df2.loc[df2['diffCM1_2'] < 0 ,'diffCM1_2'] = -1
        df2.loc[df2['diffCM1_2'] > 0 ,'diffCM1_2'] = 1
        
  
        df2.loc[df2['diffCM2_3'] == 0 ,'diffCM2_3'] = 0
        df2.loc[df2['diffCM2_3'] < 0 ,'diffCM2_3'] = -1
        df2.loc[df2['diffCM2_3'] > 0 ,'diffCM2_3'] = 1
        
        df2.loc[df2['diffCM3_4'] == 0 ,'diffCM3_4'] = 0
        df2.loc[df2['diffCM3_4'] < 0 ,'diffCM3_4'] = -1
        df2.loc[df2['diffCM3_4'] > 0 ,'diffCM3_4'] = 1
        
        df2.loc[df2['diffCM4_5'] == 0 ,'diffCM4_5'] = 0
        df2.loc[df2['diffCM4_5'] < 0 ,'diffCM4_5'] = -1
        df2.loc[df2['diffCM4_5'] > 0 ,'diffCM4_5'] = 1
        
        df2.loc[df2['diffCM5_6'] == 0 ,'diffCM5_6'] = 0
        df2.loc[df2['diffCM5_6'] < 0 ,'diffCM5_6'] = -1
        df2.loc[df2['diffCM5_6'] > 0 ,'diffCM5_6'] = 1
         
        
        df2["CurrencyTag"] = df2["diffCM1_2"] + df2["diffCM2_3"]+  df2["diffCM3_4"]+ df2["diffCM4_5"]+  df2["diffCM5_6"]
        df2 = df2.drop(["diffCM1_2","diffCM2_3","diffCM3_4","diffCM4_5","diffCM5_6"],axis =1)
        df2 = df2.drop(["currency_19M1","currency_19M2","currency_19M3","currency_18M12","currency_18M11","currency_18M10"],axis =1)
        df2.to_csv('F19Q2.csv')
        

        
if Quarter == "Q3" :
    if currentYear == 2019 :
              # ADDING ORDERS OF PREV SIX MONTHS FROM THE QUARTER 
        df3['Order_19M1'] = bizChurnFile['Order_19M1']
        df3['Order_19M2'] = bizChurnFile['Order_19M2']
        df3['Order_19M3'] = bizChurnFile['Order_19M3']
        df3['Order_19M4'] = bizChurnFile['Order_19M4']
        df3['Order_19M5'] = bizChurnFile['Order_19M5']
        df3['Order_19M6'] = bizChurnFile['Order_19M6']
       
                
        df3['Order_19M6'].fillna(0,inplace=True)
        df3['Order_19M5'].fillna(0,inplace=True)
        df3['Order_19M4'].fillna(0,inplace=True)
        df3['Order_19M3'].fillna(0,inplace=True)
        df3['Order_19M2'].fillna(0,inplace=True)
        df3['Order_19M1'].fillna(0,inplace=True)
        
        #Difference for orders 
        df3["diffOM1_2"] = df3['Order_19M6'] - df3['Order_19M5']    
        df3["diffOM2_3"] = df3['Order_19M5'] - df3['Order_19M4']
        df3["diffOM3_4"] = df3['Order_19M4'] - df3['Order_19M3']
        df3["diffOM4_5"] = df3['Order_19M3'] - df3['Order_19M2']
        df3["diffOM5_6"] = df3['Order_19M2'] - df3['Order_19M1']
        
        
        df3.loc[df3['diffOM1_2'] == 0 ,'diffOM1_2'] = 0
        df3.loc[df3['diffOM1_2'] < 0 ,'diffOM1_2'] = -1
        df3.loc[df3['diffOM1_2'] > 0 ,'diffOM1_2'] = 1
        
  
        df3.loc[df3['diffOM2_3'] == 0 ,'diffOM2_3'] = 0
        df3.loc[df3['diffOM2_3'] < 0 ,'diffOM2_3'] = -1
        df3.loc[df3['diffOM2_3'] > 0 ,'diffOM2_3'] = 1
        
        df3.loc[df3['diffOM3_4'] == 0 ,'diffOM3_4'] = 0
        df3.loc[df3['diffOM3_4'] < 0 ,'diffOM3_4'] = -1
        df3.loc[df3['diffOM3_4'] > 0 ,'diffOM3_4'] = 1
        
        df3.loc[df3['diffOM4_5'] == 0 ,'diffOM4_5'] = 0
        df3.loc[df3['diffOM4_5'] < 0 ,'diffOM4_5'] = -1
        df3.loc[df3['diffOM4_5'] > 0 ,'diffOM4_5'] = 1
        
        df3.loc[df3['diffOM5_6'] == 0 ,'diffOM5_6'] = 0
        df3.loc[df3['diffOM5_6'] < 0 ,'diffOM5_6'] = -1
        df3.loc[df3['diffOM5_6'] > 0 ,'diffOM5_6'] = 1
         
        df3["OrderTag"] = df3["diffOM1_2"] + df3["diffOM2_3"]+  df3["diffOM3_4"]+ df3["diffOM4_5"]+  df3["diffOM5_6"]
        df3 = df3.drop(["diffOM1_2","diffOM2_3","diffOM3_4","diffOM4_5","diffOM5_6"],axis =1)
        df3 = df3.drop(["Order_19M1","Order_19M2","Order_19M3","Order_19M4","Order_19M5","Order_19M6"],axis =1)
        
        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df3['Volume_19M1'] = bizChurnFile['Volume_19M1']
        df3['Volume_19M2'] = bizChurnFile['Volume_19M2']
        df3['Volume_19M3'] = bizChurnFile['Volume_19M3']
        df3['Volume_19M4'] = bizChurnFile['Volume_19M4']
        df3['Volume_19M5'] = bizChurnFile['Volume_19M5']
        df3['Volume_19M6'] = bizChurnFile['Volume_19M6']
        
                 
        df3['Volume_19M1'].fillna(0,inplace=True)
        df3['Volume_19M2'].fillna(0,inplace=True)
        df3['Volume_19M3'].fillna(0,inplace=True)
        df3['Volume_19M4'].fillna(0,inplace=True)
        df3['Volume_19M5'].fillna(0,inplace=True)
        df3['Volume_19M6'].fillna(0,inplace=True)
        
        
        df3["diffVM1_2"] = df3['Volume_19M6'] - df3['Volume_19M5']    
        df3["diffVM2_3"] = df3['Volume_19M5'] - df3['Volume_19M4']
        df3["diffVM3_4"] = df3['Volume_19M4'] - df3['Volume_19M3']
        df3["diffVM4_5"] = df3['Volume_19M3'] - df3['Volume_19M2']
        df3["diffVM5_6"] = df3['Volume_19M2'] - df3['Volume_19M1']
        
        df3.loc[df3['diffVM1_2'] == 0 ,'diffVM1_2'] = 0
        df3.loc[df3['diffVM1_2'] < 0 ,'diffVM1_2'] = -1
        df3.loc[df3['diffVM1_2'] > 0 ,'diffVM1_2'] = 1
        
  
        df3.loc[df3['diffVM2_3'] == 0 ,'diffVM2_3'] = 0
        df3.loc[df3['diffVM2_3'] < 0 ,'diffVM2_3'] = -1
        df3.loc[df3['diffVM2_3'] > 0 ,'diffVM2_3'] = 1
        
        df3.loc[df3['diffVM3_4'] == 0 ,'diffVM3_4'] = 0
        df3.loc[df3['diffVM3_4'] < 0 ,'diffVM3_4'] = -1
        df3.loc[df3['diffVM3_4'] > 0 ,'diffVM3_4'] = 1
        
        df3.loc[df3['diffVM4_5'] == 0 ,'diffVM4_5'] = 0
        df3.loc[df3['diffVM4_5'] < 0 ,'diffVM4_5'] = -1
        df3.loc[df3['diffVM4_5'] > 0 ,'diffVM4_5'] = 1
        
        df3.loc[df3['diffVM5_6'] == 0 ,'diffVM5_6'] = 0
        df3.loc[df3['diffVM5_6'] < 0 ,'diffVM5_6'] = -1
        df3.loc[df3['diffVM5_6'] > 0 ,'diffVM5_6'] = 1
        
        df3["VolumeTag"] = df3["diffVM1_2"] + df3["diffVM2_3"]+  df3["diffVM3_4"]+ df3["diffVM4_5"]+  df3["diffVM5_6"]
        df3 = df3.drop(["diffVM1_2","diffVM2_3","diffVM3_4","diffVM4_5","diffVM5_6"],axis =1)
        df3 = df3.drop(["Volume_19M1","Volume_19M2","Volume_19M3","Volume_19M4","Volume_19M5","Volume_19M6"],axis =1)

        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df3['currency_19M1'] = bizChurnFile['currency_19M1']
        df3['currency_19M2'] = bizChurnFile['currency_19M2']
        df3['currency_19M3'] = bizChurnFile['currency_19M3']
        df3['currency_19M4'] = bizChurnFile['currency_19M4']
        df3['currency_19M5'] = bizChurnFile['currency_19M5']
        df3['currency_19M6'] = bizChurnFile['currency_19M6']
        
        
        df3['currency_19M6'].fillna(0,inplace=True)
        df3['currency_19M5'].fillna(0,inplace=True)
        df3['currency_19M4'].fillna(0,inplace=True)
        df3['currency_19M3'].fillna(0,inplace=True)
        df3['currency_19M2'].fillna(0,inplace=True)
        df3['currency_19M1'].fillna(0,inplace=True)
        
        

        ###################
        #Difference for currency 
        df3["diffCM1_2"] = df3['currency_19M6'] - df3['currency_19M5']    
        df3["diffCM2_3"] = df3['currency_19M5'] - df3['currency_19M4']
        df3["diffCM3_4"] = df3['currency_19M4'] - df3['currency_19M3']
        df3["diffCM4_5"] = df3['currency_19M3'] - df3['currency_19M2']
        df3["diffCM5_6"] = df3['currency_19M2'] - df3['currency_19M1']
        
        df3.loc[df3['diffCM1_2'] == 0 ,'diffCM1_2'] = 0
        df3.loc[df3['diffCM1_2'] < 0 ,'diffCM1_2'] = -1
        df3.loc[df3['diffCM1_2'] > 0 ,'diffCM1_2'] = 1
        
  
        df3.loc[df3['diffCM2_3'] == 0 ,'diffCM2_3'] = 0
        df3.loc[df3['diffCM2_3'] < 0 ,'diffCM2_3'] = -1
        df3.loc[df3['diffCM2_3'] > 0 ,'diffCM2_3'] = 1
        
        df3.loc[df3['diffCM3_4'] == 0 ,'diffCM3_4'] = 0
        df3.loc[df3['diffCM3_4'] < 0 ,'diffCM3_4'] = -1
        df3.loc[df3['diffCM3_4'] > 0 ,'diffCM3_4'] = 1
        
        df3.loc[df3['diffCM4_5'] == 0 ,'diffCM4_5'] = 0
        df3.loc[df3['diffCM4_5'] < 0 ,'diffCM4_5'] = -1
        df3.loc[df3['diffCM4_5'] > 0 ,'diffCM4_5'] = 1
        
        df3.loc[df3['diffCM5_6'] == 0 ,'diffCM5_6'] = 0
        df3.loc[df3['diffCM5_6'] < 0 ,'diffCM5_6'] = -1
        df3.loc[df3['diffCM5_6'] > 0 ,'diffCM5_6'] = 1
         
        
        df3["CurrencyTag"] = df3["diffCM1_2"] + df3["diffCM2_3"]+  df3["diffCM3_4"]+ df3["diffCM4_5"]+  df3["diffCM5_6"]
        df3 = df3.drop(["diffCM1_2","diffCM2_3","diffCM3_4","diffCM4_5","diffCM5_6"],axis =1)
        df3 = df3.drop(["currency_19M1","currency_19M2","currency_19M3","currency_19M4","currency_19M5","currency_19M6"],axis =1)
        df3.to_csv('F19Q3.csv')
        
        
if Quarter == "Q3" :
    if currentYear == 2018 :
        
        df4['Order_18M1'] = bizChurnFile['Order_18M1']
        df4['Order_18M2'] = bizChurnFile['Order_18M2']
        df4['Order_18M3'] = bizChurnFile['Order_18M3']
        df4['Order_18M4'] = bizChurnFile['Order_18M4']
        df4['Order_18M5'] = bizChurnFile['Order_18M5']
        df4['Order_18M6'] = bizChurnFile['Order_18M6']
       
                 
        df4['Order_18M6'].fillna(0,inplace=True)
        df4['Order_18M5'].fillna(0,inplace=True)
        df4['Order_18M4'].fillna(0,inplace=True)
        df4['Order_18M3'].fillna(0,inplace=True)
        df4['Order_18M2'].fillna(0,inplace=True)
        df4['Order_18M1'].fillna(0,inplace=True)
        
        #Difference for orders 
        df4["diffOM1_2"] = df4['Order_18M6'] - df4['Order_18M5']    
        df4["diffOM2_3"] = df4['Order_18M5'] - df4['Order_18M4']
        df4["diffOM3_4"] = df4['Order_18M4'] - df4['Order_18M3']
        df4["diffOM4_5"] = df4['Order_18M3'] - df4['Order_18M2']
        df4["diffOM5_6"] = df4['Order_18M2'] - df4['Order_18M1']
        
        
        df4.loc[df4['diffOM1_2'] == 0 ,'diffOM1_2'] = 0
        df4.loc[df4['diffOM1_2'] < 0 ,'diffOM1_2'] = -1
        df4.loc[df4['diffOM1_2'] > 0 ,'diffOM1_2'] = 1
        
  
        df4.loc[df4['diffOM2_3'] == 0 ,'diffOM2_3'] = 0
        df4.loc[df4['diffOM2_3'] < 0 ,'diffOM2_3'] = -1
        df4.loc[df4['diffOM2_3'] > 0 ,'diffOM2_3'] = 1
        
        df4.loc[df4['diffOM3_4'] == 0 ,'diffOM3_4'] = 0
        df4.loc[df4['diffOM3_4'] < 0 ,'diffOM3_4'] = -1
        df4.loc[df4['diffOM3_4'] > 0 ,'diffOM3_4'] = 1
        
        df4.loc[df4['diffOM4_5'] == 0 ,'diffOM4_5'] = 0
        df4.loc[df4['diffOM4_5'] < 0 ,'diffOM4_5'] = -1
        df4.loc[df4['diffOM4_5'] > 0 ,'diffOM4_5'] = 1
        
        df4.loc[df4['diffOM5_6'] == 0 ,'diffOM5_6'] = 0
        df4.loc[df4['diffOM5_6'] < 0 ,'diffOM5_6'] = -1
        df4.loc[df4['diffOM5_6'] > 0 ,'diffOM5_6'] = 1
         
        df4["OrderTag"] = df4["diffOM1_2"] + df4["diffOM2_3"]+  df4["diffOM3_4"]+ df4["diffOM4_5"]+  df4["diffOM5_6"]
        df4 = df4.drop(["diffOM1_2","diffOM2_3","diffOM3_4","diffOM4_5","diffOM5_6"],axis =1)
        df4 = df4.drop(["Order_18M1","Order_18M2","Order_18M3","Order_18M4","Order_18M5","Order_18M6"],axis =1)
        

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df4['Volume_18M1'] = bizChurnFile['Volume_18M1']
        df4['Volume_18M2'] = bizChurnFile['Volume_18M2']
        df4['Volume_18M3'] = bizChurnFile['Volume_18M3']
        df4['Volume_18M4'] = bizChurnFile['Volume_18M4']
        df4['Volume_18M5'] = bizChurnFile['Volume_18M5']
        df4['Volume_18M6'] = bizChurnFile['Volume_18M6']
        
        df4['Volume_18M1'].fillna(0,inplace=True)
        df4['Volume_18M2'].fillna(0,inplace=True)
        df4['Volume_18M3'].fillna(0,inplace=True)
        df4['Volume_18M4'].fillna(0,inplace=True)
        df4['Volume_18M5'].fillna(0,inplace=True)
        df4['Volume_18M6'].fillna(0,inplace=True)
        
        
        df4["diffVM1_2"] = df4['Volume_18M6'] - df4['Volume_18M5']    
        df4["diffVM2_3"] = df4['Volume_18M5'] - df4['Volume_18M4']
        df4["diffVM3_4"] = df4['Volume_18M4'] - df4['Volume_18M3']
        df4["diffVM4_5"] = df4['Volume_18M3'] - df4['Volume_18M2']
        df4["diffVM5_6"] = df4['Volume_18M2'] - df4['Volume_18M1']
        
        df4.loc[df4['diffVM1_2'] == 0 ,'diffVM1_2'] = 0
        df4.loc[df4['diffVM1_2'] < 0 ,'diffVM1_2'] = -1
        df4.loc[df4['diffVM1_2'] > 0 ,'diffVM1_2'] = 1
        
  
        df4.loc[df4['diffVM2_3'] == 0 ,'diffVM2_3'] = 0
        df4.loc[df4['diffVM2_3'] < 0 ,'diffVM2_3'] = -1
        df4.loc[df4['diffVM2_3'] > 0 ,'diffVM2_3'] = 1
        
        df4.loc[df4['diffVM3_4'] == 0 ,'diffVM3_4'] = 0
        df4.loc[df4['diffVM3_4'] < 0 ,'diffVM3_4'] = -1
        df4.loc[df4['diffVM3_4'] > 0 ,'diffVM3_4'] = 1
        
        df4.loc[df4['diffVM4_5'] == 0 ,'diffVM4_5'] = 0
        df4.loc[df4['diffVM4_5'] < 0 ,'diffVM4_5'] = -1
        df4.loc[df4['diffVM4_5'] > 0 ,'diffVM4_5'] = 1
        
        df4.loc[df4['diffVM5_6'] == 0 ,'diffVM5_6'] = 0
        df4.loc[df4['diffVM5_6'] < 0 ,'diffVM5_6'] = -1
        df4.loc[df4['diffVM5_6'] > 0 ,'diffVM5_6'] = 1
        
        df4["VolumeTag"] = df4["diffVM1_2"] + df4["diffVM2_3"]+  df4["diffVM3_4"]+ df4["diffVM4_5"]+  df4["diffVM5_6"]
        df4 = df4.drop(["diffVM1_2","diffVM2_3","diffVM3_4","diffVM4_5","diffVM5_6"],axis =1)
        df4 = df4.drop(["Volume_18M1","Volume_18M2","Volume_18M3","Volume_18M4","Volume_18M5","Volume_18M6"],axis =1)

        
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df4['currency_18M1'] = bizChurnFile['currency_18M1']
        df4['currency_18M2'] = bizChurnFile['currency_18M2']
        df4['currency_18M3'] = bizChurnFile['currency_18M3']
        df4['currency_18M4'] = bizChurnFile['currency_18M4']
        df4['currency_18M5'] = bizChurnFile['currency_18M5']
        df4['currency_18M6'] = bizChurnFile['currency_18M6']
        
        df4['currency_18M6'].fillna(0,inplace=True)
        df4['currency_18M5'].fillna(0,inplace=True)
        df4['currency_18M4'].fillna(0,inplace=True)
        df4['currency_18M3'].fillna(0,inplace=True)
        df4['currency_18M2'].fillna(0,inplace=True)
        df4['currency_18M1'].fillna(0,inplace=True)
        
        

        ###################
        #Difference for currency 
        df4["diffCM1_2"] = df4['currency_18M6'] - df4['currency_18M5']    
        df4["diffCM2_3"] = df4['currency_18M5'] - df4['currency_18M4']
        df4["diffCM3_4"] = df4['currency_18M4'] - df4['currency_18M3']
        df4["diffCM4_5"] = df4['currency_18M3'] - df4['currency_18M2']
        df4["diffCM5_6"] = df4['currency_18M2'] - df4['currency_18M1']
        
    
        df4.loc[df4['diffCM1_2'] == 0 ,'diffCM1_2'] = 0
        df4.loc[df4['diffCM1_2'] < 0 ,'diffCM1_2'] = -1
        df4.loc[df4['diffCM1_2'] > 0 ,'diffCM1_2'] = 1
        
  
        df4.loc[df4['diffCM2_3'] == 0 ,'diffCM2_3'] = 0
        df4.loc[df4['diffCM2_3'] < 0 ,'diffCM2_3'] = -1
        df4.loc[df4['diffCM2_3'] > 0 ,'diffCM2_3'] = 1
        
        df4.loc[df4['diffCM3_4'] == 0 ,'diffCM3_4'] = 0
        df4.loc[df4['diffCM3_4'] < 0 ,'diffCM3_4'] = -1
        df4.loc[df4['diffCM3_4'] > 0 ,'diffCM3_4'] = 1
        
        df4.loc[df4['diffCM4_5'] == 0 ,'diffCM4_5'] = 0
        df4.loc[df4['diffCM4_5'] < 0 ,'diffCM4_5'] = -1
        df4.loc[df4['diffCM4_5'] > 0 ,'diffCM4_5'] = 1
        
        df4.loc[df4['diffCM5_6'] == 0 ,'diffCM5_6'] = 0
        df4.loc[df4['diffCM5_6'] < 0 ,'diffCM5_6'] = -1
        df4.loc[df4['diffCM5_6'] > 0 ,'diffCM5_6'] = 1
         
        
        df4["CurrencyTag"] = df4["diffCM1_2"] + df4["diffCM2_3"]+  df4["diffCM3_4"]+ df4["diffCM4_5"]+  df4["diffCM5_6"]
        df4 = df4.drop(["diffCM1_2","diffCM2_3","diffCM3_4","diffCM4_5","diffCM5_6"],axis =1)
        df4 = df4.drop(["currency_18M1","currency_18M2","currency_18M3","currency_18M4","currency_18M5","currency_18M6"],axis =1)
        df4.to_csv('F18Q3.csv')
        
        df4.to_csv('F18Q3.csv')
        
        
        
if Quarter == "Q4" :
    if currentYear == 2018 :
        
        # ADDING ORDERS OF PREV SIX MONTHS FROM THE QUARTER 
        df5['Order_18M4'] = bizChurnFile['Order_18M4']
        df5['Order_18M5'] = bizChurnFile['Order_18M5']
        df5['Order_18M6'] = bizChurnFile['Order_18M6']
        df5['Order_18M7'] = bizChurnFile['Order_18M7']
        df5['Order_18M8'] = bizChurnFile['Order_18M8']
        df5['Order_18M9'] = bizChurnFile['Order_18M9']
        
       
        df5['Order_18M4'].fillna(0,inplace=True)
        df5['Order_18M5'].fillna(0,inplace=True)
        df5['Order_18M6'].fillna(0,inplace=True)
        df5['Order_18M7'].fillna(0,inplace=True)
        df5['Order_18M8'].fillna(0,inplace=True)
        df5['Order_18M9'].fillna(0,inplace=True)
        
        #Difference for orders 
        df5["diffOM1_2"] = df5['Order_18M9'] - df5['Order_18M8']    
        df5["diffOM2_3"] = df5['Order_18M8'] - df5['Order_18M7']
        df5["diffOM3_4"] = df5['Order_18M7'] - df5['Order_18M6']
        df5["diffOM4_5"] = df5['Order_18M6'] - df5['Order_18M5']
        df5["diffOM5_6"] = df5['Order_18M5'] - df5['Order_18M4']
        
        
        df5.loc[df5['diffOM1_2'] == 0 ,'diffOM1_2'] = 0
        df5.loc[df5['diffOM1_2'] < 0 ,'diffOM1_2'] = -1
        df5.loc[df5['diffOM1_2'] > 0 ,'diffOM1_2'] = 1
        
  
        df5.loc[df5['diffOM2_3'] == 0 ,'diffOM2_3'] = 0
        df5.loc[df5['diffOM2_3'] < 0 ,'diffOM2_3'] = -1
        df5.loc[df5['diffOM2_3'] > 0 ,'diffOM2_3'] = 1
        
        df5.loc[df5['diffOM3_4'] == 0 ,'diffOM3_4'] = 0
        df5.loc[df5['diffOM3_4'] < 0 ,'diffOM3_4'] = -1
        df5.loc[df5['diffOM3_4'] > 0 ,'diffOM3_4'] = 1
        
        df5.loc[df5['diffOM4_5'] == 0 ,'diffOM4_5'] = 0
        df5.loc[df5['diffOM4_5'] < 0 ,'diffOM4_5'] = -1
        df5.loc[df5['diffOM4_5'] > 0 ,'diffOM4_5'] = 1
        
        df5.loc[df5['diffOM5_6'] == 0 ,'diffOM5_6'] = 0
        df5.loc[df5['diffOM5_6'] < 0 ,'diffOM5_6'] = -1
        df5.loc[df5['diffOM5_6'] > 0 ,'diffOM5_6'] = 1
         
        df5["OrderTag"] = df5["diffOM1_2"] + df5["diffOM2_3"]+  df5["diffOM3_4"]+ df5["diffOM4_5"]+  df5["diffOM5_6"]
        df5 = df5.drop(["diffOM1_2","diffOM2_3","diffOM3_4","diffOM4_5","diffOM5_6"],axis =1)
        df5 = df5.drop(["Order_18M7","Order_18M8","Order_18M9","Order_18M4","Order_18M5","Order_18M6"],axis =1)
        

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        
        df5['Volume_18M4'] = bizChurnFile['Volume_18M4']
        df5['Volume_18M5'] = bizChurnFile['Volume_18M5']
        df5['Volume_18M6'] = bizChurnFile['Volume_18M6']
        df5['Volume_18M7'] = bizChurnFile['Volume_18M7']
        df5['Volume_18M8'] = bizChurnFile['Volume_18M8']
        df5['Volume_18M9'] = bizChurnFile['Volume_18M9']
        
        df5['Volume_18M7'].fillna(0,inplace=True)
        df5['Volume_18M8'].fillna(0,inplace=True)
        df5['Volume_18M9'].fillna(0,inplace=True)
        df5['Volume_18M4'].fillna(0,inplace=True)
        df5['Volume_18M5'].fillna(0,inplace=True)
        df5['Volume_18M6'].fillna(0,inplace=True)
        
        
        df5["diffVM1_2"] = df5['Volume_18M9'] - df5['Volume_18M8']    
        df5["diffVM2_3"] = df5['Volume_18M8'] - df5['Volume_18M7']
        df5["diffVM3_4"] = df5['Volume_18M7'] - df5['Volume_18M6']
        df5["diffVM4_5"] = df5['Volume_18M6'] - df5['Volume_18M5']
        df5["diffVM5_6"] = df5['Volume_18M5'] - df5['Volume_18M4']
        
        df5.loc[df5['diffVM1_2'] == 0 ,'diffVM1_2'] = 0
        df5.loc[df5['diffVM1_2'] < 0 ,'diffVM1_2'] = -1
        df5.loc[df5['diffVM1_2'] > 0 ,'diffVM1_2'] = 1
        
  
        df5.loc[df5['diffVM2_3'] == 0 ,'diffVM2_3'] = 0
        df5.loc[df5['diffVM2_3'] < 0 ,'diffVM2_3'] = -1
        df5.loc[df5['diffVM2_3'] > 0 ,'diffVM2_3'] = 1
        
        df5.loc[df5['diffVM3_4'] == 0 ,'diffVM3_4'] = 0
        df5.loc[df5['diffVM3_4'] < 0 ,'diffVM3_4'] = -1
        df5.loc[df5['diffVM3_4'] > 0 ,'diffVM3_4'] = 1
        
        df5.loc[df5['diffVM4_5'] == 0 ,'diffVM4_5'] = 0
        df5.loc[df5['diffVM4_5'] < 0 ,'diffVM4_5'] = -1
        df5.loc[df5['diffVM4_5'] > 0 ,'diffVM4_5'] = 1
        
        df5.loc[df5['diffVM5_6'] == 0 ,'diffVM5_6'] = 0
        df5.loc[df5['diffVM5_6'] < 0 ,'diffVM5_6'] = -1
        df5.loc[df5['diffVM5_6'] > 0 ,'diffVM5_6'] = 1
        
        df5["VolumeTag"] = df5["diffVM1_2"] + df5["diffVM2_3"]+  df5["diffVM3_4"]+ df5["diffVM4_5"]+  df5["diffVM5_6"]
        df5 = df5.drop(["diffVM1_2","diffVM2_3","diffVM3_4","diffVM4_5","diffVM5_6"],axis =1)
        df5 = df5.drop(["Volume_18M7","Volume_18M8","Volume_18M9","Volume_18M4","Volume_18M5","Volume_18M6"],axis =1)

        
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df5['currency_18M7'] = bizChurnFile['currency_18M7']
        df5['currency_18M8'] = bizChurnFile['currency_18M8']
        df5['currency_18M9'] = bizChurnFile['currency_18M9']
        df5['currency_18M4'] = bizChurnFile['currency_18M4']
        df5['currency_18M5'] = bizChurnFile['currency_18M5']
        df5['currency_18M6'] = bizChurnFile['currency_18M6']
        
        df5['currency_18M6'].fillna(0,inplace=True)
        df5['currency_18M5'].fillna(0,inplace=True)
        df5['currency_18M4'].fillna(0,inplace=True)
        df5['currency_18M7'].fillna(0,inplace=True)
        df5['currency_18M8'].fillna(0,inplace=True)
        df5['currency_18M9'].fillna(0,inplace=True)
        
        

        ###################
        #Difference for currency 
        df5["diffCM1_2"] = df5['currency_18M9'] - df5['currency_18M8']    
        df5["diffCM2_3"] = df5['currency_18M8'] - df5['currency_18M7']
        df5["diffCM3_4"] = df5['currency_18M7'] - df5['currency_18M6']
        df5["diffCM4_5"] = df5['currency_18M6'] - df5['currency_18M5']
        df5["diffCM5_6"] = df5['currency_18M5'] - df5['currency_18M4']
        
    
        df5.loc[df5['diffCM1_2'] == 0 ,'diffCM1_2'] = 0
        df5.loc[df5['diffCM1_2'] < 0 ,'diffCM1_2'] = -1
        df5.loc[df5['diffCM1_2'] > 0 ,'diffCM1_2'] = 1
        
  
        df5.loc[df5['diffCM2_3'] == 0 ,'diffCM2_3'] = 0
        df5.loc[df5['diffCM2_3'] < 0 ,'diffCM2_3'] = -1
        df5.loc[df5['diffCM2_3'] > 0 ,'diffCM2_3'] = 1
        
        df5.loc[df5['diffCM3_4'] == 0 ,'diffCM3_4'] = 0
        df5.loc[df5['diffCM3_4'] < 0 ,'diffCM3_4'] = -1
        df5.loc[df5['diffCM3_4'] > 0 ,'diffCM3_4'] = 1
        
        df5.loc[df5['diffCM4_5'] == 0 ,'diffCM4_5'] = 0
        df5.loc[df5['diffCM4_5'] < 0 ,'diffCM4_5'] = -1
        df5.loc[df5['diffCM4_5'] > 0 ,'diffCM4_5'] = 1
        
        df5.loc[df5['diffCM5_6'] == 0 ,'diffCM5_6'] = 0
        df5.loc[df5['diffCM5_6'] < 0 ,'diffCM5_6'] = -1
        df5.loc[df5['diffCM5_6'] > 0 ,'diffCM5_6'] = 1
         
        
        df5["CurrencyTag"] = df5["diffCM1_2"] + df5["diffCM2_3"]+  df5["diffCM3_4"]+ df5["diffCM4_5"]+  df5["diffCM5_6"]
        df5 = df5.drop(["diffCM1_2","diffCM2_3","diffCM3_4","diffCM4_5","diffCM5_6"],axis =1)
        df5 = df5.drop(["currency_18M9","currency_18M8","currency_18M7","currency_18M4","currency_18M5","currency_18M6"],axis =1)
        df5.to_csv('F18Q3.csv')

        
        df5.to_csv('F18Q4.csv')

        
        

        
    
    
 




