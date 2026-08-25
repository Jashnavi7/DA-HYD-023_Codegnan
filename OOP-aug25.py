#superclass with arguments
class Father:
    def __init__(self,property):
        self.property = property
    def father_prop(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    def __init__(self,earning,property):   
        self.earning = earning
        super().__init__(property)     #calling superclass using arguments
    def kid_prop(self):
        print(f'Child property is {self.earning}')
        print(f'Child final propert is {self.earning+self.property}')
obj = Kid(200000,1000000)
obj.father_prop()
obj.kid_prop()  


#whatif child class having same method name as parent class --> Method overriding
#Area of squares or rectangle
#superclass with method
class Square:
    """Method overriding Usage"""
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f'Area of square is {self.x * self.x}')
class Rectangle(Square):
    def __init__(self,x,y):
        self.y = y
        super().__init__(x)     #calling superclass with arguments --> constructor overriding
    def area(self):
        super().area()      #calling superclass with method --> Method overriding
        print(f'Area of Rectangle is {self.x * self.y}')
x,y = map(int,input('Enter the values:').split(','))
obj = Rectangle(x,y)
obj.area()

'''
#Multiple Inheritence
Syntax:
class Parent1:
    ......
class Parent2:
    ......
class Child(Parent1,Parent2):
    ......
'''

class User:
    """First Parent class with user features"""
    def voice_calls(self):
        print('Can make Voice Calls')
class Notifications:
    def notifications(self):
        print('Sending Notifications')
class PremiumUser(User,Notifications):
    def verification_badge(self):
        print('Blue tick verification')
obj = PremiumUser()
obj.verification_badge()
obj.notifications()
obj.voice_calls()

'''   
#Multilevel Inheritence --> Level by Level
class Grandparent:
    .........
class Parent(GrandParent):
    ........
class Child(Parent):
    .....
'''
class User:
    def video_call(self):
        print('Make video calls')
class BusinessUser(User):
    def create_catalog(self):
        print('can create catalog')
class VerifiedBusinessUser(BusinessUser):
    def blue_ticks(self):
        print('Blueticks Enabled')
obj = VerifiedBusinessUser()
obj.video_call()
obj.blue_ticks()
obj.create_catalog()