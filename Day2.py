#multiassignment of variables
name,age,location = 'Jashnavi',22,'Hyderabad'
print(name,age,location,sep=',')
print(name,age,location,sep='         ')


#Reassigning variables
a,b = 2,3.4
print(a,b,sep=',')
b,a = a,b   #swapping
print(a,b,sep=',')


#deleting the variable
#del a,b
#print(a,b)


name = 'codegnan' ; age = 7 ; course = 'Data Analysis'  #valid
print(age,name)


'''
Punctuators ==> []-->(list), {}-->(dict,sets) , ()-->(tuples)

name='codegnan' , age =7   #invalid syntax
print(age,name)


DataTypes --> Numeric (int,float,complex),boolean,None
Sequences --> Lists,tuples,sets,strings,frozenset,mappings

Numeric Type --> int,float,complex
int datatype --> quantity,age..
float datatype --> salary,price,temp
complex datatype --> combination of real and imaginary

Boolean --> True / False    
'''
#int
age = 7
print(age)
print(type(age))  #type --> returns the datatype of an object

#quantity = 03  --> not allowed
#print(quantity)

#float
price = 750.23
print(price)
print(type(price))

#complex
data = 5+2j     #j is for complex notation // j is imaginary representation
print(data)
print(type(data))

#Boolean
valid = True
print(valid)
print(type(valid))

error = False
print(error)
print(type(error))


'''Typecasting --> converting onr type to another type
python by default follows implicit type we dont need to mention datatype

we will go for explicit conversion
every built in datatype is a built in function
int,float,complex,boolean
typecasting --> int -->ArithmeticError float,complex,boolean'''

#converting int to other datatypes
age = 35
print(age)
print(type(age))
b = float(age)
print(b)
print(type(b))
c = complex(age)
print(c)
print(type(c))
d = bool(age)
print(d)
print(type(d))
e = bool(0)
print(e)
print(type(e))

#converting float to other datatypes
discount = 35.6
print(discount)
print(type(discount))
b = int(discount)
print(b)
print(type(b))
c = bool(discount)
print(c)
print(type(c))

'''
#converting complex to other types
imag = 3+2j
print(imag)
a = int(imag)
print(a)
print(type(a))   #we cant convert them into other datatypes except boolean'''


e = int(float(bool(complex(5))))
print(e)

a = bool(int(float(6)))
print(a)

f = 6 + 2.5 + 7j + True    # true adds one false adds nothing 
print(f)
