import pandas as pd


data=pd.read_csv('data_set.csv')
size=len(data)

j=size-1
c1=[3,4]

size=len(data)
d1=[] #distance from cluster c1
d2=[] #distance from cluster c2
#d22=[]

c2=[data['x'][j],data['y'][j]]
for i in range(0,6) :
    c3=c1[0] - data['x'][i]
    c3=abs(c3) + abs(c1[1] - data['y'][i])
    d1.append(c3)
    c3=c2[0] - data['x'][i]
    c3=abs(c3) + abs(c2[1] - data['y'][i])
    d2.append(c3)
    
p1=[] #cluster points for p1
p2=[] #cluster points for p2

for i in range(0,6):    #comparing among the cluster which one is minimum
    t=min(d1[i],d2[i])
    if t==d1[i]:
        p1.append(t)
    else:
        p2.append(t)
    
store=c2 #storing the cluster

c4=sum(p1) #sum of cluster p1
c5=sum (p2) #sum of cluster p2
c7=c4+c5 #summing up the clusters
j=j-1

while j>=0 :
    c3=0
    c6=0
    d22=[]
    nc=[]
    p1=[]
    p2=[]
    c2=[data['x'][j],data['y'][j]]
    for i in range(0,6):
        c3=c2[0] - data['x'][i]
        c3=abs(c3) + abs(c2[1] - data['y'][i])
        d22.append(c3)
        
    for i in range(0,6):    #comparing among the cluster which one is minimum
        t=min(d22[i],d1[i])
        if t==d1[i]:
            p1.append(t)
        else:
            p2.append(t)    
    
        
    c6=(sum(p2) + sum(p1)) #sum of new clusters of d2 for comparing
    #print(c6)
    
    if c6<c7 : #comparing the clusters d2 with newly cluster d22
        print('Previous cluster c2 was::',store)
        nc=[data['x'][j],data['y'][j]]
        print("the new clusters c2 after updation::",nc)
        store=nc #storing the values to print previous cluster in next updation
        c7=c6
    j=j-1
    

    
        
    

        
    