
#Importing Libraries
import numpy as np
import pandas as pd
import math
import os
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


os.getcwd()

#Importing Data
RetailBase_df=pd.read_csv('PriceSensitivity.csv',encoding = 'unicode_escape')

#Creating Trainning Dataset
for col in RetailBase_df.columns: 
    print(col)
    
'''user_id
PSProxy
coupon_amount_myr
coupon_used
nationality
gender
job_sector
risk
days_from_last_transx
avg_transx_size
orders
total_volume
mean_ccy
no_of_bene
mean_bene_country
age
state
postal_code
country Dependent Variable : SensitivityTag'''
RetailBase_df=RetailBase_df[['user_id', 'PSProxy', 'coupon_amount_myr', 'coupon_used', 'nationality', 'gender', 'job_sector', 'occupation', 'risk', 'days_from_last_transx', 'avg_transx_size', 'orders', 'total_volume', 'mean_ccy', 'no_of_bene', 'mean_bene_country', 'age', 'state', 'postal_code', 'SensitivityTag']]

###Nationality
RetailBase_df.nationality.value_counts()

RetailBase_df.loc[RetailBase_df['nationality']=='Indian', 'Indian'] = 1
RetailBase_df.loc[RetailBase_df['nationality']!='Indian', 'Indian'] = 0

RetailBase_df.loc[RetailBase_df['nationality']=='Malaysian', 'Malaysian'] = 1
RetailBase_df.loc[RetailBase_df['nationality']!='Malaysian', 'Malaysian'] = 0

RetailBase_df.loc[(RetailBase_df['nationality']!='Indian')&(RetailBase_df['nationality']!='Malaysian'), 'NationalityOther'] = 1
RetailBase_df.loc[(RetailBase_df['nationality']=='Indian')|(RetailBase_df['nationality']=='Malaysian'), 'NationalityOther'] = 0

###Gender 
RetailBase_df.gender.value_counts()

RetailBase_df.loc[RetailBase_df['gender']=='Male', 'Gender_Final'] = 1
RetailBase_df.loc[RetailBase_df['gender']=='Female', 'Gender_Final'] = 0

###job_sector
RetailBase_df.job_sector.value_counts()

RetailBase_df.loc[RetailBase_df['job_sector']=='Property and construction', 'job_sector'] = 'Construction'

RetailBase_df.job_sector.value_counts()

RetailBase_df.loc[(RetailBase_df['job_sector']=='Environment and agriculture')|(RetailBase_df['job_sector']=='Real Estate')|(RetailBase_df['job_sector']=='Law')|(RetailBase_df['job_sector']=='Sales')|(RetailBase_df['job_sector']=='Construction'), 'Job_sector_BinA'] = 1
RetailBase_df.loc[(RetailBase_df['job_sector']!='Environment and agriculture')&(RetailBase_df['job_sector']!='Real Estate')&(RetailBase_df['job_sector']!='Law')&(RetailBase_df['job_sector']!='Sales')&(RetailBase_df['job_sector']!='Construction'), 'Job_sector_BinA'] = 0

RetailBase_df.loc[(RetailBase_df['job_sector']=='Accountancy, banking and finance')|(RetailBase_df['job_sector']=='Public services and administration')|(RetailBase_df['job_sector']=='Business, consulting and management')|(RetailBase_df['job_sector']=='Media and internet')|(RetailBase_df['job_sector']=='Health-care')|(RetailBase_df['job_sector']=='Transport and logistics')|(RetailBase_df['job_sector']=='Hospitality and events management')|(RetailBase_df['job_sector']=='Teaching and education')|(RetailBase_df['job_sector']=='Retail')|(RetailBase_df['job_sector']=='Law enforcement and security')|(RetailBase_df['job_sector']=='Other')|(RetailBase_df['job_sector']=='Creative arts and design')|(RetailBase_df['job_sector']=='Leisure, sports and tourism'), 'Job_sector_BinB'] = 1
RetailBase_df.loc[(RetailBase_df['job_sector']!='Accountancy, banking and finance')&(RetailBase_df['job_sector']!='Public services and administration')&(RetailBase_df['job_sector']!='Business, consulting and management')&(RetailBase_df['job_sector']!='Media and internet')&(RetailBase_df['job_sector']!='Health-care')&(RetailBase_df['job_sector']!='Transport and logistics')&(RetailBase_df['job_sector']!='Hospitality and events management')&(RetailBase_df['job_sector']!='Teaching and education')&(RetailBase_df['job_sector']!='Retail')&(RetailBase_df['job_sector']!='Law enforcement and security')&(RetailBase_df['job_sector']!='Other')&(RetailBase_df['job_sector']!='Creative arts and design')&(RetailBase_df['job_sector']!='Leisure, sports and tourism'), 'Job_sector_BinB'] = 0

