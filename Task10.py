#Leap Year
year = int(input('Enter Year:'))
if (year%4==0 and year%100!=0)or year%400 == 0:
    print('Leap year')
else:
    print('Not a leap Year')


year = int(input('Enter Year:'))
while (year%4==0 and year%100!=0) or year%400 == 0:
    print('Leap year')
else:
    print('Not a leap Year')
    

def leap(year):
    if (year%4 == 0 and year%100!=0) or year%400 == 0:
        print('Leap year')
    else:
        print('Not a leap year')
    return 
year = int(input('Enter year:'))
leap(year)
