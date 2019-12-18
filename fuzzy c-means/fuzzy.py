import random
import sys
d=[2,4,6,3,31,12,15,16,38,35,14,21,23,25,30]
#d=[3,7,10,17,18,20]

u1=[]
u2=[]
t1,t2=[],[]

for i in range(0,len(d)):
    u1.append(random.uniform(0.1,0.9))
    u2.append(1-u1[i])
    
c1,c2=0,0

u1_prev,u2_prev=[],[]
cent1,cent2=[],[]


for i in range(0,len(d)):
    t1.append(u1[i]**2 * d[i])
    t2.append(u1[i]**2)

c1=sum(t1)/sum(t2)

t1,t2=[],[]
for i in range(0,len(d)):
    t1.append(u2[i]**2 * d[i])
    t2.append(u2[i]**2)

c2=sum(t1)/sum(t2)
a1=[]

k=1
def fz(c1,c2,u1,u2,k,a1):
    a1=[]
    flag=0
    print(k)
    new_u1,new_u2=[],[]
    a1,a2=[],[]
    for i in range(0,len(d)):
        new_u1.append(1/(((abs(d[i]-c1)/abs(d[i]-c1))**2) +((abs(d[i]-c1)/abs(d[i]-c2))**2)))
        new_u2.append(1/(((abs(d[i]-c2)/abs(d[i]-c1))**2) +((abs(d[i]-c2)/abs(d[i]-c2))**2)))
    
    #print(new_u1)
    #print(new_u2)
    
    '''for i in range(0,len(d)):
        a1.append(new_u1[i]+new_u2[i])'''
        
    for i in range(0,len(d)):
        if( new_u1[i] - u1[i]< 0.01):
           if( new_u2[i] - u2[i]< 0.01):
            #print('u1',u1)
            #print('new_u1',new_u1)
            print('matched in ::',k)
            print(c1,c2)
            for i in range(0,len(d)):
                a1.append(new_u1[i]+new_u2[i])
            #print(a1)
            sys.exit(0)
        else:
            u1,u2=[],[]
            u1=new_u1
            u2=new_u2
            t1,t2=[],[]
            for i in range(0,len(d)):
                t1.append(new_u1[i]**2 * d[i])
                t2.append(new_u1[i]**2)
    
            c1=sum(t1)/sum(t2)
    
            t1,t2=[],[]
            for i in range(0,len(d)):
                t1.append(new_u2[i]**2 * d[i])
                t2.append(new_u2[i]**2)
    
            c2=sum(t1)/sum(t2)
            k=k+1
            fz(c1,c2,u1,u2,k,a1)
          
fz(c1,c2,u1,u2,k,a1)          
