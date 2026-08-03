'''
task:students marks and grade analyzes
90-100-->A
80-89-->B
70-79-->C
60-69-->D
<60-->Fail
#also -ve negative cases should not be allowed and marks should not be greater than 100
'''
#Grade check:
Marks = int(input("Enter your Marks:"))
if Marks>0 and Marks<=100:
    if Marks>=90:
        print("Grade A")
        print("Remark: Outstanding!")
    elif Marks>=80:
        print("Grade B")
        print("Remark: Excellent!")
    elif Marks>=70:
        print("Grade C")
        print("Remark: Good")
    elif Marks>=60:
        print("Grade D")
        print("Remark: Fair, needs improvement")
    elif Marks>=50:
        print("Grade E")
        print("Remark: Poor, needs serious improvement")
    else:
        print("Grade F")
        print("Remark: Failed, needs to reappear")
else:
    print("Invalid Marks Entered")


'''
#PRACTICE
amount=int(input("enter amount:"))
if amount>=500:
    print("Withdraw amount")
else:
    print("Transaction Unsuccessful")

#PRACTICE
number=int(input("enter value:")) 
if number>=0:
    print("Positive value")
elif number<0:
    print("Negative value")
else:
    print("dont enter strings")

'''



#Even odd check:
number=int(input("enter number:"))
if  number>0 and number%2==0:
    print("even number")
elif  number>0 and number%2!=0:
    print("odd number")
elif  number<0 and number%2==0:
    print("negative even number")
elif number<0 and number%2!=0:
    print("negative odd number")
else:
    print("zero is neither odd nor even")



#Season identifier:
season=int(input("enter month number"))
if season  in [12,1,2]:
    print("winter")
elif season  in [3,4,5]:
    print("spring")
elif season  in [6,7,8]:
    print("summer")
elif season  in [9,10,11]:
    print("autumn")
else:
    print("invalid month number")

season=int(input("enter month number"))
if season>0 and season>=12:
    if season==12 or season==1 or season ==2:
        print("winter")
    elif season==3 or season==4 or season==5:
        print("spring")
    elif season==6 or season==7 or season==8:
        print("summer")
else:
    print("autumn")


