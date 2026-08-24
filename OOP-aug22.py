#create a class with car brand,name color,price 
'''class Cars:
    def details(self,brand,name,color,price):
        self.brand = brand
        self.name = name
        self.color = color
        self.price = price
    def display(self):
        print(f'car brand is {self.brand} , name is {self.name}, color is {self.color}, price is {self.price}')
first = Cars()
first.details('Toyota','Innova Crysta','white',1500000)
first.display()


Constructor --> Instance methods --> public Attributes
Encapsulation
Constructor --> It is a special method (__init__())
which will automatically initialize the attributes and the method to the object
constructors are 2 types:
 parameterized,non parametrized
parameterized --> have parameters in function
Non parameterized --> dont have parameters


#paratemeterized Constructor
class Cars:
    """Understanding the usage of constructor in OOP"""
    def __init__(self,brand,name,color,price):
        self.brand = brand
        self.name = name
        self.color = color
        self.price = price
    def display(self):
        print(f'car brand is {self.brand} , name is {self.name}, color is {self.color}, price is {self.price}')
first = Cars('Tata','Nexon','black',900000)
first.display()

#Non-paratemeterized Constructor
class Cars:
    """Understanding the usage of constructor in OOP"""
    def __init__(self):
        self.brand = 'BMW'
        self.name = 'Sedon'
        self.color = 'Black'
        self.price = 9000000
    def display(self):
        print(f'car brand is {self.brand} , name is {self.name}, color is {self.color}, price is {self.price}')
first = Cars()
first.display()

Encapsulation --> it is one of the main feature of OOP
It binds (bundles) the data (attributes) and the methods(behave) into single unit(class)
Attributes --> public,private,protected
public attributes--> Attributes defined inside the class() and can be modified outside the class
Protected attributes --> we use single underscore before an attribute moreover it can be modified also outside the class and even accessible in subcalsses
Private attributes --> we use specail notation as double underscore such as __password accessible only inside the class and cant be directly modify


#public attribute
class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username):
        self.user = username  #public attribute
        #to access details
    def display(self):
        print(f'Student Username is {self.user}')
u1 = CodegnanPortal('Jashnavi')
u1.display()
u1.user = 'vaishnavi'
u1.display()
print(u1.__dict__)   #returns the key value pair like dictionary for attributes


#protected attribute
class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username,_otp):
        self.user = username  #public attribute
        self._otp = _otp  #protected attribute
        #to access details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
u1 = CodegnanPortal('Jashnavi',1234)
u1.display()
u1._otp = 4321
u1.display()

#private attribute
class CodegnanPortal:
    """Codegnan portal with users"""
    def __init__(self,username,_otp,__password):
        self.user = username  #public attribute
        self._otp = _otp  #protected attribute
        self.__password = __password
        #to access details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
        print(f'Student password is {self.__password}')
u1 = CodegnanPortal('Jashnavi',1234,'admin789')
u1.display()
print(u1.__dict__)
print(u1._CodegnanPortal__password)
'''
#getter setter
class CodegnanPortal:
    """codegnan portal with only users"""
    def __init__(self,username,otp,password):
        self.user=username
        self._otp=otp
        self.__password=password
    #usage of getter()
    def get_password(self):
        return self.__password
    #to modify password
    def set_password(self,new_password):
        if (len(new_password)<=6):
            print("password need to be modified")
        else:
            self.__password=new_password
            print("password is updated")
    def display(self):
        print(f"student name is {self.user}")
        print(f"student received otp {self._otp}")
        print(f"student password is {self.__password}")
u1=CodegnanPortal("Jashnavi","6761","admin908")
print(u1.get_password()) #used to retrive the private attributes
u1.set_password("admin765432") #used to modify the private attributes
print(u1.get_password())