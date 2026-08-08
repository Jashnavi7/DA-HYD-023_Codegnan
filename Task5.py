#find secret number
Secret = '123'
while 1:               
    entry = input('Enter Key:')
    if Secret == entry:
        print('Key is correct')
        break
    elif Secret < entry:
        print('Key is greater')
    else:
        print('key is lesser')
    print('Try again...')

#OTP verification
otp = 1234
cur_attempt = 0
max_attempt = 7
while cur_attempt < max_attempt:               
    entry =int(input('Enter otp:'))
    if otp == entry:
        print('OTP is correct')
        break
    cur_attempt += 1
    print('Try again...')    
else:
    print('Blocked')

#Taking food orders
orders_count = 0
while 1:
    food_items = input('Enter food item:')
    if food_items == 'exit':
        break
    else:
        orders_count += 1
print('Count of orders:',orders_count)

order = input('Enter food item:')
orders_count = 0
while order != 'exit':
    orders_count += 1
    order = input('Enter food item:')
print('Count of orders:',orders_count)

#Guessing the word
word = 'python'
Chances = 3
attempt = 1
while attempt <= 3:
    entry = input('Enter word:')
    if word == entry:
        print(f'You won! You have {Chances - attempt} chances')
        break
    else:
        print(f'You lost..You have {Chances - attempt} chances')
        attempt += 1
    
