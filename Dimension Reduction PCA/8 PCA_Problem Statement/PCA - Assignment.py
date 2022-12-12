""" Perform hierarchical and K-means clustering on the dataset. After that, 
perform PCA on the dataset and extract the first 3 principal components
and make a new dataset with these 3 principal components as the columns.
Now, on this new dataset, perform hierarchical and K-means clustering. 
Compare the results of clustering on the original dataset and clustering 
on the principal components dataset (use the scree plot technique to obtain 
the optimum number of clusters in K-means clustering and check if you’re 
getting similar results with and without PCA). """

import pandas as pd
import matplotlib.pylab as plt

Uni_k1 = pd.read_excel(r"D:\DATA Science 360 DigiTMG\Self Study\Dimension Reduction PCA\University_Clustering.xlsx\University_Clustering.xlsx")

Uni_k1.describe()
Uni_k1.info()

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)

# Droping Test columns
Uni_k1 = Uni_k1.drop(["State","Univ"], axis = 1)

df_norm = norm_func(Uni_k1.iloc[:, 1:])
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

Uni_k1['clust'] = cluster_labels # creating a new column and assigning it to new column 

Uni_k1 = Uni_k1.iloc[:, [7,0,1,2,3,4,5,6]]
Uni_k1.head()

# Aggregate mean of each cluster
Uni_k1.iloc[:, 2:].groupby(Uni_k1.clust).mean()


######################## K means ######################
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from sklearn.cluster import	KMeans
# from scipy.spatial.distance import cdist 
# Kmeans on University Data set 
Uni1 = pd.read_excel(r"D:\DATA Science 360 DigiTMG\Self Study\Dimension Reduction PCA\University_Clustering.xlsx\University_Clustering.xlsx")

Uni1.describe()
Uni = Uni1.drop(["State"], axis = 1)

# Normalization function 
def norm_func(i):
    x = (i - i.min())	/ (i.max() - i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(Uni.iloc[:, 1:])

###### scree plot or elbow curve ############
TWSS = []
k = list(range(2, 9))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
    
TWSS
# Scree plot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

# Selecting 5 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 3)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
Uni['clust'] = mb # creating a  new column and assigning it to new column 

Uni.head()
df_norm.head()

Uni = Uni.iloc[:,[7,0,1,2,3,4,5,6]]
Uni.head()

Uni.iloc[:, 2:8].groupby(Uni.clust).mean()


################################## PCA

import pandas as pd
import numpy as np

uni_p1 = pd.read_excel(r"D:\DATA Science 360 DigiTMG\Self Study\Dimension Reduction PCA\University_Clustering.xlsx\University_Clustering.xlsx")
uni_p1.describe()

uni_p1.info()
uni_p2 = uni_p1.drop(["State","Univ"], axis = 1)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 

# Considering only numerical data 
uni_p2.data = uni_p2.iloc[:,:]

# Normalizing the numerical data 
uni_p2_normal = scale(uni_p2.data)
uni_p2_normal

pca = PCA(n_components = 3)
pca_values = pca.fit_transform(uni_p2_normal)

# The amount of variance that each PCA explains is 
var = pca.explained_variance_ratio_
var

# PCA weights
pca.components_
pca.components_[0]

# Cumulative variance 
var1 = np.cumsum(np.round(var, decimals = 4) * 100)
var1

# Variance plot for PCA components obtained 
plt.plot(var1, color = "red")

# PCA scores
pca_values

pca_data = pd.DataFrame(pca_values)
pca_data.columns = "comp0", "comp1", "comp2",
final = pd.concat([uni_p1.Univ, pca_data.iloc[:, 0:3]], axis = 1)

# Scatter diagram
import matplotlib.pylab as plt
ax = final.plot(x='comp0', y='comp1', kind='scatter',figsize=(12,8))
final[['comp0', 'comp1', 'Univ']].apply(lambda x: ax.text(*x), axis=1)

###########  after Aplyig PCA doing Hierarical clst

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(pca_data, method = "complete", metric = "euclidean")

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

pca_data['clust'] = cluster_labels # creating a new column and assigning it to new column 

pca_data = pca_data.iloc[:, [3,0,1,2]]
pca_data.head()

# Aggregate mean of each cluster
pca_data.iloc[:,:].groupby(pca_data.clust).mean()

####################### After Aplying PCA Doing K Means

TWSS = []
k = list(range(2, 9))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(pca_data)
    TWSS.append(kmeans.inertia_)
    
TWSS
# Scree plot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

# Selecting 3 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 5)
model.fit(pca_data)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
pca_data['clust'] = mb # creating a  new column and assigning it to new column 

pca_data.head()
df_norm.head()

pca_data = pca_data.iloc[:,[3,0,1,2]]
pca_data.head()

pca_data.iloc[:, 2:8].groupby(pca_data.clust).mean()


"""
A pharmaceuticals manufacturing company is conducting a study on a new medicine 
to treat heart diseases. The company has gathered data from its secondary sources 
and would like you to provide high level analytical insights on the data. Its 
aim is to segregate patients depending on their age group and other factors given 
in the data. Perform PCA and clustering algorithms on the dataset and check if the 
clusters formed before and after PCA are the same and provide a brief report on 
your model. You can also explore more ways to improve your model. 
"""


import pandas as pd
import numpy as np

hrt1 = pd.read_csv("D:\DATA Science 360 DigiTMG\Assignment\As Dimension Reduction PCA\Datasets_PCA\heart disease.csv")
hrt1.describe()

hrt1.info()

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 

# Considering only numerical data 
hrt1.data = hrt1.iloc[:, 1:]

# Normalizing the numerical data 
uni_norma2 = scale(hrt1.data)
uni_norma2

pca = PCA(n_components = 6)
pca_values = pca.fit_transform(uni_norma2)

# The amount of variance that each PCA explains is 
var = pca.explained_variance_ratio_
var

# PCA weights
pca.components_
pca.components_[0]

# Cumulative variance 
var1 = np.cumsum(np.round(var, decimals = 4) * 100)
var1

# Variance plot for PCA components obtained 
plt.plot(var1, color = "red")

# PCA scores
pca_values

pca_data = pd.DataFrame(pca_values)
pca_data.columns = "comp0", "comp1", "comp2", "comp3", "comp4", "comp5"
final = pd.concat([pca_data.iloc[:, 0:6]], axis = 1)

# Scatter diagram
import matplotlib.pylab as plt
ax = final.plot(x='comp0', y='comp1', kind='scatter',figsize=(12,8))

##### After PCA doing Clustering 

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

zz = linkage(pca_data, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(20, 12));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(zz, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()

# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(final) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

pca_data['clust'] = cluster_labels # creating a new column and assigning it to new column 

pca_data = pca_data.iloc[:, [3,0,1,2]]
pca_data.head()

# Aggregate mean of each cluster
pca_data.iloc[:,:].groupby(pca_data.clust).mean()