RetailBase_df.loc[(RetailBase_df['job_sector']=='Environment and agriculture')|(RetailBase_df['job_sector']=='Real Estate')|(RetailBase_df['job_sector']=='Law')|(RetailBase_df['job_sector']=='Sales')|(RetailBase_df['job_sector']=='Construction')|(RetailBase_df['job_sector']=='Accountancy, banking and finance')|(RetailBase_df['job_sector']=='Public services and administration')|(RetailBase_df['job_sector']=='Business, consulting and management')|(RetailBase_df['job_sector']=='Media and internet')|(RetailBase_df['job_sector']=='Health-care')|(RetailBase_df['job_sector']=='Transport and logistics')|(RetailBase_df['job_sector']=='Hospitality and events management')|(RetailBase_df['job_sector']=='Teaching and education')|(RetailBase_df['job_sector']=='Retail')|(RetailBase_df['job_sector']=='Law enforcement and security')|(RetailBase_df['job_sector']=='Other')|(RetailBase_df['job_sector']=='Creative arts and design')|(RetailBase_df['job_sector']=='Leisure, sports and tourism'), 'Job_sector_BinC'] = 0
RetailBase_df.loc[(RetailBase_df['job_sector']!='Environment and agriculture')&(RetailBase_df['job_sector']!='Real Estate')&(RetailBase_df['job_sector']!='Law')&(RetailBase_df['job_sector']!='Sales')&(RetailBase_df['job_sector']!='Construction')&(RetailBase_df['job_sector']!='Accountancy, banking and finance')&(RetailBase_df['job_sector']!='Public services and administration')&(RetailBase_df['job_sector']!='Business, consulting and management')&(RetailBase_df['job_sector']!='Media and internet')&(RetailBase_df['job_sector']!='Health-care')&(RetailBase_df['job_sector']!='Transport and logistics')&(RetailBase_df['job_sector']!='Hospitality and events management')&(RetailBase_df['job_sector']!='Teaching and education')&(RetailBase_df['job_sector']!='Retail')&(RetailBase_df['job_sector']!='Law enforcement and security')&(RetailBase_df['job_sector']!='Other')&(RetailBase_df['job_sector']!='Creative arts and design')&(RetailBase_df['job_sector']!='Leisure, sports and tourism'), 'Job_sector_BinC'] = 1

#mean_bene_country
RetailBase_df.mean_bene_country.value_counts()

RetailBase_df.loc[RetailBase_df['mean_bene_country']=='India', 'Bene_Cntry_India'] = 1
RetailBase_df.loc[RetailBase_df['mean_bene_country']!='India', 'Bene_Cntry_India'] = 0

RetailBase_df.loc[RetailBase_df['mean_bene_country']=='Australia', 'Bene_Cntry_Australia'] = 1
RetailBase_df.loc[RetailBase_df['mean_bene_country']!='Australia', 'Bene_Cntry_Australia'] = 0

RetailBase_df.loc[RetailBase_df['mean_bene_country']=='Singapore', 'Bene_Cntry_Singapore'] = 1
RetailBase_df.loc[RetailBase_df['mean_bene_country']!='Singapore', 'Bene_Cntry_Singapore'] = 0

RetailBase_df.loc[(RetailBase_df['mean_bene_country']=='Singapore')|(RetailBase_df['mean_bene_country']=='India')|(RetailBase_df['mean_bene_country']=='Australia'), 'Bene_Cntry_Other'] = 0
RetailBase_df.loc[(RetailBase_df['mean_bene_country']!='Singapore')&(RetailBase_df['mean_bene_country']!='India')&(RetailBase_df['mean_bene_country']!='Australia'), 'Bene_Cntry_Other'] = 1

#mean_ccy
RetailBase_df.mean_ccy.value_counts()
RetailBase_df.loc[RetailBase_df['mean_ccy']=='INR', 'Mean_Ccy_INR'] = 1
RetailBase_df.loc[RetailBase_df['mean_ccy']!='INR', 'Mean_Ccy_INR'] = 0

RetailBase_df.loc[RetailBase_df['mean_ccy']=='AUD', 'Mean_Ccy_AUD'] = 1
RetailBase_df.loc[RetailBase_df['mean_ccy']!='AUD', 'Mean_Ccy_AUD'] = 0

