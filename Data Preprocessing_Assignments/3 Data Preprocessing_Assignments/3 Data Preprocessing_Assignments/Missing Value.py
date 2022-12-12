# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
"""
Q5) Calculate Mean, Median, Mode, Variance, Standard Deviation, Range & comment about the values / draw inferences, for the given dataset
"""

# _______________missing value _____________________##
import numpy as np
import pandas as pd
# load data 

df_m = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\claimants.csv")
df_m.dtypes
df_m.columns
# check for count of NA's in each column
df_m.isna().sum()
# for Mean, Meadian, Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

# Mean Imputer  CLMSEX
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df_m["CLMSEX"] = pd.DataFrame(mean_imputer.fit_transform(df_m[["CLMSEX"]]))
df_m["CLMSEX"].isna().sum()

# df_m.isna().sum()
# Mean Imputer  CLMINSUR
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df_m["CLMINSUR"] = pd.DataFrame(mean_imputer.fit_transform(df_m[["CLMINSUR"]]))
df_m["CLMINSUR"].isna().sum()

# Mean Imputer  SEATBELT
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df_m["SEATBELT"] = pd.DataFrame(mean_imputer.fit_transform(df_m[["SEATBELT"]]))
df_m["SEATBELT"].isna().sum()

# Mean Imputer  CLMAGE
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df_m["CLMAGE"] = pd.DataFrame(mean_imputer.fit_transform(df_m[["CLMAGE"]]))
df_m["CLMAGE"].isna().sum()

df_m.isna().sum() # No Missing Value
