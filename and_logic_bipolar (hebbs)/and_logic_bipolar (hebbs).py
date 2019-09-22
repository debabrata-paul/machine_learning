import pandas as pd
import numpy as nm
data=pd.read_csv('and_logic_bipolar (hebbs) data_set.csv')
#v=(data['x1'][0],data['x1'][0])
# print(v)

w=nm.zeros(3,dtype=int) 

size=data.shape[0]
for i in range(0,size):
    w1=nm.array([data['x1'][i],data['x0'][i],data['b'][i]])
    w=w + (w1 * data['y'][i])
    print('Wnew FOR SET ::',i+1,' IS :: ',w)

    
# CALCULATING AS Y= B + SUMOF(Wi*Xi) 
for i in range(0,4):
    w2=nm.array([(data['x1'][i] * w[0]),(data['x0'][i] * w[1]),(data['b'][i] * w[2])])
    w2=sum(w2) + data['b'][i]
    if w2>0:
        print('SET ',i+1,'IS :: x1')
    else:
        print('SET ',i+1,'IS :: x0')
    