RetailBase_df.loc[RetailBase_df['mean_ccy']=='SGD', 'Mean_Ccy_SGD'] = 1
RetailBase_df.loc[RetailBase_df['mean_ccy']!='SGD', 'Mean_Ccy_SGD'] = 0

RetailBase_df.loc[(RetailBase_df['mean_ccy']=='SGD')|(RetailBase_df['mean_bene_country']=='INR')|(RetailBase_df['mean_bene_country']=='AUD'), 'Mean_Ccy_Other'] = 0
RetailBase_df.loc[(RetailBase_df['mean_ccy']!='SGD')&(RetailBase_df['mean_bene_country']!='INR')&(RetailBase_df['mean_bene_country']!='AUD'), 'Mean_Ccy_Other'] = 1

###State
RetailBase_df.state.value_counts()

RetailBase_df.loc[RetailBase_df['state']=='KL', 'KL'] = 1
RetailBase_df.loc[RetailBase_df['state']!='KL', 'KL'] = 0

RetailBase_df.loc[RetailBase_df['state']=='Selangor', 'Selangor'] = 1
RetailBase_df.loc[RetailBase_df['state']!='Selangor', 'Selangor'] = 0

RetailBase_df.loc[RetailBase_df['state']=='Johor', 'Johor'] = 1
RetailBase_df.loc[RetailBase_df['state']!='Johor', 'Johor'] = 0

RetailBase_df.loc[RetailBase_df['state']=='Penang', 'Penang'] = 1
RetailBase_df.loc[RetailBase_df['state']!='Penang', 'Penang'] = 0

RetailBase_df.loc[(RetailBase_df['state']!='KL')&(RetailBase_df['state']!='Selangor')&(RetailBase_df['state']!='Johor')&(RetailBase_df['state']!='Penang'), 'StateOther'] = 1
RetailBase_df.loc[(RetailBase_df['state']=='KL')|(RetailBase_df['state']=='Selangor')|(RetailBase_df['state']=='Johor')|(RetailBase_df['state']=='Penang'), 'StateOther'] = 0


#Making a new Dataset with dependent and independent variables for existing users
Dataset=RetailBase_df[['SensitivityTag', 'coupon_amount_myr','coupon_used','Indian','Malaysian','NationalityOther','Gender_Final','Job_sector_BinA','Job_sector_BinB','Job_sector_BinC','Bene_Cntry_India','Bene_Cntry_Australia','Bene_Cntry_Singapore','Bene_Cntry_Other','Mean_Ccy_INR','Mean_Ccy_AUD','Mean_Ccy_SGD','Mean_Ccy_Other','risk','days_from_last_transx','orders','total_volume','no_of_bene','age','KL','Selangor','Johor','Penang','StateOther']]

#For New Users
Dataset_new=RetailBase_df[['SensitivityTag','Indian','Malaysian','NationalityOther','Gender_Final','Job_sector_BinA','Job_sector_BinB','Job_sector_BinC','risk','age','KL','Selangor','Johor','Penang','StateOther']]
for col in Dataset.columns:
    print(col)
    

#X and Y
X=Dataset.iloc[:,1:].values
y=Dataset.iloc[:,0].values
 
X_new=Dataset_new.iloc[:,1:].values
y_new=Dataset_new.iloc[:,0].values


#Test Train Split
X_train, X_test, y_train, y_test =train_test_split(X, y,test_size=0.3, random_state=0)
X_new_train, X_new_test, y_new_train, y_new_test =train_test_split(X_new, y_new,test_size=0.3, random_state=0)

#Modelling for existing customers
model = XGBClassifier(
 learning_rate =0.1,
 n_estimators=50,
 max_depth=5,
 min_child_weight=1,
 gamma=0.3)
model.fit(X_train, y_train)
y_pred_train=model.predict(X_train)
print(y_pred_train)
accuracy= accuracy_score(y_pred_train, y_train)
print(accuracy*100)

#Testing
y_pred_test=model.predict(X_test)
accuracy= accuracy_score(y_pred_test, y_test)
print(accuracy*100)


#Modelling for new customers
model_new = XGBClassifier(
 learning_rate =0.1,
 n_estimators=50,
 max_depth=5,
 min_child_weight=1,
 gamma=0.3)
model_new.fit(X_new_train, y_new_train)
y_new_pred_train=model_new.predict(X_new_train)
print(y_new_pred_train)
accuracy= accuracy_score(y_new_pred_train, y_new_train)
print(accuracy*100)

