'''
File Handling in python : Files are mainly used to store the data
 It supports (r,w,a)read mode write mode append using open()
'''
#First lets understand how we can access .txt files using python

import os

if  os.path.exists('sample.txt'):    #checks whether it exists or not
    file = open('sample.txt','r')     #takes as object and access file when open is used
    print('File is loaded succesfully')
else:
    print('File is not present')

#Now let us access the content from the file
file = open('sample.txt','r')   #it takes default read mode even if we dont write 'r'
#print(file)
#print(file.read())   #reads the entire content in the File
#print(type(file.read()))
#a = file.read()
#print(a)
#print(len(a))  #assign to a variable and check the length

#radline(),readlines()
print(file)
#print(file.readline())  #read single line from the file
print(file.readlines())  #reads all lines in the file in a list and gives \n in between 2 lines


#'w' mode --> It automatically creats a new file , if the file is exists
file = open('data.txt','w')   #creates file
print(file)  
#as file is automatically create lets write content to it
file.write('Good Afternoon , How are you?')
file.write('\nHad your Lunch?')  #does not overrides it agains writes in file
file.close()


#we can use with keyword to avoid close()
with open('data.txt','w') as f:    #it also access files
    f.write('Now checking what happened')    #it doesnot needs close()  it overrides before content
   
# 'a' --> it also automatically creates a file ,but if the file is already existing it appends the content to the previous file
with open('data.txt','a') as g:
    g.write('\nOkay let us see how its going')  #adds content to before content in the file

# + --> read and write
with open('data.txt','r+') as h:   #'r+' performs both read and write
    #print(h.read())
    #h.write('\nstop the class')
    h.write('\nBoring')
    print(h.read())  #if we first writes and then reads it overrides first content in file it replaces that content

#File operations size and path
import os
#file = open('data.txt','r')
if os.path.exists('data.txt'):
    print('File size is',os.path.getsize('data.txt'),'Bytes')
    print('File Absolute path is',os.path.abspath('data.txt'))
else:
    print('File is not present')