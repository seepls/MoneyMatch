import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

business_transx_data = pd.read_csv('ac_margin.csv',engine='python')
business_transx_data['margin_ac_client']=pd.to_numeric(business_transx_data['margin_ac_client'])
print(business_transx_data.dtypes())
business_transx_data['lognorm'] = np.log(business_transx_data['margin_ac_client'])
plt.hist(business_transx_data.lognorm, bins=20)
plt.ylabel('frequency')
plt.xlabel('Margin according to client distribution')
plt.show()



