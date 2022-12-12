# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
"""
Q5) Calculate Mean, Median, Mode, Variance, Standard Deviation, Range & comment about the values / draw inferences, for the given dataset
"""

# _______________Q1 _____________________##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# load data 

df = pd.read_excel(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\Assignment_module02 (1).xlsx")
df.dtypes
df.columns
#df2 = df1['Points']
df.mean() #mean

df.median() # median
df.Points.mode() # Mode
df.Score.mode() # Mode
df.Weigh.mode() # Mode

df.var()
df.std()
df.describe()

Points_Range=df.Points.max()-df.Points.min()
Points_Range

Score_Range=df.Score.max()-df.Score.min()
Score_Range

Weigh_Range=df.Weigh.max()-df.Weigh.min()
Weigh_Range

f,ax=plt.subplots(figsize=(15,5))

plt.subplot(1,3,1)
plt.boxplot(df.Points)
plt.title('Points')
plt.subplot(1,3,2)
plt.boxplot(df.Score)
plt.title('Score')
plt.subplot(1,3,3)
plt.boxplot(df.Weigh)
plt.title('Weigh')
plt.show()

############ Q7 ###################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
x=pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])
name=['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P.Morgan & Co.','Lehman Brothers',
      'Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways',
      'Warner-Lambert']
x.mean()
x.std()
plt.hist(x)
stats.skew(x)
sns.boxplot(x)
# outlier

IQR = x.quantile(0.75) - x.quantile(0.25)
lower_limit = x.quantile(0.25) - (IQR * 1.5)
upper_limit = x.quantile(0.75) + (IQR * 1.5)

############### 1. Remove (let's trim the dataset) ################
# Trimming Technique
# let's flag the outliers in the data set
outliers_x = np.where(x > upper_limit, True, np.where(x < lower_limit, True, False))
sum(outliers_x)

x_trimmed = x.loc[~(outliers_x),]
x.shape, x_trimmed.shape

# let's explore outliers in the trimmed dataset
sns.boxplot(x_trimmed)
