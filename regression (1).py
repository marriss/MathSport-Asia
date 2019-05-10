# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:13:06 2018

@author: Anshul
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset2=pd.read_excel('test_train_data_of features.xlsx')

x1=dataset2.iloc[0:637,10].values
y1=dataset2.iloc[0:637,4].values
y2=dataset2.iloc[0:637,7].values

plt.scatter(y1,x1,color='red')
plt.title('Fall of wicket between 11-15 overs vs avg run-rate')
plt.xlabel('Fall of wicket between 11-15 overs')
plt.ylabel('avg run-rate')
plt.show()


plt.scatter(y2,x1,color='red')
plt.title('Fall of wicket between 16-20 overs vs avg run-rate')
plt.xlabel('Fall of wicket between 16-20 overs')
plt.ylabel('avg run-rate')
plt.show()


import pandas as pd
import statsmodels.formula.api as sm
df = pd.DataFrame({"A": x1, "B": y1, "C": y2})
result = sm.ols(formula="A ~ B + C", data=df).fit()
print(result.params)

print (result.summary())