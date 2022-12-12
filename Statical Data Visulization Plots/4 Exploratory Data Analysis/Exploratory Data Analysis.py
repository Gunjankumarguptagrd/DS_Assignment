# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:04:31 2022

@author: Gunjan
"""
"""
Problem Statements:
Q1) Calculate Skewness, Kurtosis using R/Python code & draw inferences on the following data.
Hint: [Insights drawn from the data such as data is normally distributed/not, outliers, measures like mean, median, mode, variance, std. deviation]
   a.   Cars speed and distance

"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
df = pd.read_csv("D:\DATA Science 360 DigiTMG\Self Study\Statical Data Visulization Plots\Statistical Datasets\Q1_a.csv")
df.dtypes
df.columns
plt.hist(df.speed)
plt.boxplot(df.speed) # No Outliers 
plt.boxplot(df.dist) # here outliers Outliers 

# Remve outliers

IQR = df['dist'].quantile(0.75) - df['dist'].quantile(0.25)
lower_limit = df['dist'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['dist'].quantile(0.75) + (IQR * 1.5)

############### 1. Remove (let's trim the dataset) ################
# Trimming Technique
# let's flag the outliers in the data set
outliers_df = np.where(df['dist'] > upper_limit, True, np.where(df['dist'] < lower_limit, True, False))
sum(outliers_df)

df_trimmed = df.loc[~(outliers_df), ]
df.shape, df_trimmed.shape

# let's explore outliers in the trimmed dataset
sns.boxplot(df_trimmed.dist) # now no outliers
df_trimmed.dist.mean()
df.speed.mean()
df_trimmed.dist.median()
df.speed.median()
df_trimmed.dist.mode()
df.speed.mode()
df_trimmed.dist.var()
df.speed.var()
df_trimmed.dist.std()
df.speed.std()

"""
Q2) Draw inferences about the following boxplot & histogram. 
Hint: [Insights drawn from the plots about the data such as whether data is normally distributed/not, outliers, measures like mean, median, mode, variance, std. deviation]

"""
df = pd.read_csv("D:\DATA Science 360 DigiTMG\Self Study\Statical Data Visulization Plots\Statistical Datasets\Q2_b.csv")
df.dtypes
df.columns
plt.boxplot(df.WT) # Otliers on WT

# Remve outliers WT

IQR = df['WT'].quantile(0.75) - df['WT'].quantile(0.25)
lower_limit = df['WT'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['WT'].quantile(0.75) + (IQR * 1.5)

############### 1. Remove (let's trim the dataset) ################
# Trimming Technique
# let's flag the outliers in the data set
outliers_df = np.where(df['WT'] > upper_limit, True, np.where(df['WT'] < lower_limit, True, False))
sum(outliers_df)

df_trimmed = df.loc[~(outliers_df), ]
df.shape, df_trimmed.shape
plt.boxplot(df_trimmed.WT) # now no outliers

plt.hist(df_trimmed.WT)

"""
Q3) Below are the scores obtained by a student in tests 
34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56
1)	Find mean, median, variance, standard deviation.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

x=pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
x.mean()
x.median()
x.var()
x.std()
