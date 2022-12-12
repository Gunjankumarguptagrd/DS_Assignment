# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:54:47 2022

@author: Gunjan
"""

#############  ASSIGNMENT-1 Data Types ################
''' 1.	Construct 2 lists containing all the available data types  
        (integer, float, string, complex and Boolean) and do the following..
        a.	Create another list by concatenating above 2 lists
        b.	Find the frequency of each element in the concatenated list.
        c.	Print the list in reverse order.
'''
list1 = ["Gunjan", 100, 12.21, True, 0, 4j] 
type(list1)
print(list1)

list2 = ["Bharani", 100, 12.50, "360DigiTMG", False, 5j] 
print(list2)
#########################
Con_list = list1+list2
print(Con_list)
############################
import collections

def countFreq(Con_list):
    return collections.Counter(Con_list)
freq = countFreq(Con_list)

######################
list5 = ["Bharani", 100, 12.50, "360DigiTMG", False, 5j] 
list5.reverse()
list5

"""
2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)
a.	Find the common elements in above 2 Sets.
b.	Find the elements that are not common.
c.	Remove element 7 from both the Sets.

"""
set1 = set([1,2,3,4,5,6,7,8,9,10])
set2 = set([5,6,7,8,9,10,11,12,13,14,15])
######### a. #############
Common_Element = set1.intersection(set2)
print(Common_Element)
############### b. ###################

uniq = set1.union(set2)- set1.intersection(set2)
print(uniq)
################## C ####################

set1.remove(7)
set1
set2.remove(7)
set2

"""
3.	Create a data dictionary of 5 states having state name as key and 
            number of covid-19 cases as values.
        a.	Print only state names from the dictionary.
        b.	Update another country and it’s covid-19 cases in the dictionary.


"""
###### i comsider covid case something #########
dict1 = {"Delhi":100, "Haryana":20, "Mumbai":300, "Benglore":40,"Jharkhand":50}

dict1.keys()
dict1.update({"Russia":111})
dict1

#################### MODULE-2 OPERATORES ##############

"""
Please implement by using Python
1.	A. Write an equation which relates   399, 543 and 12345 
B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.

"""
x = 12345
y = 543
z = 399

equation = 22*y + z
print(equation)  #12345
if equation == x:
    print('it is a valid relation')
"""
2.  a=5,b=3,c=10.. What will be the output of the following:
              A. a/=b
              B. c*=5  
"""
a=5
b=3
c=10
a/=b
print(a) #1.66666667
c*=5
print(c) #50
"""
3. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
            B. How can you obtain 64 by using numbers 4 and 3 .
"""
"s" in "Data Science"

###############  MODULE 3 Variables ########################

"""
1.	What will be the output of the following (can/cannot):
a.	Age1=5
b.	5age=55

"""
Age1=5 # 5
5age=55 # invalid syntax


"""
2.	What will be the output of following (can/cannot):
a.	Age_1=100
b.	age@1=100

"""
Age_1=100 # 100
age@1=100 #cannot assign to operator
"""
3.	How can you delete variables in Python ?
"""
x= 50
del x
x

##############  MODULE-4 Conditional Statements ###################

"""
1.	 Take a variable ‘age’ which is of positive value and check the following:
a.	If age is less than 10, print “Children”.
b.	If age is more than 60 , print ‘senior citizens’
c.	 If it is in between 10 and 60, print ‘normal citizen’

"""
age = input("enter your age")
if age=10:
    return "Children"
elif age >10 & age <=60:
        return("Normal Citizen")
elif age>60    
return("Senior Citizen")

"""
Male and Female ,consider them as sr.citizens if their age >=60]
3.	Check whether the given number is positive and divisible by 5 or not.  

"""

age = 60
num = 5
if age%num == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
    
###############  MODULE 5 LOOPS and Functions ####################

"""

1.	A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.
        B) How do we create a sequence of numbers in Python.
        C)  Read the input from keyboard and print a sequence of numbers up to that number
"""

###############  A ###################
 list1=[1,5.5,(10+20j),"data science"]
print(list1)

############  B ###################
for x in range(10):
    print(x)
################## C ###############

seq = int(input("Enter Any Number for Sequence"))
for i in range(0,seq):
    print(i)
    
"""
2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 Create a dictionary such that list2 are keys and list 1 are values..
"""
list1=[0,1,2,3,4,5,6,7,8,9]
list2=['zero','one','two','three','four','five','six','seven','eight' ,'nine']

res = dict(zip(list1, list2))
print ("Resultant dictionary is : " +  str(res))

"""
3.	 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to
 the even number and multiply with 5 if it is odd number in the list1..
"""

list1 = [3, 4, 5, 6, 7, 8]

list2 = []

for num in list1:
    if (num%2) == 0:
        num + 10
        list2.append(num)
    else:
        num*5
        list2.append(num)

list2

"""
 Write a simple user defined function that greets a person in such a way that :
             i) It should accept both name of person and message you want to deliver.
              ii) If no message is provided, it should greet a default message ‘How are you’
           Ex: Hello ---xxxx---, How are you  - default message.
            Ex: Hello ---xxxx---, --xx your message xx---

"""

x ="gunjan"
def greet1(x):
    print("Hello", x, "How are you")
greet1(x)

########### MODULE 6 PACKAGES ##########################

"""
1.	For the dataset “Indian_cities”, 
a)	Find out top 10 states in female-male sex ratio
b)	Find out top 10 cities in total number of graduates
c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.


"""
########### a ##################
import pandas as pd

x = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Python programming\Python Problem Statements\Indian_cities.csv")
gkk = x.groupby(['state_name']).mean()
### x.columns
sot = gkk.sort_values('sex_ratio', ascending=False)
sot.head(10)

################# b #########################

x1 = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Python programming\Python Problem Statements\Indian_cities.csv")
### x1.columns
## gk = x1.name_of_city 
df_new = x1[['name_of_city', 'total_graduates']]
sot1 = df_new.sort_values('total_graduates', ascending=False)
sot1.head(10)
            
            
####################### c ###########################            
            
x2 = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Python programming\Python Problem Statements\Indian_cities.csv")
### x1.columns
## gk = x1.name_of_city 
df_new1 = x2[['state_name','name_of_city', 'literates_total']]
sot2 = df_new1.sort_values('literates_total', ascending=False)
sot2.head(10)
            
"""
2.	For the data set “Indian_cities”
a)	Construct histogram on literates_total and comment about the inferences
b)	Construct scatter  plot between  male graduates and female graduates

"""
hst = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Python programming\Python Problem Statements\Indian_cities.csv")
### x1.columns
df_new3 = hst[['literates_total']]

df_new3.hist()

#############  C ##################
import pandas as pd
pt = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Python programming\Python Problem Statements\Indian_cities.csv")
### x1.columns
df_new4 = pt[['male_graduates']]
df_new5 = pt[['female_graduates']]

import matplotlib.pyplot as plt

plt.scatter(df_new4, df_new5)
plt.show()

"""
3.	For the data set “Indian_cities”
a)	Construct Boxplot on total effective literacy rate and draw inferences
b)	Find out the number of null values in each column of the dataset and delete them.

"""
############## a #######################
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

load = pd.read_csv(r"D:\DATA Science 360 DigiTMG\Assignment\Python programming\Python Problem Statements\Indian_cities.csv")

literacy = load[['effective_literacy_rate_total']].sort_values('effective_literacy_rate_total', ascending=True)                                              
literacy

data = load[['female_graduates']]
fig = plt.figure(figsize =(10, 5))
 
# Creating plot
plt.boxplot(data) 
plt.show()

################## b #########################


