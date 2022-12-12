# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
# _______________STANDARDIZATION & NORMALIZATION_________##
import pandas as pd
import numpy as np

### Standardization
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\Seeds_data.csv")

a = data.describe()
a
# Initialise the Scaler
scaler = StandardScaler()
# To scale data
df = scaler.fit_transform(data)
# Convert the array back to a dataframe
dataset = pd.DataFrame(df)
res = dataset.describe()

### Normalization
## load data set
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\Seeds_data.csv")

data.columns
### Normalization function - Custom Function
# Range converts to: 0 to 1
def norm_func(i): 
    x = (i-i.min())/(i.max()-i.min())
    return(x)

df_norm = norm_func(data)
b = df_norm.describe()
b
