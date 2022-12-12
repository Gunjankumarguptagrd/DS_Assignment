# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:52:25 2022

@author: Gunjan
"""
# _______________STRING MANIPULATIONS_________##

"""
1.	Create a string “Grow Gratitude”.
Code for the following tasks:
a)	How do you access the letter “G” of “Growth”?
b)	How do you find the length of the string?
c)	Count how many times “G” is in the string.
"""

# Accessing
x = "Growth Gratitude"
letter = x[0:6]
letter
# find length
len(x)

# count G
x.count('G')
x

"""
2.	Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”
Code for the following:
a)	Count the number of characters in the string.
"""
str = 'Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.'
print(str)
str.count(' ')


"""
3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
Code for the following tasks:
a)	get one char of the word
b)	get the first three char
c)	get the last three char

"""
str1="Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
str1
print(str1[-1])
print (str1[0:1]) # first char

print (str1[:3]) #get the first three char
print (str1[-3:]) #get the last three char

"""
4.	create a string "stay positive and optimistic". Now write a code to split on whitespace.
Write a code to find if:
a)	The string starts with “H”
b)	The string ends with “d”
c)	The string ends with “c”

"""
str4 = "stay positive and optimistic"
str4.startswith('H') # The string starts with “H”
str4.endswith('d') # The string ends with “d”
str4.endswith('c') # The string ends with “c”

"""
5.	Write a code to print " 🪐 " one hundred and eight times. (only in python)
"""
star = " 🪐 "
print(star*108)
"""
6.	Write a code to print " o " one hundred and eight times. (only in R)
"""
# R didn't study

"""
7.Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”
"""
rep = 'Grow Gratitude'
rep.replace('Grow', 'Growth') # Replacec with Growth

"""
8.A story was printed in a pdf, which isn’t making any sense. i.e.:
“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”

"""
story = '.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A'
rev_story = ''.join(reversed(story))
rev_story
