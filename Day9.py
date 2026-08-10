#Strings --> caseconversions, searching &finding,string testing methods,Replace,space removal

#Searching,Finding<Replacing,Joining...
a = 'Codegnan'
print(len(a))
print(min(a))
print (max(a))
b = a.index('e')   
print(b)          #returns the index position
c = a.index('n')
print(c)            #returns only first occurance
d = a.index('n',6)
print(d)             #returns next occurance
#e = a.index('n',8)
#print(e)            #ValueError
#f = a.index('z')
#print(z)           #valueError

b = a.rindex('n')
print(b)         #returns last occurance
c = a.index('n',1,7)
print(c)    #returns index of occurance in that range
#count() --> returns the number of items in the object which are repeating
print(a.count('n'))   #returns count of n
print(a.count('j'))   #returns 0 as we dont have j in object

#find()
print(a.find('C'))
print(a.find('t'))  #returns -1 if it is not present in the object
print(a.rfind('n'))  #returns last occurence

a = 'DataAnalysis'
for i in a:
    print(i,a.count(i),a.index(i))

#replacing,splitting,joining
#Replacing
a = 'jash#navi'
print(a.replace('j','r'))  #just replaces doesnot change string
print(a)
b = a.replace('i','a')    #reaasign the string after replacing
print(b)
print(a.replace('#',''))   #replace with empty space
print(a.replace('#','&^%$'))

#splitting
a = 'Data Analysis'
print(a.split())
b = 'jangili,jashnavi,patel'
print(b.split())  #doesnot split becoz ',' is not there in input
print(b.split(','))

#Join(iterable) --> concatinate any number of strings
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('@'.join(a))
print(a.join('@'))


#Strings testing methods(boolean output) --> isaplha(),isalnum(),isdigit(),isupper(),islower()
a = 'Jashnavi789'
print(a.isalnum())  #returns True for alphanumeric characters
b = 'jashnavi'
print(b.isalnum())
c = '123'
print(c.isalnum())
d = '123'
print(d.isdigit())
e = 'JASHnavi'
print(e.isupper())
f = "jashnavi"
print(f.islower())
print(f.isalpha())
#print('4/2'.isnumeric())   -- {isnumeric() has upper edge (numbers,fractions,romans)}
print(a.startswith('j'))
print(a.startswith('h',3))
print(a.istitle())


#space removal --> strip() removes leading and traning spaces
a = ' dnugdch wudhwio '
print(a.strip())
b = input('Enter string:').strip().lower()
print(b)

#zfill() --> filling with zeros as per the given numeric string
print('456'.zfill(8))  #fill zeros to left side
print('hi'.center(6))
print('hi'.center(6,'$'))
print('hi'.ljust(6,'#'))
print('hi'.rjust(6,'*'))
