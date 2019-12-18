import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
import numpy as np
from sklearn import metrics


df=pd.read_excel("C:/Users/hp.DEBABRATA/Desktop/New folder (2)/COMP_SALE.xlsx")
#print(df)

def datapreprocess(dataset):
    dataset=np.array(dataset)
    x=np.ndarray(shape=(dataset.shape[0],dataset.shape[1]-1),dtype=np.int32)
    y=np.zeros(dataset.shape[0])
    for i in range(dataset.shape[0]):
        if(dataset[i,0]=='<30'):
            x[i,0]=0
        elif(dataset[i,0]=='31 - 40'):
            x[i,0]=1
        elif(dataset[i,0]=='>40'):
             x[i,0]=2
        if(dataset[i,1]=='LOW'):
            x[i,1]=0
        elif(dataset[i,1]=='MEDIUM'):
            x[i,1]=1
        elif(dataset[i,1]=='HIGH'):
             x[i,1]=2
        if(dataset[i,2]=='YES'):
            x[i,2]=1
        elif(dataset[i,2]=='NO'):
            x[i,2]=0
        if(dataset[i,3]=='EXCELLENT'):
            x[i,3]=1
        elif(dataset[i,3]=='FAIR'):
            x[i,3]=0
        if(dataset[i,4]=='YES'):
            y[i]=1
        elif(dataset[i,4]=='NO'):
            y[i]=0
    return x,y


x,y=datapreprocess(df)
print(x,y)


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.01, random_state=1)

clf=DecisionTreeClassifier(criterion="entropy",max_features=2,min_samples_leaf=0.5)

clf=clf.fit(X_train,y_train)

#print(X_test)
s=np.array([[0,2,1,0]])
y_pred = clf.predict(s)
print(y_pred,y_test)


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

