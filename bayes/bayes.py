import pandas as pd

data=pd.read_csv('data.csv')

n=len(data)

b1=0 #for buy
b2=0 #for cant buy

for i in range(0,n):
    if(data['c'][i]==1):
        b1=b1+1
    else:
        b2=b2+1
        
#calculation for age

a1=0 #age <30 where they can buy
a11=0 #age <30 where they cannot buy
a2=0 #age 31-40 where they can buy
a22=0 #age 31-40 where they cannot buy
a3=0 # age >40 where they can buy
a33=0 # age >40 where they cannot buy

for i in range(0,n):
    if((data['Age'][i]== '<30') and (data['c'][i]==1)):
        a1=a1+1
    elif ((data['Age'][i]=='<30') and (data['c'][i]==0)):
        a11=a11+1
    elif((data['Age'][i]=='31-40') and (data['c'][i]==1)):
        a2=a2+1
    elif ((data['Age'][i]=='31-40') and (data['c'][i]==0)):
        a22=a22+1
    elif ((data['Age'][i]=='>40') and (data['c'][i]==1)):
        a3=a3+1
    else:
        a33=a33+1
        

a1=a1/b1 #probability of buy
a11=a11/b2 #probability of cannot buy

a2=a2/b1 #probability of buy
a22=a22/b2 #probability of cannot buy

a3=a3/b1 #probability of buy
a33=a33/b2 #probability of cannot buy

# calculation for income

i1=0 #income high and can buy
i11=0  #income high and cannot buy

i2=0 #income medium and can buy
i22=0 #income medium and cannot buy

i3=0 #income low and can buy
i33=0  #income low and cannot buy


for i in range(0,n):
    if((data['Income'][i]== 'High') and (data['c'][i]==1)):
        i1=i1+1
    elif ((data['Income'][i]=='High') and (data['c'][i]==0)):
        i11=i11+1
    elif((data['Income'][i]=='Medium') and (data['c'][i]==1)):
        i2=i2+1
    elif ((data['Income'][i]=='Medium') and (data['c'][i]==0)):
        i22=i22+1
    elif ((data['Income'][i]=='Low') and (data['c'][i]==1)):
        i3=i3+1
    else:
        i33=i33+1
        
i1=i1/b1 #probabability of income high who can buy
i11=i11/b2  #probabability of income high who cannot buy

i2=i2/b1 #probabability of income medium who can buy
i22=i22/b2 #probabability of income medium who cannot buy

i3=i3/b1 #probabability of income low who can buy
i33=i33/b2 #probabability of income low who cannot buy



#calculation for student

s1=0 #student and can buy
s11=0  #student and cannot buy

s2=0 #not student and can buy
s22=0 #not student and cannot buy




for i in range(0,n):
    if((data['Student'][i]== 'Yes') and (data['c'][i]==1)):
        s1=s1+1
    elif ((data['Student'][i]=='Yes') and (data['c'][i]==0)):
        s11=s11+1
    elif((data['Student'][i]=='No') and (data['c'][i]==1)):
        s2=s2+1
    else :
         s22=s22+1
         
s1=s1/b1 #probability of student who can buy
s11=s11/b2 #probability of student who cannot buy

s2=s2/b1 #probability of not student who can buy
s22=s22/b2 #probability of not student who cannot buy


#calculation for credit

c1=0 #credit excellent and can buy
c11=0  #credit excellent and cannot buy

c2=0 #credit fair and can buy
c22=0 #credit fair and cannot buy




for i in range(0,n):
    if((data['Credit'][i]== 'Excellent') and (data['c'][i]==1)):
        c1=c1+1
    elif ((data['Credit'][i]=='Excellent') and (data['c'][i]==0)):
        c11=c11+1
    elif((data['Credit'][i]=='Fair') and (data['c'][i]==1)):
        c2=c2+1
    else :
         c22=c22+1
         
c1=c1/b1 #probability of credit excellent who can buy
c11=c11/b2 #probability of credit excellent cannot buy

c2=c2/b1 #probability of credit fair who can buy
c22=c22/b2 #probability of credit fair who cannot buy


p1=b1/n #probability of buy
p2=b2/n #probability of cannot buy

s1=a1 * i2 * s1 * p1
s2=a11 * i22 * s11 * p2

s3=max(s1,s2)

if(s3==s1):
    print('AGE 30,INCOME MEDIUM,STUDENT-YES---CAN BUY')
else:
    print('AGE 30,INCOME MEDIUM,STUDENT-YES--CANNOT BUY')


    




