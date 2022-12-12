# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
"""
1)	Prepare the dataset by performing the preprocessing techniques, to have the all the features in numeric format.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data 

df = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\animal_category.csv")
df.dtypes
df.columns
#df.Sepal_Length
df.shape # will give u shape of the dataframe

df.dtypes

# Create dummy variables
df_new = pd.get_dummies(df)
print(df_new)
df_new_1 = pd.get_dummies(df, drop_first = True)
# we have created dummies for all categorical columns

