import pandas as pd
import math

data=pd.read_csv('knn.csv')

s1=len(data)

#k=[data['out'][9],data['temp'][9],data['hum'][9],data['windy'][9]]
k=[15,77,87,-1] #1st set windy (true=1/false=-1)

#k=[20,65,86,1] #2nd set

li2=[]
li3=[]
for i in range(0,s1):
    s=(data['out'][i]-k[0])**2 + (data['temp'][i] -k[1])**2 + (data['hum'][i] - k[2])**2 + (data['windy'][i]-k[3])**2
    s=math.sqrt(s)
    li2.append(s)
    
li3=li2 #storing the value

li3.sort() #sorting in order


li4=[]
for i in range(0,5): #storing the 5 values in the classes
    li4.append(li3[i])

m=0 #yes 
n=0 #no
for i in range(0,5):
    for j in range(0,s1):
        if(li4[i]==li2[j]) : #comparing the sorted value with the unsorted value to acheive index
            if(data['play'][j]==1) :
                m=m+1
                break
            else :
                n=n+1
                break
print('Probability of getting Yes::',m/5)
print('Probability of getting No::',n/5)


