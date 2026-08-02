'''
Task: Student marks and grade analyzer
90-100 -->'A'
80-89 -->'B'
70-79 -->'C'
60-69 -->'D'
<60 --> 'Fail'
# also -ve cases should not be entered and marks should not greater than 100
'''

marks=int(input("Enter Student marks:"))
if marks <=100 and marks>=90:
    print("Grade:A")
elif marks <=89 and marks>=80:
    print("Grade:B")
elif marks <=79 and marks>=70:
    print("Grade:C")
elif marks <=69 and marks>=60:
    print("Grade:D")
elif marks<60 and marks>=0 :
    print("Fail")
else:
    print("marks should not be entered in -ve cases and greater than 100")

#or   

marks=int(input("Enter Student marks:"))
if marks >0 and marks<=100:
    if marks>=90:
        print("Grade:A")
    if marks <=89 and marks>=80:
        print("Grade:B")
    if marks <=79 and marks>=70:
        print("Grade:C")
    if marks <=69 and marks>=60:
        print("Grade:D")
    if marks<60 and marks>=0:
        print("Fail")
else:
    print("marks should not be entered in -ve cases and greater than 100")
    



#Voter Eligibility checkcase -->make sure to satisfy all possible conditions
#>=18 -->Access
#<18 -->no of years eligibility should tell
#negative values -->not acceptable

age=int(input("enter age:"))
if age>=18 and age<=100:
    print("User have Access")
elif age<18 and age>=0:
    print("user need to wait more",(18-age),"years")
else:
    print("Negative values are not acceptable and age should be less than 100 is acceptable")


#output -->print()-->we can pass any values also use sep and end
#Output Formatting -->old style formatting(using commas)
#% usage (%f,%d),.format() usage,fstring notation

a,b=7,9
print(a)
print(b)
print(a,b)
name="Codegnan";batch="Data Analytics"
print(name,batch) #by default sep having space
print(name,batch,sep=',')
print(name,batch,sep='------>')
#end='\n' -->new line , '\t'-->tab space
print(name,batch,end='\t')
print(a,b)
print("Hyderabad")
      


name='Codegnan';age=7;batch='DA-023';place='Hyd'
#Usage of commas
print(batch,'is in',name) #variables and msg to be seperated by comma
print(name,'is in',place,'age is',age,'years')

#Old style formatting -->%d-->integer, %s-->String, %f-->float
salary = 24253.256
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
print("His Salary is %.1f"%(salary)) #%.1f-->rounding to 1 decimal

#.format() usage
print("{} is in {}".format(name,place)) # oder matters

# fstring usage (more recommended) 
print(f'{name} is in {place}')
print(f'{"Srividya"} is in {name}')
      

























