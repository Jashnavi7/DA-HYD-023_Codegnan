'''
OOP --> Class,Object,Methods(__init__())
Encapsulation --> Public,Protected,Private
Inheritance --> It is one of the key feature of OOP where we inherit properties (attributes/methods) from one class to other class (base class{parent call} to derived class{child class})
Features --> Code reusability, Avoiding code duplication, Code maintainability, Polymorphism (Method overriding(super()), method overloading, Operator overloading __ add__,__str__)
WhatsApp --> Personal User, Business user(catalog), Community admin

Types of Inheritence:
    Single Inheritence(Finger Print): One child class inheriting properties from one parent class
    Multiple Inheritence(Mother,Father --> child): One child class inheriting from two parent classes
    Multilevel Inheritence (Grandparent --> Parent --> Child): Level by Level
    Hierarchical Inheritence (multiple child classes): Inheriting properties from single parent class
    Hydrid Inheritence: It can carry one or more type of inheritence

Syntax:-

Single Inheritence:
class baseclass:
    statement(s)..
    ....
class Derivedclass(baseclass):
    ............
    .........

#WhtasApp Scenario --> Personal User
class User:
    """Single Inheritence User"""
    def send_message(self):
        print('Send Message')
    def voice_call(self):
        print('Make voice call')
    def video_call(self):
        print('Make video call')
class BusinessUser(User):
    pass
    def create_catalog(self):
        print('Displaying Products catalog')

u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.voice_call()
u1.video_call()
u1.create_catalog()

#social Media Login
class Users:
    company = 'Codegnan'
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
class Update(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()  
u1 = Update('jashnavi',' Jangili')
print(u1.full_name())
print(u1.company)
u2 = Users('vaish','samudrala')
print(u2.full_name())

#What if we have constructor in child class
#Father --> Kid(Property)
class Father:
    def __init__(self):
        self.property = 1000000
    def father_prop(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    def __init__(self):
        self.earning = 200000
    def kid_prop(self):
        print(f'Child property is {self.earning}')
obj = Kid()
obj.father_prop()
obj.kid_prop()    #returns attribute error has we have constructors in both classes

when we have constructors in both parent and child classes child class constructor overrides parent class constructor
we use super() to overcome it:
 super().__init__()
 super().__init__(args)
 super().method()
'''
class Father:
    def __init__(self):
        self.property = 1000000
    def father_prop(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    def __init__(self):
        super().__init__()  #calling superclass constructor
        self.earning = 200000
    def kid_prop(self):
        #print(f'Child property is {self.earning}')
        print(f'Child final propert is {self.earning+self.property}')
obj = Kid()
obj.father_prop()
obj.kid_prop()  