#Testing
y_new_pred_test=model_new.predict(X_new_test)
accuracy= accuracy_score(y_new_pred_test, y_new_test)
print(accuracy*100)
#print(model.feature_importances_)

#Predictions FOR NEW CUSTOMERS
New_Customers=pd.read_csv('retailusers_df.csv', encoding="unicode_escape")
New_Customers=New_Customers.drop(New_Customers[New_Customers['has_transacted']==1].index)

New_Customers=New_Customers[['user_id',  'nationality', 'gender', 'job_sector', 'risk', 'days_from_last_transx', 'age', 'state']]

###Nationality
New_Customers.nationality.value_counts()

New_Customers.loc[New_Customers['nationality']=='Indian', 'Indian'] = 1
New_Customers.loc[New_Customers['nationality']!='Indian', 'Indian'] = 0

New_Customers.loc[New_Customers['nationality']=='Malaysian', 'Malaysian'] = 1
New_Customers.loc[New_Customers['nationality']!='Malaysian', 'Malaysian'] = 0

New_Customers.loc[(New_Customers['nationality']!='Indian')&(New_Customers['nationality']!='Malaysian'), 'NationalityOther'] = 1
New_Customers.loc[(New_Customers['nationality']=='Indian')|(New_Customers['nationality']=='Malaysian'), 'NationalityOther'] = 0

###Gender 
New_Customers.gender.value_counts()

New_Customers.loc[New_Customers['gender']=='Male', 'Gender_Final'] = 1
New_Customers.loc[New_Customers['gender']=='Female', 'Gender_Final'] = 0

###job_sector
New_Customers.job_sector.value_counts()

New_Customers.loc[New_Customers['job_sector']=='Property and construction', 'job_sector'] = 'Construction'

New_Customers.job_sector.value_counts()

New_Customers.loc[(New_Customers['job_sector']=='Environment and agriculture')|(New_Customers['job_sector']=='Real Estate')|(New_Customers['job_sector']=='Law')|(New_Customers['job_sector']=='Sales')|(New_Customers['job_sector']=='Construction'), 'Job_sector_BinA'] = 1
New_Customers.loc[(New_Customers['job_sector']!='Environment and agriculture')&(New_Customers['job_sector']!='Real Estate')&(New_Customers['job_sector']!='Law')&(New_Customers['job_sector']!='Sales')&(New_Customers['job_sector']!='Construction'), 'Job_sector_BinA'] = 0

New_Customers.loc[(New_Customers['job_sector']=='Accountancy, banking and finance')|(New_Customers['job_sector']=='Public services and administration')|(New_Customers['job_sector']=='Business, consulting and management')|(New_Customers['job_sector']=='Media and internet')|(New_Customers['job_sector']=='Health-care')|(New_Customers['job_sector']=='Transport and logistics')|(New_Customers['job_sector']=='Hospitality and events management')|(New_Customers['job_sector']=='Teaching and education')|(New_Customers['job_sector']=='Retail')|(New_Customers['job_sector']=='Law enforcement and security')|(New_Customers['job_sector']=='Other')|(New_Customers['job_sector']=='Creative arts and design')|(New_Customers['job_sector']=='Leisure, sports and tourism'), 'Job_sector_BinB'] = 1
New_Customers.loc[(New_Customers['job_sector']!='Accountancy, banking and finance')&(New_Customers['job_sector']!='Public services and administration')&(New_Customers['job_sector']!='Business, consulting and management')&(New_Customers['job_sector']!='Media and internet')&(New_Customers['job_sector']!='Health-care')&(New_Customers['job_sector']!='Transport and logistics')&(New_Customers['job_sector']!='Hospitality and events management')&(New_Customers['job_sector']!='Teaching and education')&(New_Customers['job_sector']!='Retail')&(New_Customers['job_sector']!='Law enforcement and security')&(New_Customers['job_sector']!='Other')&(New_Customers['job_sector']!='Creative arts and design')&(New_Customers['job_sector']!='Leisure, sports and tourism'), 'Job_sector_BinB'] = 0

