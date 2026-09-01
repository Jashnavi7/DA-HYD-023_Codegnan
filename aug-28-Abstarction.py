'''
OOP--> Abstraction
'''
#class method --> these are termed by using @Classmethod decorator, it applied for the entire class level data thereby every obj utilisation willb be modified

class Ecommerce:
    """usage of class method and class attribute"""
    company = "flipkart" #class attribute
    delivary_charge=50    
    @classmethod   # must use to create class method, if not used then it is instance method
    def update_delivary(cls): #cls  is same like self to carry the variables and values from the outside of function
        cls.delivary_charge=100
        print(f"delivary charge is {cls.delivary_charge}")
product=Ecommerce()
print(product.company)
print(product.delivary_charge) #50
product.update_delivary() #update delivary_charge to 100 --> permanent change
print(Ecommerce.company) #calling through the class
print(Ecommerce.delivary_charge) # class attribute called by the class name  #100
Ecommerce.update_delivary()
mobile=Ecommerce()
print(mobile.delivary_charge)  #100 as the value is modified 


#applying inheritance and usage of class method and class attributes 
#banking scenario --> rbi --> sbi,kotak..........
# diff attribute names or calling with the class name
class RBI:
    cash=5000000
    @classmethod
    def rbi_cash(cls):
        print(f"Avaiable cash with RBI is {cls.cash}") #cls.cash refers to hdfc cash value  #value overriding
class SBI(RBI):
    pass #using pass we want a class with no attributes and methods
class HDFC(RBI):
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f"HDFC Cash is {cls.cash}")
        print(f"sum of cash is {HDFC.cash+RBI.cash}")  #when parent and child have same cls attributes then we can use class names to access
#a=SBI()
#print(a.available_cash)
#a.rbi_cash()
#SBI.rbi_cash()
b=HDFC()
print(RBI.cash)
print(b.cash)
b.rbi_cash() # cannot modified once defined...hdfc is primary class and give more priority to 30000000 
b.hdfc_cash()

#static method --> it does notb depend on either on object or on the class
#we can create by using the @staticmethod decorator
#it is mainly used as utility or helper functions
class Ecommerce:
    """using the static method"""
    @staticmethod
    def free_delivary(price): # self or cls is not used because static methods do not depend on class or object
        return price>500
u1=Ecommerce()
print(u1.free_delivary(100))
print(u1.free_delivary(600))


#combination of class and static methods
class Ecommerce:
    """usage of class and static method"""
    platform="flipkart"
    @classmethod
    def show_platform(cls):
        print("welcome to the platform")
        print(f"{cls.platform}")
    @staticmethod
    def free_delivary(price):
        return price>500
u1=Ecommerce()
u1.show_platform()
print(u1.free_delivary(600))

#Abstraction---> it is also one of the key feature of OOP, where it shows the only relevant details to user and hides the implementation
#instagram --> uploading photo,upload vedio,reel
#when we need all child classes to follow same pattern
#we have abc module to implement abstraction

import abc
from abc import ABC,abstractmethod
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
    def upload(self):
        print("---------compresing the picture")
        print("edit the picture")
        print("photo uploaded successfully")
    pass
class Vedio(Content):
    def upload(self):
        print("---------vedio started encoding")
        print("vedio editing is in process")
        print("vedio uploaded successfully")
class Reel(Content):
    def upload(self):
        print("---------Adding effects to the reel")
        print("Reel is edited")
        print("Reel uploaded successfully")
content_items=[Photo(),Vedio(),Reel()]  #storing the classes in list and using 1 ojb(list) to create the objecsts to all classes 
for c in content_items: # accessing the each obj from the list of objects 
    c.upload() # accesss upload in the order of the object stored ---photo-->vedio-->reel'''
a=Photo()