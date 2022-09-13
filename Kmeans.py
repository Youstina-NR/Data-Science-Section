import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X = -2* np.random.rand(20,2)
X1 = 0.1+ 2 * np.random.rand(10,2)


X[10:] = X1
print(X)
X = [[2,8]
    ,[2,5]
    ,[1,2]
    ,[5,8]
    ,[7,3]
    ,[6,4]
    ,[8,4]
    ,[4,7]]
X = np.array(X)
plt.scatter(X[ : , 0],X[:,1],s=150,c='b')
plt.show()

Kmean = KMeans(n_clusters=2)
Kmean.fit(X)

print(Kmean.cluster_centers_)

plt.scatter(X[:,0],X[:,1],s=150,c='b')
plt.scatter(Kmean.cluster_centers_[0][0],Kmean.cluster_centers_[0][1],s=200,c='g',marker='s')
plt.scatter(Kmean.cluster_centers_[1][0],Kmean.cluster_centers_[1][1],s=200,c='r',marker='s')
plt.show()
print(Kmean.labels_)
sample_test=np.array([[-3.0,-3.0],[3.0,4.0]])
sample_test=np.array([[2,3],[10,5]])
print(Kmean.predict(sample_test))