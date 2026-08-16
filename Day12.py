'''
Sequences --> Strings,Lists,Tuples,Set,Frozenset
Mapping --> Dictionary

#Sets --> A set is a unique collection of objects,Unordered,Mutable,Hashing,Unindexed,Unique,Heterogeneous
#set(),{}
'''


#Sets
#a = {}    #empty dictionary
a = set()
print(type(a))
stud_id = {123,345,234,564,234}
print(stud_id)
print(type(stud_id))
print(len(stud_id))
#print(a[2])   #raises TypeError -- as set is not subscriptable
print(234 in stud_id)
#print(stud_id * 2)  #raises TypeError -- set can't be repeated
#print(stud_id + stud_id)  #raises TypeError -- Two sets can't be merged

data = {12,3,4,5,[12,3,4],'saketh'}
print(data)   #list shouldn't be included in set as it is unhashable type(hashing techinique)

data = {12,3,4,5,(12,3,4),'saketh'}
print(data)   #possible bcoz tuples are immutable
print('length:',len(data))
for i in data:
    print(i)


'''
Methods on sets --> add(),update(),remove(),discard(),pop(),copy()
add() --> adds element to the set (single value) to add multiple values we need to add in inform of set. set doesnot add multiple values
update() --> we can update multiple elements in set
remove() --> removes an element from the set(it must be a member)
discard() --> will remove an element if its present else it ignores the statement
pop()  --> removes any 1 element in the set
copy() --> creates a shallow copy of set (independent of each other)
'''


names = {'sai','saketh','kiran','codegnan'}
print(f'length:{len(names)}')

#add()
names.add('python')
print(names)
#names.add('jash','sdf') #TypeError -- set.add() takes one argument
names.add(('Jash','sdf'))
print(names)   #posiible becoz it including set of elements inside the set
#names.add({'vaish','vidya'})  #raises TypeError -- unhashable set

#update()
da_names = {'sonu','akash','sai','mani'}
names.update(da_names)
print(names)
print(len(names))
print(da_names)
da_names.update(names)
print(da_names)
print(len(da_names))

#remove() 
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')
#print(da_names)  #KeyError -- as sai is not there in the set

#discard() 
da_names.discard('sai')  #doesnot gives error it just ignores statement
print(da_names)

#pop()
da_names.pop()
print(da_names.pop())
print(da_names)
da_names.add('sairam')
print(da_names)
da_names.update(['fhvu','ruyn'])
print(da_names)
da_names.update('goat','cat')
print(da_names)

#copy()
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)


'''
Mathematical operations --> union(),intersection(),difference(),symmetric_diffrence,issubset(),issuperset(),isdisjoint()
union() --> returns all elements present in both sets but removes duplicates
intersection() --> returns common elements in both sets
difference() --> removes common elements and prints elements from first set
Symmetric difference() --> removes common elements and prints elements from both sets
issubset() --> returns True if all the elements in set2 is present in set1
issuperset() --> returns True if set1 has all elements present in set2
isdisjoint() --> returns false for sets having common elements
'''


da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}

da_25 = {67,90,34,78,78}
#union()
event = da_23.union(da_24)
event2 = da_23 | da_24   #we can also write '|' instead of .union
print(event2)   
event1 = da_23.union(da_24).union(da_25) #union can be performed with any number of sets
print(event1)
print(event)
print(len(event))

#intersection()
common = da_23.intersection(da_24)  #can be performed with only 2 sets
common1 = da_23 & da_24  #we can also use '&' instead of intersection
print(common)
print(common1)
print(len(common))

com = da_23.intersection_update(da_24)
print(com) #it returns None
print(da_23)  #common elements are finally stored

#difference()
diff = da_23.difference(da_24)
print(diff)
d = da_23 - da_24  #we can also write '-' instead of difference
print(d)

#Symmetric difference()
symm = da_23.symmetric_difference(da_24)
print(symm)
s = da_23 ^ da_24   #we can also use '^' instead of symmetric_difference
print(s)

#issubset()
da_24.remove(46)
da_24.remove(47)
print(da_24.issubset(da_23))

#issuperset
print(da_23.issuperset(da_24))

#isdisjoint()
print(da_23.isdisjoint(da_24))
