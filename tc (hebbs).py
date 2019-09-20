import pandas as pd
import numpy as nm
data=pd.read_csv('tc (hebbs).csv')
w0=nm.zeros(10,dtype=int) #FOR CREATING ZERO ARRAY
size=data.shape[0]
t1=nm.empty(0,dtype=int)

for i in range(0,size-1):
    t1=nm.append(t1,data['t'][i])

c1=nm.empty(0,dtype=int)
for i in range(0,size-1):
    c1=nm.append(c1,data['c'][i])
 

#CALCULATING FOR T
wnew=w0 + (t1*data['t'][10])
print(wnew)

#CALCULATING FOR C
wnew=wnew + (c1 * data['c'][10])
print(wnew)

#CALCULATION FOR T (FORMULA)
tcal=nm.empty(0,dtype=int)
for i in range(0,size-1):
  tcal=nm.append(tcal,data['t'][i] * wnew[i])

tcal=sum(tcal) + data['t'][10] #wixi + bias value
if tcal > 0:
    print('VALUES OF T IS IN T')
else:
    print('VALUES OF T IS IN C')
    
#CALCULATION FOR C (FORMULA)
tcal=nm.empty(0,dtype=int)
for i in range(0,size-1):
  tcal=nm.append(tcal,data['c'][i] * wnew[i])
  
tcal=sum(tcal) + data['c'][10] #wixi + bias value
if tcal > 0:
    print('VALUES OF C IS IN T')
else:
    print('VALUES OF C IS IN C')
