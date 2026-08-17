'''
Mapping --> Dictionary --> Collection of key-value pairs used to store related data 
 JSON,APIs,database records
Dictionary is mutble,Indexed through keys,ordered,heterogeneous
Keys must be unique(int,string,float....)
dict() --> data = {}   data = {Keys : value}
'''


details = {}
print(type(details))

details = {'Id':'CGH1234','Name':'Jashnavi',
           'Gender':'F','Age':16,'Batch':'DA23',
           'Place':'Hyd'}
print(details)
print(len(details))


#Access the data from dictionary
#details[0]  #raises KeyError

print(details.keys())
print(details.values())
print(details['Id'],details['Name']) #returns values of the given keys

#if key is not matching/invalid
#print(details['Marks']  #keyError as marks is not there
details['Marks'] = []
print(details)
details['Marks'].append(30)
print(details)
details['Marks'].extend([23,24,25])
print(details)

#create key value pair of practice session
details['Practice_session'] = ('tues','thru','sat')
print(details)

#Accessing
print(details['Marks'][2])
print(details['Practice_session'][1])
details['Mock'] = ('mon','wed','fri')

#operations --> mutable,indexing,through keys,membership
print('wed' in details) #returns false as wed is not a key
'''
for i in details :
    print(i)    #returns keys one by one with or without .key()
for j in details.values():
    print(j)    #returns values one by one
    '''
for i in details.keys():     #returns same output with or without.keys()
    print(f'key : {i} ')    
    print(f'Values : {details[i]}')

for i in details.items():   #returns key-value pairs
    print(i)

for key,value in details.items():  #if we dont write .items() we get ValueError bcoz we are not saying what to return
    print(f'Key is {key}')
    print(f'Value is {value}')


#update() --> for updating values
details.update({'marks':[],'ps':('tues','thur','sat')})
print(details)
details['marks'].extend([56,34,67])
print(details)

marks = list(map(int,input('Enter marks:').split(',')))
details['marks'].extend(marks)
print(details)

#get() -->  return the values of the keys present in the dictionary
print(details.get('Name'))
print(details.get('marks'))  #it returns none as we dont have the key: marks

#setdefault() --> to insert key-value pair or key which is not present in the dictionary if key is present it just returns the value of the key
details.setdefault('Branch','cse')
#details['Branch'] = 'aiml'
print(details)

print(details.setdefault('Name','jash'))  #we cant update value for a key in setdefault

#pop
print(details.pop('Branch'))  #we must mention key,orelse it throws error
print(details.keys())

#popitems
print(details.popitem())   #pops from lastin  ,returns key-value pair which is popped as a tuple


#del
del details['Age']    #delets specific key-value pair
print(details.keys())

#clear()
details.clear()   #removes all elements from dictionary
print(details)


#fromkeys() --> creates a dictionary from other iterables(lists,tuples,sets,strings)
data = ['jash','jang','jaan']
a = (dict.fromkeys(data))   # creates a dict but values set to None
a['jash'] = 11
print(a)
b = dict.fromkeys(['GGH','CGH1'],['cod','gna'])
print(b)


#Task --> create a set of details of student like codegnan

student_profile = {'Name':'Jashnavi','stu_id':'CGH3793','Batch_no':'DA-HYD-023',
                   'Email':'764@gmail.com','DOB':'7-6-2004',
                   'Age':22,'Gender':'F','City':'Mulugu','State':'Telangana',
                   'Phone_no':'XXXXXXXXXX','Github':'https://github.com/1234'}
print(student_profile)

