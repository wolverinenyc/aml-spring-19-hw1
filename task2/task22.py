from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import savefig

iris = load_iris()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(
        iris['data'],iris['target'], random_state=0)

'''
# replicate this set of tables using only matplotlib and numpy
iris_df = pd.DataFrame(X_train,columns=iris.feature_names)
grr = pd.scatter_matrix(iris_df,c=y_train,figsize=(15,15),marker='o',
                        hist_kwds={'bins':20},s=60,alpha=0.8,cmap='rainbow')
'''

#   PROBLEM WITH THIS IS THAT THE HISTOGRAM HEIGHTS ARE TOO LARGE AND REALLY
#   NEED TO BE DISPLAYED ON A WIDER Y-RANGE. BUT THE GRAPHS IN THE BOOK SHOW THESE
#   AS THE LABELS/TICKS FOR EACH ROW :/ 

y_train_c = np.where(y_train==0,'b','')
y_train_c = np.where(y_train==1,'r',y_train_c)
y_train_c = np.where(y_train==2,'g',y_train_c)


fig,ax = plt.subplots(4,4,figsize=(15,15),sharex='col',sharey='row')
fig.subplots_adjust(wspace=0,hspace=0)

for i in range(0,4):
    ax[i,i].hist(X_train[:,i],bins=20)

for i in range(0,4):
    for j in range(0,4):
        if i==j:
            continue
        ax[j,i].scatter(X_train[:,i],X_train[:,j],c=y_train_c,marker='o', 
              s=60,alpha=0.8)
            
   
ax[0,0].set_xlim((4,8))
ax[0,0].set_xticks([x/10.0 for x in range(45,80,5)])
ax[1,1].set_xlim((1.8,5))
ax[1,1].set_xticks([x/10.0 for x in range(20,50,5)])
ax[2,2].set_xlim((0.8,8))
ax[2,2].set_xticks(list(range(1,8)))
ax[3,3].set_xlim((0,2.6))
ax[3,3].set_xticks([x/10.0 for x in range(0,30,5)])

ax[0,0].set_ylim((4,8))
ax[0,0].set_yticks([x/10.0 for x in range(45,80,5)])
ax[1,0].set_ylim((1.8,5))
ax[1,0].set_yticks([x/10.0 for x in range(20,50,5)])
ax[2,0].set_ylim((0.8,7))
ax[2,0].set_yticks(list(range(1,8)))
ax[3,0].set_ylim((0,2.6))
ax[3,0].set_yticks([x/10.0 for x in range(0,30,5)])

ax[3,0].set_xlabel('sepal length (cm)')
ax[3,1].set_xlabel('sepal width (cm)')
ax[3,2].set_xlabel('petal length (cm)')
ax[3,3].set_xlabel('petal width (cm)')

ax[0,0].set_ylabel('sepal length (cm)')
ax[1,0].set_ylabel('sepal width (cm)')
ax[2,0].set_ylabel('petal length (cm)')
ax[3,0].set_ylabel('petal width (cm)')

savefig('task22_iris.png', bbox_inches='tight')

