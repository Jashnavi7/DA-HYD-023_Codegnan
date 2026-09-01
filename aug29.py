'''
modules --> a module is a python file containing variables,functions,objects --> import keyword is used
'''
def greeting():
    """simple greeting function"""
    return "Welcome to codegnan"
print(greeting())

details = {'company': 'codegnan','batch':'da-23','place':'hyd'}
print(__name__) #returns the name of file #if accessing inside the same file then __name__ is always __main__ but for outside files the __name__ is user used file name not __main__
if __name__ =="__main__":
    print(greeting())

print(greeting())