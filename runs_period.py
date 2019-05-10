# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:07:43 2018

@author: Puneet Garg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('data upto 2017.csv')
dataset=dataset.fillna(0)
len(dataset)
x=np.zeros((636,3))
for i in range(1,637):
    run11=0
    run12=0
    run21=0
    for k in range(len(dataset)):
        if(dataset["match_id"][k]==i):
            if(dataset["inning"][k]==1):
                if(dataset["over"][k]>=1 and dataset["over"][k]<=6):
                    run11=run11+dataset["total_runs"][k]   
                if(dataset["over"][k]>=7 and dataset["over"][k]<=10):
                    run12=run12+dataset["total_runs"][k]
                if(dataset["over"][k]>=11 and dataset["over"][k]<=15):
                    run21=run21+dataset["total_runs"][k] 
    x[i-1][0]=run11
    x[i-1][1]=run12
    x[i-1][2]=run21
     
