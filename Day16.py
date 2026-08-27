#Exception Handling
'''
Exception handling and scope of variables / built in functions

Exception handling --> it is a machanism that help to respond or make the flow of execution in normal way, without this error will occur and disrupt the flow of execution

Common expections --> ValueError,TypeError, IndexError,AttributeError,ZeroDivisionError


#Exception Handling
syntax:

try:
    #code that will cause the exception
except Exception e:
    #code will catch the exeception
finally:
    #runs irrespective of try/except
    ....

#basic exception
try:
    #a = 10
    #a = int(input('Enter value:'))
    l = list(map(int,input('Enter values:').split(',')))
    result = l[2]
    print(result)
    l.apped(8)
    print(l)
#except Exception as e:
#    print(e)    #returns the message of the error
#except Exception:
#    print(Exception) #returns a class exception
except TypeError:
    print('check the type of the input')
except ValueError:
    print('Invalid entry enter only integer values')
except ZeroDivisionError:
    print('Division is zero is not possible')
except NameError:
    print('check the name of the variable properly') #if any name is given with error returns nameerror
except IndexError:
    print('List index out of range,give correct index')
except AttributeError:
    print('Check name and write properly')



#Handling Multiple Exceptions
try:
    l = list(map(int,input('Enter values:').split(',')))
    result = l[5]
    print(result)
    l.apped(8)
    print(l)
except (IndexError,AttributeError) as e:   #can handle both exceptions
    print(e)
    l = int(input())
    print(l)


#BMI --> bmi = weight/(height**2)
#Feet --> 12 inches --> 1inch --> 2.54cm
while True:
    try:
        weight=int(input("enter the weight in kgs:"))
        height=float(input("enter the height in metres:"))
        if weight>0 and height>0:
            break   #stops the flow of the execution of statements
            #continue  skips current oteration and continues statements
            #pass
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print(f'Make sure to enter weight as integer only, height also as number')
bmi=(weight)/((height)**2)
print(bmi)

use exception handling along with jumping statements in functions bmi task


Scope of variables --> Scope is basically the region/area where it is accessible
 Local Scope, Global Scope
Local Scope --> variables defined inside the function accessible inside 
Global Scope --> Defined outside and can be accessed anywhere in the script
Local variable has high priority over Global variable

 Global keyword,Enclosing Scope(Nested functions non local Keyword)


#Scope of variables
#Local Scope
def display():
    """Usage of Local Scope"""
    name = 'Codegnan' #local variable
    print(name)
display()
#print(name)  it raises NameError



#Global Scope
place = 'Hyderabad' #gloabl variable
def display():
    """Usage of Local&Global Scope"""
    name = 'Codegnan'  #local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)


count = 20
def data():
    """Usage of global Keyword"""
    global count      #modifying global variable inside function and accessible outside the function
    #count = 5   local variable
    count = count + 5   #if we dont use global inside function count is not recognised and get Unboundlocal Error
    print(f'inside {count}')
data()
print(f'outside {count}')



#Enclosing Scope
def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10   #if there is nonlocal we get unboundlocal erro
        print(f'inside is {count}')
    inner()
    print(f'outer is {count}')
outer()
'''


#Built-in Functions --> variable BuiltinScope
len = 56
print(len + 4)  #take len as variable

print(len('codegnan'))  #TypeError as int object is not callable





















