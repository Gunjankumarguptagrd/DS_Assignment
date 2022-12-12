# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
# Zero - Variance Features  ##
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns


Z = pd.read_csv("D:\DATA Science 360 DigiTMG\Assignment\Data Preprocessing_Assignments\DataSets-Data Pre Processing\Z_dataset.csv")
Z.columns
Z.dtypes
Z.var() == 0
Z.var()
