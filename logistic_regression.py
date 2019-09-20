import pandas as pd
import math
data=pd.read_csv('logistic_regression_data_set.csv')
# print(data)

size=data.shape[0]
 #print(size) # SIZE OF ARRAY


b0=0
b1=0
b2=0
print('INITIAL b0=',b0)
print('INITIAL b1=',b1)
print('INITIAL b2=',b2)

y=(b0 * 1) + (b1 * data['x1'][0]) + (b2 *  data['x2'][0])
pr=(1/(1+math.exp(-y)))
# print(pr)

print('INITIAL PREDICTION=',pr)

for i in range(0,size):
    print('FOR I=',i+1)
    b0=b0 + 0.3*(y-pr)*pr*(1-pr)*1
    print('b0=',b0)
    b1=b1 + 0.3*(y-pr)*pr*(1-pr)*data['x1'][i]
    print('b1=',b1)
    b2=b2 + 0.3*(y-pr)*pr*(1-pr)*data['x2'][i]
    print('b2=',b2)
    y=(b0 * 1) + (b1 * data['x1'][i]) + (b2 *  data['x2'][i])
    print('y=',y)
    pr=(1/(1+math.exp(-y)))
    print('predicted=',pr)
    
    
