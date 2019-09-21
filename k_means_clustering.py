import pandas as pd
import sys


data=pd.read_csv('k_means_clustering_data_set.csv')

c1=data['x'][0]
c2=data['x'][7]
c3=data['x'][8]

n=len(data)
k=1

def kmeans(c1,c2,c3,k):
    li1=[]
    li2=[]
    li3=[]
    for i in range(0,n):
        cal1=(c1 - data['x'][i]) **2
        li1.append(cal1)
        cal2=(c2 - data['x'][i]) **2
        li2.append(cal2)
        cal3=(c3 - data['x'][i]) **2
        li3.append(cal3)
        
    cul1=[]
    cul2=[]
    cul3=[]
    for i in range(0,15): #CHECKING WHICH ONE IS MINIMUM
        if(li1[i] < li2[i] and li1[i] < li3[i]):
            cul1.append(data['x'][i])
        elif(li2[i] < li1[i] and li2[i] < li3[i]):
            cul2.append(data['x'][i])
        else:
             cul3.append(data['x'][i])
    
    print('\n',k,' ITERATION')
        
    # AVERAGE OF CLUSTER1   
    s1=sum(cul1)
    s1=s1/(len(cul1))
    print('\ncluster is :: ',s1,' AND POINTS ARE :: ',cul1) #PRINTING OF CLUSTERS1
    #AVERAGE FOR CLUSTER2
    s2=sum(cul2)
    s2=s2/(len(cul2))
    print('\ncluster is :: ',s2,' AND POINTS ARE :: ',cul2) #PRINTING OF CLUSTER 2
    #AVERAGE FOR CLUSTER3
    s3=sum(cul3)
    s3=s3/(len(cul3)) 
    print('\ncluster is :: ',s3,' AND POINTS ARE :: ',cul3) #PRINTING OF CLUSTER3 
    
    #EXIT CONDITION
    if(s1==c1 and s2==c2 and s3==c3):
        print('\nNO DIFFERENCE IN CLUSTER FOUND...EXITTING...!')
        sys.exit(0)
    c1=s1
    c2=s2
    c3=s3      
    k=k+1 
    kmeans(c1,c2,c3,k)
    
kmeans(c1,c2,c3,k)

        
    

    