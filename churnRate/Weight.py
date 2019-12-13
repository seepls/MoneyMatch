import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

features = ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip',   'callcard', 'wireless','churn']
churn_df = pd.read_csv("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/ChurnData.csv")
churn_df = churn_df[features]
churn_df['churn'] = churn_df['churn'].astype('int')
X_normal = preprocessing.StandardScaler().fit_transform(churn_df.drop('churn',axis=1).to_numpy())
y = churn_df['churn']

##split model
X_train, X_test, y_train, y_test = train_test_split( X_normal, y, test_size=0.2, random_state=4)


LR = LogisticRegression(C=0.001, solver='liblinear').fit(X_train,y_train)
print(classification_report(LR.predict(X_test),y_test))
for f,w in zip(features,LR.coef_[0]):
    print("Feature - {} has a weight of - {:.5f}".format(f,w))

>>
0.625
Feature - tenure has a weight of - -0.02402
Feature - age has a weight of - -0.01687
Feature - address has a weight of - -0.01598
Feature - income has a weight of - -0.00497
Feature - ed has a weight of - 0.01042
Feature - employ has a weight of - -0.01900
Feature - equip has a weight of - 0.02367
Feature - callcard has a weight of - -0.02006
Feature - wireless has a weight of - 0.02094