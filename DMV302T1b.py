#importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

#reading csv file without reading the first row so we can
#name the columns without affecting the data
data = pd.read_csv('DMV302_Assessment_3_Dataset1.csv', header = None)

#naming 3D data
data.columns = ['x', 'y', 'z']

x = data['x']
y = data['y']
z = data['z']

#perform kmeans clustering
kmeans = KMeans(n_clusters=3, n_init="auto").fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print(centroids)

#creating 3d scatterplot with matplotlib
fig = plt.figure(figsize = (12,12))

ax = fig.add_subplot(111, projection='3d')

#selecting datapoint from eachcluster
ax.scatter(x[labels == 0],y[labels == 0],z[labels == 0], s = 40 , color = '#dea5a4', label = "cluster 1")
ax.scatter(x[labels == 1],y[labels == 1],z[labels == 1], s = 40 , color = '#FDFD96', label = "cluster 2")
ax.scatter(x[labels == 2],y[labels == 2],z[labels == 2], s = 40 , color = '#77DD77', label = "cluster 3")

#naming the axis
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
#displaying legend 
ax.legend()
#saving fig to png
plt.savefig('DMV302T1b.png')