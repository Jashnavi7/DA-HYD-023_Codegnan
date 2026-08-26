'''
Polymorphism --> It is also one of the key feature of OOP
poly --> many  morph --> forms
Methods with same name can take different parameters(arguments)
  Method overloading (compile time polymorphism)-->
  Method overriding (runtine polymorphism)
  operator Overloading(+,*) (__add__,__str__ {Dunder method})

Hotstar
 Free User --> can watch the movies with advertisements
 Premium User --> can watch premium content without advertisements
 VIP User --> live content,streaming quality,premium content 
'''

#Method Overloading
class Hotstar:
    """Understand polymorphism"""
    def watch():
        print(f'User logged into Hotstar...Opening home page')
    def watch(self,movie):
        self.movie = movie
        print(f'User watching movie {self.movie}')
app = Hotstar()
app.watch('Leo')
app.watch()          # it returns error as watch() is overload 

'''
1.Method usage with default arguments
2.Method usage with variable length arguments
3.Method usage with type of arguments
'''

#Default arguments
class Hotstar:
    """Method usage with default arguments"""
    def watch(self,movie = None):    #here we are using default arguments
        if movie is None:
            print(f'User logged into Hotstar.....Checking...')
        else:
            self.movie = movie
            print(f'user started watching {self.movie}')
app = Hotstar()
app.watch()
app.watch('7')
app.watch('8')


#variable length arguments
class Hotstar:
    """Method usage with default arguments"""
    def watch(self,*movies):    #here we are using variable length arguments
        if len(movies) == 0:   #Taking length of the arguments to 0
            print(f'User logged into Hotstar.....Checking...')  
        else:
            for i in movies:
                print(f'user started watching {i}')
app = Hotstar()
app.watch()
#movie = map(str,input('enter movies:').split(','))
app.watch('7','8')

'''
Method overloading with type of arguments usage
Hotstar --> one movie at a time
        --> multiple movies at a time
'''

class Hotstar:
    """Method Overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print('Playing content')
            for movies in content:
                print(f'User watching movie:{movies}')
app = Hotstar()
#app.watch() gives error as we dont write any default argument like None
app.watch('7')
app.watch(['7thSense','8-Vasanthalu','1-NenOkkadine','Leo'])   #using type of arguments - giving input in a list



'''
#Method Overriding
 It happens in the scenario of inheritence, where if child class is having method as same as parent class thats where override
 we can use super() or if we create different objects
''' 

class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print('User logged into homepage')
class PremiumUser(Freeuser):
    """Using Inheritence"""
    def watch(self,movie):
        super().watch()  #calling superclass using method
        self.movie = movie
        print(f'User watching {self.movie}')
obj = PremiumUser()
obj.watch('Vikram')
obj1 = Freeuser()
obj1.watch()

