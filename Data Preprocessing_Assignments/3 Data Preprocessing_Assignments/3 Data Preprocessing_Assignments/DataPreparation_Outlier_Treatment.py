# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:59:16 2022

@author: Gunjan
"""

###### DataPreparation_Outlier_Treatment #########3
""" 1.	Prepare the dataset by performing the preprocessing 
        techniques, to treat the outliers.
"""
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\boston_data.csv")
df.dtypes
df.columns # Cheking Columns of excel file

#finding ouliers
sns.boxplot(df.ptratio)

sns.boxplot(df.tax) # no outliers

IQR = df['ptratio'].quantile(0.75) - df['ptratio'].quantile(0.25)
lower_limit = df['ptratio'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['ptratio'].quantile(0.75) + (IQR * 1.5)

############### 1. Remove (let's trim the dataset) ################
# Trimming Technique
# let's flag the outliers in the data set
outliers_df = np.where(df['ptratio'] > upper_limit, True, np.where(df['ptratio'] < lower_limit, True, False))
sum(outliers_df)

df_trimmed = df.loc[~(outliers_df), ]
df.shape, df_trimmed.shape

# let's explore outliers in the trimmed dataset
sns.boxplot(df_trimmed.tax)  # now no outliers

#### replace the outliers by the maximum and minimum limit ######
df['df_replaced'] = pd.DataFrame(np.where(df['ptratio'] > upper_limit, upper_limit, np.where(df['ptratio'] < lower_limit, lower_limit, df['ptratio'])))
sns.boxplot(df.df_replaced)
