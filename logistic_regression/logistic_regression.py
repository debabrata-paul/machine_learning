import pandas as pd
import numpy as np
import math
import sys
data=pd.read_csv('logistic_regression_data_set.csv')
# print(data)

size=data.shape[0]
 #print(size) # SIZE OF ARRAY



b0=0
b1=0
b2=0

yreal=data['y']
ypred=np.zeros(size)
epoch=0
while epoch < 5:
    acc=0
    for i in range(0,size):
        ypred[i]=(b0 * 1) + (b1 * data['x1'][i]) + (b2 *  data['x2'][i])
        print(ypred[i])
        pr=(1/(1+math.exp(-ypred[i])))
        if ypred[i] >=0.5:
            ypred[i]=1
        else :
            ypred[i]=0
        b0=b0 + (0.3*(yreal[i]-pr)*pr*(1-pr)*1)
        b1=b1 + (0.3*(yreal[i]-pr)*pr*(1-pr)*data['x1'][i])
        b2=b2 + (0.3*(yreal[i]-pr)*pr*(1-pr)*data['x2'][i])
            
    for i in range(yreal.shape[0]):
        if yreal[i] == ypred[i]:
            acc += 1
    acc = acc/yreal.shape[0]
    print(f'Accuracy:{acc}')
    epoch+=1
    
    print(ypred)
    print(b0,b1,b2)



        
            
            
        










    

    
    
    