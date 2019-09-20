n1=int(input('ENTER THE NO OF INPUTS::'))
li1=[]
li2=[]

print('ENTER THE AREAS::')
for i in range(0,n1):
	num=int(input())
	li1.append(num)

print('ENTER THE RENTS::')
for i in range(0,n1):
	num=int(input())
	li2.append(num)

#print(li1)
#print(li2)

store1=0
# SUMMATION OF AREA
for i in range(0,n1):
	store1=store1+li1[i]

store1=store1//n1 #mean of area

li3=[]  #(xi - x_)
for i in range(0,n1):
	num=li1[i]-store1
	li3.append(num)
	






store2=0
# SUMMATION OF RENT
for i in range(0,n1):
	store2=store2+li2[i]

store2=store2//n1 #mean of rent

li4=[] #(yi - y_)

for i in range(0,n1):
	num=li2[i]-store2
	li4.append(num)


li5=[]

store3=0 # summation of (xi - x_)(yi - y_)
for i in range(0,n1):
	num=li3[i] * li4[i]
	store3=store3+num

store4=0 # summation of (xi - x_)^2

for i in range(0,n1):
	num=li3[i] **2
	store4=store4+num


b1=store3/store4
print('b1 IS::',b1)

b0=store2 - (b1 * store1)
print('b0 IS::',b0)

num6=int(input('ENTER THE AREA TO PREDICT::'))

y1=b0 + (b1 * num6)

print('THE RENT IS:: ', y1)

ypred=[]

for i in range(0,n1):
	num=b0 + (b1 * li1[i])
	ypred.append(num)

print('ypred',ypred)

sst=0
for i in range(0,n1):
	num=li4[i] ** 2
	sst=sst + num

ssr=0
for i in range(0,n1):
	num=(ypred[i] - store2) **2
	ssr=ssr+num

print('ssr',ssr)
print('sst',sst)
rr=ssr/sst

print('R^2::',rr)	

 























