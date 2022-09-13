# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:10:50 2022

@author: Silver

"""

import random as ran


#1. Writes a list comprehension that prints a list of the cubes of the numbers 1 through 10.


print([i**3 for i in range(1,11)])



#2. Write a list comprehension that prints out the possible results of two coin flips (one result would be ’ht’). (Hint - how many results should there be?)

print( [ flip1+flip2 for flip1 in ran.sample([ 'h', 't'], 1) \
    for flip2 in ran.sample(['h', 't'],1) ] )


#3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string.

def return_vowels(str):
    return [ ch for ch in str if ch in [ 'a', 'e', 'i', 'o', 'u']]

print("Vowels in the word cantelope ", return_vowels('cantelope'))

"""
4. Run this list comprehension  [x+y for x in [10,20,30] for y in [1,2,3]]
and figure out what is going on here.
"""

[x+y for x in [10,20,30] for y in [1,2,3]]

""" 
Next, write a nested for loop that gives you the same result. 
"""

for x in [10,20,30]:
    for y in [1,2,3]:
        print(x+y)