New_Customers.loc[(New_Customers['job_sector']=='Environment and agriculture')|(New_Customers['job_sector']=='Real Estate')|(New_Customers['job_sector']=='Law')|(New_Customers['job_sector']=='Sales')|(New_Customers['job_sector']=='Construction')|(New_Customers['job_sector']=='Accountancy, banking and finance')|(New_Customers['job_sector']=='Public services and administration')|(New_Customers['job_sector']=='Business, consulting and management')|(New_Customers['job_sector']=='Media and internet')|(New_Customers['job_sector']=='Health-care')|(New_Customers['job_sector']=='Transport and logistics')|(New_Customers['job_sector']=='Hospitality and events management')|(New_Customers['job_sector']=='Teaching and education')|(New_Customers['job_sector']=='Retail')|(New_Customers['job_sector']=='Law enforcement and security')|(New_Customers['job_sector']=='Other')|(New_Customers['job_sector']=='Creative arts and design')|(New_Customers['job_sector']=='Leisure, sports and tourism'), 'Job_sector_BinC'] = 0
New_Customers.loc[(New_Customers['job_sector']!='Environment and agriculture')&(New_Customers['job_sector']!='Real Estate')&(New_Customers['job_sector']!='Law')&(New_Customers['job_sector']!='Sales')&(New_Customers['job_sector']!='Construction')&(New_Customers['job_sector']!='Accountancy, banking and finance')&(New_Customers['job_sector']!='Public services and administration')&(New_Customers['job_sector']!='Business, consulting and management')&(New_Customers['job_sector']!='Media and internet')&(New_Customers['job_sector']!='Health-care')&(New_Customers['job_sector']!='Transport and logistics')&(New_Customers['job_sector']!='Hospitality and events management')&(New_Customers['job_sector']!='Teaching and education')&(New_Customers['job_sector']!='Retail')&(New_Customers['job_sector']!='Law enforcement and security')&(New_Customers['job_sector']!='Other')&(New_Customers['job_sector']!='Creative arts and design')&(New_Customers['job_sector']!='Leisure, sports and tourism'), 'Job_sector_BinC'] = 1


###State
New_Customers.state.value_counts()

New_Customers.loc[New_Customers['state']=='KL', 'KL'] = 1
New_Customers.loc[New_Customers['state']!='KL', 'KL'] = 0

New_Customers.loc[New_Customers['state']=='Selangor', 'Selangor'] = 1
New_Customers.loc[New_Customers['state']!='Selangor', 'Selangor'] = 0

New_Customers.loc[New_Customers['state']=='Johor', 'Johor'] = 1
New_Customers.loc[New_Customers['state']!='Johor', 'Johor'] = 0

New_Customers.loc[New_Customers['state']=='Penang', 'Penang'] = 1
New_Customers.loc[New_Customers['state']!='Penang', 'Penang'] = 0

New_Customers.loc[(New_Customers['state']!='KL')&(New_Customers['state']!='Selangor')&(New_Customers['state']!='Johor')&(New_Customers['state']!='Penang'), 'StateOther'] = 1
New_Customers.loc[(New_Customers['state']=='KL')|(New_Customers['state']=='Selangor')|(New_Customers['state']=='Johor')|(New_Customers['state']=='Penang'), 'StateOther'] = 0


#Making a new Dataset with dependent and independent variables for existing users
#Dataset=RetailBase_df[['SensitivityTag', 'coupon_amount_myr','coupon_used','Indian','Malaysian','NationalityOther','Gender_Final','Job_sector_BinA','Job_sector_BinB','Job_sector_BinC','Bene_Cntry_India','Bene_Cntry_Australia','Bene_Cntry_Singapore','Bene_Cntry_Other','Mean_Ccy_INR','Mean_Ccy_AUD','Mean_Ccy_SGD','Mean_Ccy_Other','risk','days_from_last_transx','orders','total_volume','no_of_bene','age','KL','Selangor','Johor','Penang','StateOther']]
#For New Users
Dataset_new=New_Customers[['Indian','Malaysian','NationalityOther','Gender_Final','Job_sector_BinA','Job_sector_BinB','Job_sector_BinC','risk','age','KL','Selangor','Johor','Penang','StateOther']]
for col in Dataset_new.columns:
    print(col)

'''Dataset.coupon_amount_myr.value_counts()
Dataset.coupon_amount_myr.value_counts()
Dataset.coupon_amount_myr.value_counts()'''

#X and Y
X_new_prediction=Dataset_new.iloc[:,:].values
y_new_prediction=model_new.predict(X_new_prediction)

Prediction_new = pd.DataFrame({'SensitivityTag': y_new_prediction[:], 'Column2': X_new_prediction[:, 0]})

Prediction_new=pd.merge(New_Customers, Prediction_new, left_index=True, right_index=True, how='left')

Prediction_new.to_csv('PSPredictionforNewCustomers.csv')

