import aug29 as a  #alias is used to temporarily call that module 
#print(dir(aug29))
#print(type(aug29.details))  # if we use alias then we should not use again file name,that throws errors
print(type(a.greeting))
print(a.greeting())
print(a.details)
#we can access funtions,datatypes using . operator
a.details['subjects']=['python','sql','eda']
print(a.details.keys())

from aug29 import details
print(details)
#print(greeting())  --> returns error as greeting is not imported from the aug28 file
details['subjects']=['python','sql','eda']
print(details.keys())

from aug29 import details,greeting
print(details)
print(greeting())

#if you want to access all functions module at a Time
from aug29 import *  # * is used to load everything from the file , * is recommanded for user defined file 

import random
import time

#random module --> get number generation,random text
#print(dir(random))
##-------otp generation
for i in range(5):
    print(random.randint(1000,9999))    #randint(start:end) ---> returns only integers
    time.sleep(1)  #sleep(seconds) --> waits for givens seconds
print(random.random())  #--> retruns random value in float that takes no arg

details=['a long back','once upon a time','back then','ten years ago']
print(random.choice(details))
#try out a story

#math module --> contains mathematical constants, log,exp,trignometeric
import math 
print(dir(math))
print(math.ceil(4.567)) #round off to the next highest value --> op 5(only interger)
print(math.floor(7.976)) #round off to lowest value --> op 7(only interger as op)
print(math.factorial(5))
print(math.pi)
print(math.gcd(4,12))
print(math.trunc(4.96))