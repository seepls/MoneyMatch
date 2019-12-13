
import pandas as pd

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

#Importing Data
Train_2=pd.read_csv('MERGED_NEW.csv',encoding = 'unicode_escape')
Train_3=Train_2[['SensitivityTag', 'user_id', 'purpose_of_transaction_new', 'nationality', 'amount', 'deposit_received']]

#OneHotEncoding
Train_3.loc[Train_3['purpose_of_transaction_new']=='Donation or Gifts', 'DonationOrGifts'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Donation or Gifts', 'DonationOrGifts'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Education', 'Education'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Education', 'Education'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Family Maintenance', 'FamilyMaintenance'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Family Maintenance', 'FamilyMaintenance'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Household Maintenance', 'HouseholdMaintenance'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Household Maintenance', 'HouseholdMaintenance'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Business/Investment', 'BusinessInvestment'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Business/Investment', 'BusinessInvestment'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Payment of bills', 'Paymentofbills'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Payment of bills', 'Paymentofbills'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Payment for goods and services', 'Paymentforgoodsandservices'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Payment for goods and services', 'Paymentforgoodsandservices'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Salary', 'Salary'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Salary', 'Salary'] = 0

Train_3.loc[Train_3['purpose_of_transaction_new']=='Purchase of property', 'Purchaseofproperty'] = 1
Train_3.loc[Train_3['purpose_of_transaction_new']!='Purchase of property', 'Purchaseofproperty'] = 0

#Nationality

Train_3.loc[Train_3['nationality']=='Indian', 'Indian'] = 1
Train_3.loc[Train_3['nationality']!='Indian', 'Indian'] = 0

Train_3.loc[Train_3['nationality']=='Malaysian', 'Malaysian'] = 1
Train_3.loc[Train_3['nationality']!='Malaysian', 'Malaysian'] = 0

Train_3.loc[Train_3['nationality']=='Other', 'NationalityOther'] = 1
Train_3.loc[Train_3['nationality']!='Other', 'NationalityOther'] = 0

#X and Y
X=Train_3.iloc[,5:].values
y=Train_3.iloc[,0].values


#Test Train Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X, y,test_size=0.2, random_state=0)


#Modelling
model = XGBClassifier(n_estimators=50)
model.fit(X_train, y_train)
y_pred_train=model.predict(X_train)
accuracy= accuracy_score(y_pred_train, y_train)
print(accuracy)

'''
#Testing
y_pred_test=model.predict(X_test[:,5:])
accuracy= accuracy_score(y_pred_test, y_test)
print(accuracy)
'''