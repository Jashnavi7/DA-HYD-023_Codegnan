'''Sequences --> strings,lists,sets,tuples,mapping(dict)
Strings --> Group ofcharacters-we use single or double or triple quotes for representation of strings
Strings are immutable ,ordered and indexed collection
index[] --> is used to fetch the object(position) starts from 0 to len(obj)-1
we use [] representation
In python space is also a character
negative indexing --> -1 to len(obj)
Slicing[start:stop] --> we can access a group of characters(objects)
Slicing is applicable from lower index to higher index not applicable from higher to lower
Striging[start:stop:step] --> includes step 
we use [start:end] start default --> 0, start in included and end is excluded
'''
name = 'Codegnan'
print(name)
print(type(name))
print(len(name))    #len --> returns the length of the items in the container
print(name[0])    #returns index
#print(name[10])     #return index error as it is out of range of name
print(name[-8])
print(name[-1])    #returns last character

#slicing
name = 'python'
print(name[:])  #returns entire string
print(name[1:])    #returns entire string
print(name[:4])    #starts from 0th index and ends before 4th index
print(name[1:5])   #starts from 1st index and ends before 5th index
print(name[0:5])
print(name[7:3])  #returns empty string
print(name[:90])  #returns total string
print(name[-1:-5])   #returns empty string
print(name[-5:-1])   #possible
print(name[-5:])
print(name[4:6])
print(name[-6:3])
print(name[2:-6]) #returns empty string bcoz it is possible in single direction

#striding
course = 'DataAnalysis'
print(len(course))
print(course[::1])    #return all characters
print(course[::2])    #returns by skipping one element
print(course[1:6:3])
print(course[2::3])
print(course[::-1])   #returns string in reverse

name = 'jash'
name[3] ='t'  #returns type error as strings are immutable


#Operations on string --> Indexing,Concatination,Repitition
name = 'codegnan'
print(name * 3)
print('^' * 7)   #Repitition

data = 'Jash' + 'nav' + 'i'   #concatination
print(data)
print('123' * 4)
print('code' in name)
for i in name:
    #print(i)   #prints vertically
    print(i,end=',')
    
#Built-in Functions --> len(),min(),max(),sorted()
name = 'Codegnan'
print(len(name))
print(min(name))  #returns min ASCII value letter
print(max(name))  #returns max ASCII value letter
print(ord('A'))
print(ord('a'))
print(sorted(name))   #return a list by sorting all elements
print(chr(65))

#Methods on strings --> Case conversions,Finding/Searching
#case conversions --> upper(),lower(),title(),capitalize()
name = 'codegnan data'
a = name.upper()
print(a)
b = name.lower()
print(b)
c = name.title()   #converts every word first letter to capital
print(c)
d = name.capitalize()   #returns first letter capital
print(d)

#Task:workout with all posiible of slicing and striding on an example
#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z--> use loops and strings to  return A - Z
