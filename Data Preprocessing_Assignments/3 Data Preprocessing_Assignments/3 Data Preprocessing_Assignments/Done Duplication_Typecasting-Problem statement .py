# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
"""
Q1. For the given dataset perform the type casting (convert the datatypes, ex. float to int)
Q2. Check for the duplicate values, and handle the duplicate values (ex. drop)
Q3. Do the data analysis (EDA)?
Such as histogram, boxplot, scatterplot etc

"""

# _______________Q1 _____________________##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# load data 

df1 = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\OnlineRetail.csv",encoding='latin1')
df1.dtypes
df1.columns
df2 = df1['UnitPrice']
#df2.dtypes
df2 = df1['c'].astype('int',errors='ignore')
df2.dtype  # int32 datype

#__________________Q2______________________#

dup = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\OnlineRetail.csv",encoding='latin1')
dup.columns
dup.drop_duplicates(subset ="InvoiceNo", keep = False, inplace = True)

#____________________Q3___________________# 

bx = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\OnlineRetail.csv",encoding='latin1')

bx.shape

# barplot
plt.bar(height = bx.UnitPrice, x = np.arange(1, 774, 1)) # initializing the parameter

plt.hist(bx.UnitPrice) # histogram
plt.hist(bx.UnitPrice, color='green')

help(plt.hist)

plt.figure()

plt.boxplot(bx.UnitPrice) # boxplot
############### Scatterplot ############3

scp = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\OnlineRetail.csv",encoding='latin1')
scp.drop_duplicates(subset ="InvoiceNo", keep = False, inplace = True)

scp.columns
Quantity = scp.Quantity
UnitPrice = scp.UnitPrice
plt.scatter(UnitPrice,Quantity)
