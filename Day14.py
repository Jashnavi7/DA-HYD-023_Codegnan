#FUNCTIONS
'''
Functions --> A function is a block of code which performs a specific task
It is a reusable block of code where we define using keyword 'def'
Advantages --> Code reusability, Code mainatinability,ease of debugging,avoiding code dulication modularity
Syntax:
    def fname(parameters):   -->Function definition
        """Doc String""""     -->Description 
        Statement(s)......     -->Function
        .....
        return value(s)....
fname(args)    -->Function call
'''


#To perform sum of given objects
def add(a,b):
    """Sum of Objects"""
    c = a + b
    return c
print(add(6,7))             #addition
print(add('Code','gnan'))       #concatination
print(add([1,2,3],[4,5,6]))       # Merging
c,d = map(int,input('Enter the values:').split(','))
print(c,d)
print(add(c,d))


def add(a,b):
    """Sum of objects without return"""
    print(a + b)
add('jash','navi')
print(add(1,2))  #returns result and None as we already printing inside function


#Usage of return
name,age,salary = 'jashnavi',22,30000    #Global variables
def details():      #parameters are importanat bcoz it always returns output as global variables if not given
    #return name,age,salary
    #return 'codegnan'
    return     #returns None as there is nothing to return
print(details())

'''
There are 5 types of arguments:
    Positional Arguments
    Default arguments
    Keyword arguments
    variable length arguments(*args)
    keyword variable length arguments(**kwargs)
Positional Arguments --> Number of arguments in function define should match with function call(order has to be maintained
Default Arguments --> we can make arguments as default but not first argument as default
Keyword Arguments --> whenever we want to specify the name of the argument  
'''


#Positional Arguments

#print(len(123,345))  this is as per built-in len(obj) will accept one argument
def details(name,place):
    """To store the details"""
    #name = 'codegnan'
    #place = 'Hyd'
    #return name,place
    print(f'name is {name}')
    print(f'place is {place}')
print(details('jash','waran'))
print(details('fvbhu','ygb'))
#print(details('ucefb',33,'cvddsj'))  #raises TypeError as we need to take 2 arguments as we passed 2 parameters
print(details(name='vidya',place='hydera'))
c,d = map(str,input('Enter values:').split(','))
details(c,d)



#default Arguments

#def grocery(item,price= 35):
#def grocery(item = 'pizza',price): #raises syntax error as non default always follows default

def grocery(item = 'Butter',price = 120): #we can make all arguments default
    """Usage of default arguments"""
    print(f'The item is {item} and price is {price}')
grocery('Milk',40)
#grocery(32,'Milk')
grocery('Bread')    #by default we have given price as 35 when giving parameters
grocery('Bread',90)
grocery()  #as both item and price are default arguments


#keyword argument
def employee(name,salary,role,place = 'hyd'):
    """ Keyword arguments usage"""
    print(f'name is {name},salary is{salary},role is {role} and place is {place}')
employee('jash',30000,'IT','hyd')
employee(name ='vaish',salary = 40000,role = 'HR')
employee('vid',55000,'Manager')















