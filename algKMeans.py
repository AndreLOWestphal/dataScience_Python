from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

x = [6,5,4,5,11,9,10,6,4,3,11,14,6,10,12]
y = [21,20,19,24,22,17,23,16,23,25,25,24,22,21,21]

dados = list(zip(x,y))
kmeans = KMeans(n_clusters=3, random_state=0)

kmeans.fit(dados)
print(dados)

plt.xlabel('x')
plt.ylabel('y')
plt.title('KMeans com 3 Clusters')
plt.scatter(x,y, c=kmeans.labels_)
plt.show()