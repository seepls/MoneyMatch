#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:53:22 2019

@author: smrititiwari
"""


# making file 1 
# 19 Q3 :
# 19M1,19M2,19M3,19M4,19M5,19M6
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
currentMonth = 8

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
       

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df1['Volume_18M7'] = bizChurnFile['Volume_18M7']
        df1['Volume_18M8'] = bizChurnFile['Volume_18M8']
        df1['Volume_18M9'] = bizChurnFile['Volume_18M9']
        df1['Volume_18M10'] = bizChurnFile['Volume_18M10']
        df1['Volume_18M11'] = bizChurnFile['Volume_18M11']
        df1['Volume_18M12'] = bizChurnFile['Volume_18M12']
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df1['currency_18M7'] = bizChurnFile['currency_18M7']
        df1['currency_18M8'] = bizChurnFile['currency_18M8']
        df1['currency_18M9'] = bizChurnFile['currency_18M9']
        df1['currency_18M10'] = bizChurnFile['currency_18M10']
        df1['currency_18M11'] = bizChurnFile['currency_18M11']
        df1['currency_18M12'] = bizChurnFile['currency_18M12']
        
        
        
        
        
        #df1.fillna(0, inplace=True)
        
        df1["diffM1_2"] = df1['currency_18M12'] - df1['currency_18M11']
        df1["diffM2_3"] = df1['currency_18M11'] - df1['currency_18M10']
        df1["diffM3_4"] = df1['currency_18M10'] - df1['currency_18M9']
        df1["diffM4_5"] = df1['currency_18M9'] - df1['currency_18M8']
        df1["diffM5_6"] = df1['currency_18M8'] - df1['currency_18M7']
        
        
        
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
       

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df2['Volume_19M1'] = bizChurnFile['Volume_19M1']
        df2['Volume_19M2'] = bizChurnFile['Volume_19M2']
        df2['Volume_19M3'] = bizChurnFile['Volume_19M3']
        df2['Volume_18M10'] = bizChurnFile['Volume_18M10']
        df2['Volume_18M11'] = bizChurnFile['Volume_18M11']
        df2['Volume_18M12'] = bizChurnFile['Volume_18M12']
        
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df2['currency_19M1'] = bizChurnFile['currency_19M1']
        df2['currency_19M2'] = bizChurnFile['currency_19M2']
        df2['currency_19M3'] = bizChurnFile['currency_19M3']
        df2['currency_18M10'] = bizChurnFile['currency_18M10']
        df2['currency_18M11'] = bizChurnFile['currency_18M11']
        df2['currency_18M12'] = bizChurnFile['currency_18M12']
        
        df3['currency_19M6'].fillna(0,inplace=True)
        df3['currency_19M5'].fillna(0,inplace=True)
        df3['currency_19M4'].fillna(0,inplace=True)
        df3['currency_19M3'].fillna(0,inplace=True)
        df3['currency_19M2'].fillna(0,inplace=True)
        df3['currency_19M1'].fillna(0,inplace=True)
        
        df3['currency_19M6'].fillna(0,inplace=True)
        df3['currency_19M5'].fillna(0,inplace=True)
        df3['currency_19M4'].fillna(0,inplace=True)
        df3['currency_19M3'].fillna(0,inplace=True)
        df3['currency_19M2'].fillna(0,inplace=True)
        df3['currency_19M1'].fillna(0,inplace=True)
        
        df3['currency_19M6'].fillna(0,inplace=True)
        df3['currency_19M5'].fillna(0,inplace=True)
        df3['currency_19M4'].fillna(0,inplace=True)
        df3['currency_19M3'].fillna(0,inplace=True)
        df3['currency_19M2'].fillna(0,inplace=True)
        df3['currency_19M1'].fillna(0,inplace=True)
        
        
        
       
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
       

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df3['Volume_19M1'] = bizChurnFile['Volume_19M1']
        df3['Volume_19M2'] = bizChurnFile['Volume_19M2']
        df3['Volume_19M3'] = bizChurnFile['Volume_19M3']
        df3['Volume_19M4'] = bizChurnFile['Volume_19M4']
        df3['Volume_19M5'] = bizChurnFile['Volume_19M5']
        df3['Volume_19M6'] = bizChurnFile['Volume_19M6']
        
        
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
        
         
        df3['Volume_19M1'].fillna(0,inplace=True)
        df3['Volume_19M2'].fillna(0,inplace=True)
        df3['Volume_19M3'].fillna(0,inplace=True)
        df3['Volume_19M4'].fillna(0,inplace=True)
        df3['Volume_19M5'].fillna(0,inplace=True)
        df3['Volume_19M6'].fillna(0,inplace=True)
        
        df3['Order_19M6'].fillna(0,inplace=True)
        df3['Order_19M5'].fillna(0,inplace=True)
        df3['Order_19M4'].fillna(0,inplace=True)
        df3['Order_19M3'].fillna(0,inplace=True)
        df3['Order_19M2'].fillna(0,inplace=True)
        df3['Order_19M1'].fillna(0,inplace=True)
        
        
        df3["diffM1_2"] = df3['currency_19M6'] - df3['currency_19M5']
        df3["diffM2_3"] = df3['currency_19M5'] - df3['currency_19M4']
        df3["diffM3_4"] = df3['currency_19M4'] - df3['currency_19M3']
        df3["diffM4_5"] = df3['currency_19M3'] - df3['currency_19M2']
        df3["diffM5_6"] = df3['currency_19M2'] - df3['currency_19M1']
        
        
        
        df3.to_csv('F19Q3.csv')
    else : 
        
        df4['Order_18M1'] = bizChurnFile['Order_18M1']
        df4['Order_18M2'] = bizChurnFile['Order_18M2']
        df4['Order_18M3'] = bizChurnFile['Order_18M3']
        df4['Order_18M4'] = bizChurnFile['Order_18M4']
        df4['Order_18M5'] = bizChurnFile['Order_18M5']
        df4['Order_18M6'] = bizChurnFile['Order_18M6']
       

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df4['Volume_18M1'] = bizChurnFile['Volume_18M1']
        df4['Volume_18M2'] = bizChurnFile['Volume_18M2']
        df4['Volume_18M3'] = bizChurnFile['Volume_18M3']
        df4['Volume_18M4'] = bizChurnFile['Volume_18M4']
        df4['Volume_18M5'] = bizChurnFile['Volume_18M5']
        df4['Volume_18M6'] = bizChurnFile['Volume_18M6']
        
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df4['currency_18M1'] = bizChurnFile['currency_18M1']
        df4['currency_18M2'] = bizChurnFile['currency_18M2']
        df4['currency_18M3'] = bizChurnFile['currency_18M3']
        df4['currency_18M4'] = bizChurnFile['currency_18M4']
        df4['currency_18M5'] = bizChurnFile['currency_18M5']
        df4['currency_18M6'] = bizChurnFile['currency_18M6']
        
        df4.to_csv('F18Q3.csv')
        
        
        
if Quarter == "Q4" :
    if currentYear == 2018 :
              # ADDING ORDERS OF PREV SIX MONTHS FROM THE QUARTER 
        df5['Order_18M7'] = bizChurnFile['Order_18M7']
        df5['Order_18M8'] = bizChurnFile['Order_18M8']
        df5['Order_18M9'] = bizChurnFile['Order_18M9']
        df5['Order_18M4'] = bizChurnFile['Order_18M4']
        df5['Order_18M5'] = bizChurnFile['Order_18M5']
        df5['Order_18M6'] = bizChurnFile['Order_18M6']
       

        # ADDING THE VOLUME OF ORDERS MADE IN PREVIOUS SIX MONTH 
        df5['Volume_18M7'] = bizChurnFile['Volume_18M7']
        df5['Volume_18M8'] = bizChurnFile['Volume_18M8']
        df5['Volume_18M9'] = bizChurnFile['Volume_18M9']
        df5['Volume_18M4'] = bizChurnFile['Volume_18M4']
        df5['Volume_18M5'] = bizChurnFile['Volume_18M5']
        df5['Volume_18M6'] = bizChurnFile['Volume_18M6']
        
        
        # ADDING THE TYPE OF CURRENCY EXCHANGED IN PREVIOUS SIX MONTH 
        df5['currency_18M7'] = bizChurnFile['currency_18M7']
        df5['currency_18M8'] = bizChurnFile['currency_18M8']
        df5['currency_18M9'] = bizChurnFile['currency_18M9']
        df5['currency_18M4'] = bizChurnFile['currency_18M4']
        df5['currency_18M5'] = bizChurnFile['currency_18M5']
        df5['currency_18M6'] = bizChurnFile['currency_18M6']
        
        
        df5.to_csv('F18Q4.csv')

        
        

        
    
    
 




