'''input formatting --> Accepting input from the user --> input()
Accepting integer input from user
By default input() accepts any input --> str
'''

#int(input())--> will accept only integers
age = int(input('Enter age:'))
print(age)
print(type(age))

#float(input())--> will accept only float
price = float(input('Enter price:'))
print(price)
print(type(price))

#complex(input())--> will accept only complex numbers
value = complex(input('Enter value:'))
print(value)
print(type(value))

#Accepting string input from user
name = input('Enter name:')
print(name)
print(type(name))

#Accept group of values
a = input('Enter names:').split()   #By default split has space
print(a)

#space seperated values
a = input('Enter names:').split()   #now enter spaces in output
print(a)

#comma seperated values 
a = input('Enter names:').split(',')   
print(a)

#List of Integers
marks = list(map(int,input('Enter the values: ').split(',')))
print(marks)

#now we want to accept 2 values from users
age,salary = map(int,input('Enter the values: ').split(','))
print(age)
print(salary)

'''
single input --> int(input)
two inputs --> a,b = map(int(input().split(','))
any number result as list --> a = list(map(int(input().split(',')))
'''

#List of float values
marks = list(map(float,input('Enter the values: ').split(',')))
print(marks)

#now we want to accept 2 values from users
price,discount = map(float,input('Enter the values: ').split(','))
print(price)
print(discount)

'''
Accepting input from user --> int,float --> input formatting
Operators --> operations perform operations between values(operands)
7 types --> Arithmetic,Assignment, Comparision(Relationship),Logical operators
Membership,Identity,Logical,Bitwise
Arithmetic operators --> +,-,*,/
Assignment operators --> =,+=,-=
Comparision Operators --> we compare the values --> returns boolean answer
 ==(equals to) , !=(not equal to) , <(lessthan) , >(greatrethan) , <=(lessthan or equals to) , >=(greaterthan or equals to)
Membership operator --> in,not in
 it checks for the existence of an object in a collection
Logical operators --> logical decision making --> and,or,not
 and --> all conditions to be satisfied
 or --> any one condition to be satisfied
 not --> reverses the output
identity Operators --> check for identification of an object --> id()
 is , is not
 
Floor division (integer division) --> returns quotient
'''

#Arithmetic Operations
print(5+8)
print(8-5)
print(5*8)
print(8/5)   #Always returns float value
print(8//5)   #Returns integer value
print(8%5)    #Gives remainder
print(5**3)   #exponential/power

#Area of rectangle
#Accept integer input as length,bredth --> find area of rectangle
length = int(input('Enter length:'))
breadth = int(input('Enter breadth:'))
Area = length * breadth
print(Area)

l,b = map(int,input('Enter values:').split(','))
area = l*b
print(area)


#Assignment operators
a=2
print(a)
a += 5   #updating value of 'a'
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 3
print(a)
a **= 2
print(a)


#comparision Operators
age = 18
number = 27
print(age == 18)
print(age != 18)
print(age<25)
print(age>25)
print(age<=25)
print(age>=25)
print(age>number)


#Membership operator
marks = [10,20,30,40,50]
print(60 in marks)
print(10 in marks)
print(20 not in marks)

print('jash' in 'jashnavi')
print('$' in '@#$%&*')


#Logical operator
a = (25 in [25,49,57]) and 45 < 56
print(a)
b = 45 > 56 or 45 < 56
print(b)
c = not(True)
print(c)


#Identity operators
a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)


