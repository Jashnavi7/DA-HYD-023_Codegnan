'''
Lists,Tuples..
List --> Mutable , ordered, Heterogenuos
index(),count(),sort(),reverse()
'''


details = ['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))    #returns first index of 21
print(details.index(21,6))  #starts searchin for 21 after the 6th index
#print(details.index('python'))     #valueError
print(details.count(21))
print(details.count('python'))  #it returns 0 as we dont have it


#copy() --> shallow copy of the given collection
data = ['codegnan',7,2018,'Hyderabad']
new = data.copy()
print(new)
print(type(new))
print(len(data))
new[2] = 'Agentic AI'
print(new)
print(data)

data.append('jashnavi')
print(data)
print(new)
print(new.pop(3))
print(data.pop(4))
print(data)
print(new)

data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents'   #nested list makes changes in original list also
print(new)
print(data)    #give output like new

new[1] = 'Python'
print(new)
print(data)


#sort() --> printing in sorted order(ascending order) , These makes permanent changes
marks = [14,24,-45,27,35]
print(marks)
marks.sort()  #sort returns list in ascending order
print(marks)
#print(marks.sort())    #returns None and list in ascending order
marks.sort(reverse = True)   #returns in descending order
print(marks)
#marks.append('jash')
marks.sort(reverse = True)   #when we try to perform operations of a list including both string and numbers it returns an TypeError
print(marks)
print(marks[::-1])


#reverse() --> returns in reverse order ,this makes permanent changes so should not include inside print statement
marks.reverse()
print(marks)


#type(),len(),max(),min(),print() --> builtin functions performs operations on collections
#sorted() is a builtin function which gives output in any collections in ascending order
print(sorted('Jashnavi'))
print(sorted(['code','23','34',45])) #raises TypeError as it has string and numeric values  


#Tuples --> tuples are indexed,ordered,heterogenous,immutable collection,dimensions,coordinates,databases records ,we prefer () for tuple notation
a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))

#Operations --> Indexing,Slicing,Striding,Membership,Merging,Repetition
courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))
print(courses[-2][-2:])
#courses[2] = 23      tuples are immutable
courses[4].append('codegnan')   #we can add elememts inside the list present in the tuple bcoz lists are mutable
print(courses)


#Tuple operations --> count(),index()
#index()
courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses.index('AgenticAI'))
print(courses.count('PFS'))
#print(courses.sort())  #attribute Error as tuple has no attribute sort if it has mixed types
print(sorted(courses[-1]))   #sorts beacause here we are sorting list in tuples
#print(sorted(courses))  #returns typeerror as it has multiple types

#Typecasting
d = tuple(sorted((2,4,7,3,6)))
print(d)


#accept group of integer space separated
a,b = map(int,input('Enter the values:').split(','))
print(a,b)

a = tuple(map(int,input('Enter values:').split(',')))
print(a)

print('9-8')
#eval() --> function can take any kind of input
print(eval('9-4'))
a = eval(input('Enter list:'))
print(a)
print(type(a))

#Create a nested tuple as above and work on slicing , striding, list functions
'''print('PFS' in courses)
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5) #merging
print(e)'''

