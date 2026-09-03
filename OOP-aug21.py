#encapsulation and consturctor
'''
constructor --> instance methods-->public attribute
Encapsulation

constructor-->it is a special method (__init__())
--> which will automatically initialize the attributes and when the obj is created
--> parameterized constructor = when the constructor have parameters
--> non parameterized constructor = when the constructor have no parameters
'''

##multiple objects with diff data and the data is given at the time of object creation i.e. constructor
#parameterized constructor
class Cars:
    def __init__(self,brand,name,color,price):
        self.brand=brand
        self.name=name
        self.color=color
        self.price=price
    def display(self):
        print(f"Car brand is {self.brand}-->name is {self.name}-->color is {self.color}-->price is {self.price}")
c1=Cars("bmw","sedan","black",650000)
c1.display()
print(c1.__dict__)
#c2=Cars()          #--> error __init__() missing 4positional arguments
#c2.display()

#non parametrized constructor
class Cars:
    def __init__(self):
        self.brand="bmw"   #public attribute--> created inside the class and can be modified for any obj 
        self.name="seden"  #if self is not used then we get attributeError as variable is not defined
        self.color="black"
        self.price="50lkhs"
    def display(self):  #instance method --> methods below the constructor
        print(f"Car brand is {self.brand}-->name is {self.name}-->color is {self.color}-->price is {self.price}")
c1=Cars()
c1.display()
print(c1.__dict__)

#encapsulation: most imp features in OOP
'''--> binds(bundles) the data (attributes) and the methods (behaviour) into single unit(class) that are used by the multiple obj
-->attributes == public,protected,private
'''
#Public attributes --> attributes defined inside the class and can be modified outside the class
class CodegnanPortal:
    """codegnan portal with only users"""
    def __init__(self,username):
        self.user=username #public attribute created inside the class
    def display(self):
        print(f"student name is {self.user}")
u1=CodegnanPortal("harshu")
u1.display() 
u1.user="harika"    ##here username is modified for obj outside the class
u1.display()
print(u1.__dict__)  ##here key is the variable used for value inside the class {user:"harika"} -->updated value is printed
u2=CodegnanPortal("Nani")
u2.display()


#protected attribute --> we use single underscore _ before the variable name --> _user
#--> these attributes can be modified outside the class and even accessible in sub classes
class CodegnanPortal:
    """codegnan portal with only users"""
    def __init__(self,username,_otp):
        self.user=username #public attribute created inside the class
        self._otp=_otp
    def display(self):
        print(f"student name is {self.user} ")
        print(f"student received the otp {self._otp}")
u1=CodegnanPortal("harshu",'5654')
u1.display() 
u1._otp="6761"    ##here username is modified for obj outside the class
u1.display()

#private attributes -- we use double underscore before the variable name --> __password
#--> accessible only inside the class and cannot be modified
class CodegnanPortal:
    """codegnan portal with only users"""
    def __init__(self,username,otp,password):
        self.user=username
        self._otp=otp
        self.__password=password
    def display(self):
        print(f"student name is {self.user}")
        print(f"student received otp {self._otp}")
        print(f"student password is {self.__password}")
u1=CodegnanPortal("harshu",6761,"nani")
u1.display()
print(u1._otp)
#print(u1.__password) #AttributeError -- as password is private attribute so cannot be accessed outside the class
print(u1.__dict__)
print(u1._CodegnanPortal__password) #NameMangling -- used to retrive the private attributes


#in above case we use Namemangling but the right way is to use getter() and setter()

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
u1=CodegnanPortal("harshu","6761","nani")
print(u1.get_password()) #used to retrive the private attributes
u1.set_password("nani765432") #used to modify the private attributes
print(u1.get_password())

#u1.display()

