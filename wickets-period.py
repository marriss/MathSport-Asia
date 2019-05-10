



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
y=np.zeros((636,3))
for i in range(1,637):
    w11=0
    w12=0
    w21=0
    for k in range(len(dataset)):
        if(dataset["match_id"][k]==i):
            if(dataset["inning"][k]==1):
                if(dataset["over"][k]>=1 and dataset["over"][k]<=6 and dataset["dismissal_kind"][k]!=0):
                    w11=w11+1  
                if(dataset["over"][k]>=7 and dataset["over"][k]<=10 and dataset["dismissal_kind"][k]!=0):
                    w12=w12+1
                if(dataset["over"][k]>=11 and dataset["over"][k]<=15 and dataset["dismissal_kind"][k]!=0):
                    w21=w21+1   
    y[i-1][0]=w11
    y[i-1][1]=w12
    y[i-1][2]=w21