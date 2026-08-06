#Adding price of all products in the cart
product_price = list(map(int,input('Enter prices:').split(' ')))
cost = 0
for price in product_price:
    cost += price
print(cost)
   
#Password analyzer
password = input('Enter password:')
digit_count = 0
upper_count = 0
small_count = 0
schar_count = 0
for i in password:
    if 'A'<=i<='Z':
        upper_count += 1
    elif 'a'<=i<='z':
        small_count += 1
    elif '0'<=i<='9':
        digit_count += 1
    else:
        schar_count += 1
print('Upper Count:', upper_count)
print('Lower Count:', small_count)
print('Digit Count:', digit_count)
print('SpecialCharacter Count:', schar_count)

#Return domain of the email entered
emails = list(map(str,input('Enter email:').split(' ')))
for i in emails:
    print(i.split('@')[1])
    
mail = input('Enter mail:')
print(mail.split('@')[1])

#print history in serial number
#moviesList = list(map(str,input('Enter movie names:').split(' ')))
#for i in moviesList:
#    print(i)
