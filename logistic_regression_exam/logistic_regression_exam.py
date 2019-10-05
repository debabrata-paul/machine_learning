import pandas as pd
import numpy as np
import math
import sys



data=pd.read_csv('data_set.csv')
size=len(data)
b0=0 #bias
b1=0 #sl
b2=0 #sw
b3=0 #pl
b4=0 #pw


yreal=data['c']
li1=[]

for i in range(0,size):
    li1.append(yreal[i])

    
ypred=np.zeros(size)
ep=0

while True :
    acc=0 #ACCURACY
    for i in range(0,size):
        acc=0
        ypred[i]=(b0 *1) +(b1 * data['sl'][i]) + (b2 * data['sw'][i]) + (b3 * data['pl'][i]) + (b4 * data['pw'][i]) 
        pr=(1/(1+ math.exp(-ypred[i])))
        if ypred[i] < 2:
            ypred[i]=0
        elif (ypred[i] > 2 and ypred[i] < 5) :
            ypred[i]=1
        else :
            ypred[i]=2
        
        b0=b0+ (0.3*(yreal[i]-pr)*pr*(1-pr)*1)
        b1=b1+ (0.3*(yreal[i]-pr)*pr*(1-pr)*data['sl'][i])
        b2=b2+ (0.3*(yreal[i]-pr)*pr*(1-pr)*data['sw'][i])
        b3=b3+ (0.3*(yreal[i]-pr)*pr*(1-pr)*data['pl'][i])
        b4=b4+ (0.3*(yreal[i]-pr)*pr*(1-pr)*data['pw'][i])
        #b5=b5+ (0.3*(yreal[i]-pr)*pr*(1-pr)*data['b'][i])
        
    for i in range(0,size):
        if ypred[i]==yreal[i]:
            acc=acc+1
    acc=acc/size *100
    print("ACCURACY IS:: %.2f" %acc,'%')
    print(ypred)
    
    size2=len(ypred)
    
    li2=[]
    
    for i in range(0,size2):
        li2.append(ypred[i])
    
    if li2==li1:
        print('PREDICTION IS SUCCESSFUL ON ITERATION::',ep)
        sys.exit(0)
    else:
        print('PREDICTION IS NOT SUCCESSFUL')
        
    ep=ep+1



    
        
        