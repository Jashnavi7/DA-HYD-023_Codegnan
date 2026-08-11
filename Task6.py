#Text case Converter
a=input("enter string:")
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())
print(a.casefold())

b=input("enter string:")
print(b.upper())
print(b.lower())
print(b.title())
print(b.capitalize())
print(b.swapcase())


#Username Validator
a=input("Enter the string:")
while a!="quit":
    if a.isalnum():
        print("The username contains  letters and numbers")
    else:
        print("The username does not only contains letters and numbers")
    if a.isidentifier():
        print("Valid python identifier")
    if a.isalpha():
        print("The username contains only letters")
    if a.isascii():
        print('It is ascii value')
    if 'a' <= a[0] <= 'z' or 'A' <= 'Z':
        print('String begins with letter')
    a=input("Enter the string:")    


#Charcater and Text Analyzer
text = input('Enter text:')
letter_count = 0
digit_count = 0
space_count = 0
printable_count = 0
for i in text:
    if i.isalpha():
        letter_count += 1
    if i.isdigit():
        digit_count += 1
    if i.isspace():
        space_count += 1
    if i.isprintable():
        printable_count += 1
print('Letters:',letter_count)
print('Digits:',digit_count)
print('Spaces:',space_count)
print('Printables:',printable_count)
print('Title Case:',text.istitle())
print('Lower Case:',text.lower())
print('Upper Case:',text.upper())


#Formatted Student Report:
name = []
marks = []
grade = []
for i in range(3):
    n = input('Enter name:')
    m = int(input('Enter marks:'))
    name.append(n)
    marks.append(m)
    if 80 <= m <= 100:
        g = 'A'
    elif 60 <= m <= 79:
        g = 'B'
    elif 40 <= m <= 59:
        g = 'C'
    else:
        g = 'Fail'
    grade.append(g)
print('STUDENT REPORT'.center(25))
print('Name'.ljust(10),'Marks'.ljust(10),'Grade'.ljust(10))
for i in range(3):
    print(name[i].ljust(10),str(marks[i]).ljust(10),grade[i].ljust(10))
       
