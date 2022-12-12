import pandas as pd
import matplotlib.pylab as plt

Univ1 = pd.read_excel(r"D:\DATA Science 360 DigiTMG\Assignment\Dataset_Assignment Clustering\EastWestAirlines.xlsx")

Univ1.describe()
Univ1.info()

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(Univ1.iloc[:, 1:])
df_norm.describe()

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(20, 12));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

Univ1['clust'] = cluster_labels # creating a new column and assigning it to new column 

Univ1 = Univ1.iloc[:, [7,0,1,2,3,4,5,6]]
Univ1.head()

# Aggregate mean of each cluster
Univ1.iloc[:, 2:].groupby(Univ1.clust).mean()

# creating a csv file 
Univ1.to_csv("University.csv", encoding = "utf-8")

import os
os.getcwd()

############## Q2. #################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
cr1 = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Dataset_Assignment Clustering\crime_data.csv")

cr1.describe()
cr1.info()


# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(cr1.iloc[:,1:])
df_norm.describe()
print(df_norm) # looking data 

# for creating dendrogram 

z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()

# Now applying AgglomerativeClustering choosing 3 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

print(cluster_labels)
print(cr1)

################# Q3 ###########################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
cr1 = pd.read_excel(r"D:\DATA Science 360 DigiTMG\Assignment\Dataset_Assignment Clustering\Telco_customer_churn.xlsx")

cr1.describe()
cr1.info()
cr1.columns

cr1 = cr1.drop(["Customer ID"], axis=1)
#converting all categorical data in continuous
cr2 = pd.get_dummies(cr1,drop_first=True) 

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(cr2.iloc[:, 1:])
df_norm.describe()

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

cr2['clust'] = cluster_labels # creating a new column and assigning it to new column 

cr3 = cr2.iloc[:, [7,0,1,2,3,4,5,6]]
cr3.head()

# Aggregate mean of each cluster
cr3.iloc[:, 2:].groupby(cr2.clust).mean()

###################### Q4 #################

"""
4.	Perform clustering on mixed data. Convert the categorical variables to numeric
 by using dummies or label encoding and perform normalization techniques. 
 The data set consists of details of customers related to their auto insurance.
 Refer to Autoinsurance.csv dataset.
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
aut1 = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Dataset_Assignment Clustering\AutoInsurance.csv")

aut1.describe()
aut1.info()
aut1.columns

aut1 = aut1.drop(["Customer"], axis=1)
#converting all categorical data in continuous
aut2 = pd.get_dummies(aut1,drop_first=True) 

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(aut2.iloc[:, 1:])
df_norm.describe()

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# Now applying AgglomerativeClustering choosing 3 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

aut2['clust'] = cluster_labels # creating a new column and assigning it to new column 

aut3 = aut2.iloc[:, [7,0,1,2,3,4,5,6]]
aut3.head()

# Aggregate mean of each cluster
aut3.iloc[:, 2:].groupby(aut2.clust).mean()

