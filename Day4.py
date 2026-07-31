'''
Identity Operators --> checks identity of an object
As we have Lists(Mutable collection) both b and c lists will have different id.where as values are same
'''

a = 5
print(id(a))
b = [1,3,4,5]
print(id(b))
c = [1,3,4,5]
print(id(c))
print(b is c)    #False
print(b == c)    #True
print(b != c)
print(b is not c)

'''
Bitwise operators --> we perform bitwise operators over operands
 &(and) , |(or) , ^(XOR) , shifting operators(<<,>>)
 Number will be converted to binary format
 Leftshift operator(<<) --> shiting to left by position ,RightShift(>>) --> shiting right by position
''''

#Bitwise operators
print(5&3)  #both numbersconverts to binary and bitwise &(AND) is performed
print(5|3)    #OR(|)
print(5^3)   #XOR(^)
print(5 and 3)   #here logical and checks for existence of both
print(5 or 3)   #checks existence of single existence

print(5<<1)    #left shift operation by one position
print(5>>1)
print(6<<2)
print(6>>2)    #right shift operation by 2 positions

'''
Control Block Statements:
    when to execute how to execute
 Conditional statements --> if,else,elif(rely on condition to be executed)
 Repetition statements(Loops) --> for,while

conditional statements
if Keyword:
Syntax:
if<Condition>:
    Statement(s)...
    .....

else Keyword::
Syntax:
else:
    Statements(s)...

if-else usage:
Syntax:
if<Condition>:
    statement(s)
    ....
else:
    Statement(s)...
    ....
'''

#if
age = int(input('Enter age:'))
if age >= 18:
    print('Your age is:',age)

age = int(input('Enter age:'))
if age >= 18 and age in [18,22,30]:
    print('Your age is:',age)

#else
#vote Eligibility
age = int(input('Enter age:'))
if age >=18:
    print('You are eligible and age is:',age)
    print('Access Granted')
else:
    age = 18 - age
    print('you are not eligible,you need to wait for',age,'year(s)')

#same case let's use only nested -->
age = int(input('Enter age:'))
if age > 0:
    if age >= 18:
        print('You are eligible and age is:',age)
        print('Access Granted')
    else:
        age = 18 - age
        print('you are not eligible,you need to wait for',age,'year(s)')
else:
    print('you have entered -ve values/0 enter valid input')
