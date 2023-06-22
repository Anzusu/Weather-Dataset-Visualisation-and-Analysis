#importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px
import seaborn as sns

#import csv file
data = pd.read_csv('DMV302_Assessment_3_Dataset2.csv', header = None)

#name each data columns for ease of acess
data.columns = ['Date', 'Average_Temp', 'Min_Temp', 'Max_Temp', 'Av_Min_Temp_1901', 'Av_Max_Temp_1901', 'Low_Temp_1901', 'High_Temp_1901', 'Act_Rain', 'Av_Rain_1901', 'High_Rain_1901']
#sort data in ascending order for animated scatterplot
data = data.sort_values(by='Average_Temp')

#animated scatterplot
fig = px.scatter(data, x = "Av_Min_Temp_1901", y = "Av_Max_Temp_1901", animation_frame = "Average_Temp",
                 animation_group = "Av_Rain_1901", size = "Av_Rain_1901", color="High_Rain_1901", hover_name="Date",
                 size_max =55, range_x=[0,80], range_y=[0,130])
fig.write_html("DMV302Tbanimationscatter.html")

#convert date time to numerical data for heatmap
data['Date'] = pd.to_datetime(data['Date'])
data['Date']= data['Date'].map(dt.datetime.toordinal)

#heatmap
plt.figure(figsize=(10, 10))
heatmap = sns.heatmap(data.corr(), vmin=1, vmax=-0.2, annot=True)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);
plt.savefig("DMV302TbHeatMap.png")

