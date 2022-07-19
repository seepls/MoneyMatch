import pandas as pd
import numpy as np

one = pd.read_csv('BSESN.csv', encoding='unicode_escape')
two = pd.read_csv('MRPL.csv', encoding='unicode_escape')
three = pd.read_csv('RELIANCE.csv', encoding='unicode_escape')

result = pd.merge(one, two, on='Date',how='left')
result.to_csv('resultFinal2.csv')
               

#lEFT bSESN
MRPL
RELIANCE 

