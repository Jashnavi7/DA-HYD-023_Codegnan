#print history in serial number
moviesList = list(map(str,input('Enter movie names:').split(' ')))
i = 1
for movie in moviesList:
    print(i,movie)
    i += 1

movies = input('enter').split()
i = 1
for movie in movies:
    print(i,movie)
    i += 1

#fibonacci series
number = int(input('Enter Number:'))
a = 0
b = 1
for i in range(number):
    print(a,end=' ')
    c = a + b
    a = b
    b = c
   
number = int(input('Enter Number:'))
a = 0
b = 1
i = 0
while i < number:
    print(a,end=' ')
    c = a + b
    a = b
    b = c
    i += 1

#write a python program to calculate the innings of a batsman==>list:4,6,1,0,2,4,0,6
runs = list(map(int,input('Enter runs:').split(',')))
score = 0
dotballs =0
boundaries = 0
for i in runs:
    score += i
    if i == 4 or i == 6:
        boundaries += 1
    elif i == 0:
        dotballs += 1
print('Total score:',score)
print('Boundaries:',boundaries)
print('Dotballs:',dotballs)   

#pattern checking
pattern = 'Jash'
max_attempts = 5
cur_attempt = 0
while cur_attempt < max_attempts:
    trail = input('Enter pattern:')
    if trail == pattern:
        print('Phone unlocked')
        break
    else:
        cur_attempt += 1
else:
    print('Phone locked...try again after 30 seconds')
    
#ATM pin
pin = '1234'
max_attempts = 3
cur_attempt = 0
while cur_attempt < max_attempts:
    trail = input('Enter pin:')
    if trail == pin:
        print('Login succesful')
        break
    else:
        cur_attempt += 1
        print('Enter wrong pin...Try again')
else:
    print('Limit reached...try again after 24 hours')
