import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Downloads\Mall_Customers.csv")
print(data.isnull().sum()) 
# data.head()
# data.info()
# data.shape()

#list created for clustering
x = data.iloc[:,[3,4]].values
wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++',n_init=10, random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print(wcss)

#elbow graph
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), wcss, marker='*')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

Kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
y=Kmeans.fit_predict(x)
print(y)

cluster=0,1,2,3,4

plt.figures(figsize=(8,8))
plt.scatter(x[y==0,0],x[y==0,1],s=50,c='blue',label='cluster 0')#s= size
plt.scatter(x[y==1,0],x[y==1,1],s=50,c='green',label='cluster 1')
plt.scatter(x[y==2,0],x[y==2,1],s=50,c='pink',label='cluster 2')
plt.scatter(x[y==3,0],x[y==3,1],s=50,c='black',label='cluster 3')
plt.scatter(x[y==4,0],x[y==4,1],s=50,c='gray',label='cluster 4')

#centeroids
plt.scatter(Kmeans.cluster_centers_[:,0],Kmeans.cluster_centers_[:,1],s=100,c='red',label='centeroids')
plt.title('customer group')
plt.title('Annual income')
plt.ylabel('spending score(1-100)')
plt.legend()
plt.show()



