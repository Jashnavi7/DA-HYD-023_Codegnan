'''
Operator Overloading --> Operators(+,-,*,/) --> Operators will behave in a different way as per user defined objects...

#Addition,Concatination,Merging
print(2+4)    #Addition
print('Jash'+'navi')    #Concatination
print([1,2]+[3,4])     #Merging

#print(3.__add__(4))   #cannot pass numbers directly
a = 12;b=13
print(a.__add__(b))    #__add__(self,other) --> Magic method
a = [12,13];b = [14,15]
print(a.__add__(b))     #Merging
print(a.__len__())   #len(a)
print(a.__mul__(2))  #prints another list


#lets apply the above scenario to Hotstar watch History
class WatchHistory:
    """Define the no.oh hours"""
    def __init__(self,hours):
        self.hours = hours
Jash = WatchHistory(12)
print(Jash.hours)
varsh = WatchHistory(15)
print(varsh.hours)
#print(Jash+varsh)    #returns typeerror because + cant add two classes without attributes
print(Jash.hours + varsh.hours)   #we have to write attributes by the side of class
'''

#Prefarable way is usage of __add__()
class WatchHistory:
    """Define the no.oh hours"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):   #other here refers to other input which assigns to others to add it to hours
        return self.hours + other.hours
    def __str__(self):
        return f'WatchHistory is {self.hours}'
Jash = WatchHistory(12)
print(Jash)
print(Jash.hours)
varsh = WatchHistory(15)
print(varsh)
print(varsh.hours)
print(Jash + varsh)   #here we dont use attributes as we used __add__() method we can directly use operator(+)
