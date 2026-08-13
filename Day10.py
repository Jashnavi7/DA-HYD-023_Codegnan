'''
sequences --> Strings,Lists,Tuples,Sets
Mapping --> Dictionary
List --> Collection of heterogeneous elements(items)
List --> Indexed,Ordered,Mutable,heterogenous,we use [] to store the data
Operators : Indexing,Slicing,Striding,Membership,Merging,Repitition
'''

marks = [12,34,56,67,89]
print(marks)
print(type(marks))
print(len(marks))
print(56 in marks)

#Nested Lists --> A list inside another list
names = ['codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(type(names))
print(names[0])
print(names[-3])
print(type(names[0]))
print(names[0][:4])
print(names[0][4:])
print(names[0][::2])
print(type(names[3]))
names[0] = names[0][::-1]
print(names)

print(len(names[3]))
print(names[3][2])
print(len(names[3]))
#indexing ,slicing --> Mutable
names[2] = 'Python'
print(names)
#By indexing if we change the elements,length of collection will reamain same
names[4] = ['jas','hnavi','jan','gili']
print(names)
print(names[0][1:])

print(names)
names[2:4] = 'fruits','vegetables','plants','tress'
print(names)
print(len(names))
names[3:6:2] = 'Java','Python'
print(names)

'''
create a nested list with strings.lists and work on indexing,slicing,striding ans string functions
Lists function --> append(),insert(),extend(),pop(),remove(),clear(),index(),count(),copy(),sort(),reverse()
append() --> inserts single element to the end of the list
append() will always increment the length of the list by 1
extend() --> inserts multiple elements to the end of the list
insert(index.object) --> inserts given object at specific index
pop() --> by default last is deleted,else given indexed object is deleted
remove() --> by default it removes the first occurance in the value in list and removes by giving value in the function
clear() --> deletes total list and gives empty list
del --> uses to remove multiple values and the changes are permanent
'''

#append()
names = ['Codegnan','jashnavi']
names.append('data')
print(names)
#names.append('cmr','it')  #TypeError
names.append(['cmr','it'])
print(names)
print(names[3].append('chatgpt'))   #it returns none as append doesnot store in names here
names[-1].append('chatgpt')
print(names)

#entend()
names.extend('analysis')    #string will be splitted as 'a','n'....
print(names)
names.extend(['analysis','data'])
print(names)
names.extend([45,72,24,56])
#names.extend(35,34)   TypeError -> as only 1 argument to be passed 
print(names)

#insert()
names.insert(1,'python')
print(names)
names.insert(0,'Java')
#names.insert([1:4],['s','df'])  syntaxError
print(names)
names.insert(-1,'c++')
print(names)
names.insert(7,'R')
print(names)

#pop()
print(names.pop())
print(names)
print(names.pop(2))
names.pop(4)
print(names)

#removes()
names.remove('Java')
print(names)

del names[1:3]  #del keyword will apply permanent changes
print(names)
names.clear()    #clear() will remove all elements and returns empty list
print(names)


#Task
data = ['codegnan','saketh','python','java']
for i in data:
    print(f'{data.index(i)} : {i}')
