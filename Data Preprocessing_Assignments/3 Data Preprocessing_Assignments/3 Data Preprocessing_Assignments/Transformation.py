# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
# _______________TRANSFORMATIONS_________##
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns


nor = pd.read_csv("D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\calories_consumed.csv")
nor.columns
nor.head()
nor.describe()
plt.boxplot(nor)
plt.show()
plt.hist(nor)
