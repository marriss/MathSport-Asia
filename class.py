# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:36:08 2018

@author: Anshul
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_excel('total runs of both innings.xlsx')
x=dataset.iloc[:,0].values
p1=0
p2=0
p3=0
p4=0
p5=0
p6=0

i=0
for i in range(len(x)):
    if(x[i]<=120):
        p1=p1+1
    if(x[i]>120 and x[i]<=140):
        p2=p2+1
    if(x[i]>140 and x[i]<=160):
        p3=p3+1
    if(x[i]>160 and x[i]<=180):
        p4=p4+1
    if(x[i]>180 and x[i]<=200):
        p5=p5+1
    if(x[i]>200):
        p6=p6+1
       
p1/636
p2/636
p3/636
p4/636
p5/636
p6/636
dataset1=pd.read_excel('prob of final score.xlsx')
i=0
for i in range(len(dataset1)):
    if(dataset1["scorei1"][i]<=120):
        dataset1["class"][i]=1
    if(dataset1["scorei1"][i]>120 and dataset1["scorei1"][i]<=140):
        dataset1["class"][i]=2
    if(dataset1["scorei1"][i]>140 and dataset1["scorei1"][i]<=160):
        dataset1["class"][i]=3
    if(dataset1["scorei1"][i]>160 and dataset1["scorei1"][i]<=180):
        dataset1["class"][i]=4
    if(dataset1["scorei1"][i]>180 and dataset1["scorei1"][i]<=200):
        dataset1["class"][i]=5
    if(dataset1["scorei1"][i]>200):
        dataset1["class"][i]=6