# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
"""
1)	Convert the continuous data into discrete classes on iris dataset.
Prepare the dataset by performing the preprocessing techniques, to have the data which improve model performance.

"""
import numpy as np
import pandas as pd

# load data 

data = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\iris.csv")
#df.dtypes
#df.columns
#df.Sepal_Length
data['Sepal_Length'] = pd.cut(data['Sepal_Length'], bins=[min(data.Sepal_Length),data.Sepal_Length.mean(), max(data.Sepal_Length)], labels=["Low","High"], include_lowest=True)
print(data)

data.Sepal_Length.value_counts()
