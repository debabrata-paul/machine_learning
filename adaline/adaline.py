import pandas as pd
import sys
                   
data=pd.read_csv('data_set.csv')
size=len(data)

w0=0 #bias
w1=0
w2=0
w3=0
w4=0
a=0.5

t2=[]
for i in range(0,size):
    t2.append(data['t'][i])

j=0
while True:
    t1=[]
    for i in range(0,size):
        t=[]
        t.append(w0)
        #print(data['x1'][i],data['x2'][i],data['x3'][i],data['x4'][i])
        t.append(data['x1'][i]*w1)
        t.append(data['x2'][i]*w2)
        t.append(data['x3'][i]*w3)
        t.append(data['x4'][i]*w4)
        #print('t',t)
        
        y=sum(t)
        if y>=0 :
            t1.append(1)
        else:
            t1.append(-1)
            
        #print('yin',y)
        #print('t-yin',data['t'][i]-y)
        
        w0=w0+(a*(data['t'][i]-y)) #bias
        w1=w1+(a*(data['t'][i]-y)*data['x1'][i])
        w2=w2+(a*(data['t'][i]-y)*data['x2'][i])
        w3=w3+(a*(data['t'][i]-y)*data['x3'][i])
        w4=w4+(a*(data['t'][i]-y)*data['x4'][i])
        
       # print('w0,w1,w2,w3,w4',w0,w1,w2,w3,w4)
    if t1==t2:
        print('MATCHED IN NO OF EPOCS IS::',j)
        sys.exit(0)
    j=j+1