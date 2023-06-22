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

#using seaborn jointplot to draw histogram and scatterplot
#create figure object
plt.figure()
sns.jointplot(data=data, x="y", y="z", height=6, ratio=3, marginal_ticks=True)
#save figure into a png
plt.savefig("DMV302T1a.png")