#Usage of else with for --> the else keyword will only be executed when the loop is completely done without any break

#for else:
work_log = [0,1,0,0,0,0,1,1,1,0,1]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0;
else:
    print(f'Longest streak is {longest_streak}')
#In above case the entire loop execution is donr we get the result of else block

work_log = [0,1,0,0,0,0,1,1,1,0,1]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0;
else:
    print(f'Longest streak is {longest_streak}')
print('Executed')
#In this case tha break keyword stops the execution,the loop is terminated and else block will not execute

#for else in notification scenario
notifications = [0,0,0,0]
for notification in notifications:
    if notification == 1:
        print('unread notification')
else:
    print('All Caugth Up')

notifications = [0,0,0,1]
for notification in notifications:
    if notification == 1:
        print('unread notification')
        break
else:
    print('All Caugth Up')

#Try to give notifications from user using list
notifications = list(map(int,input('Enter values: 0 0r 1:').split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print('Unread Notification')
        break
else:
    print('All caugth up')

'''
while --> it relies on condition, it will be completely executes until the condition is satisfied..

Syntax for while:
while<condition>:
    Statement(s)...
    ......

while True:
    print('Yes')   #runs an infinite loop --> to stop press ctrl+c(Keyboard Interrupt)
'''
i = 0  #Initializer
while i<= 10:
    print(i)
    i += 1  #counter
#while should have an initialized variable and a counter                 

#get the counter from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

i = 0
while i < 10:
    print(10 - i)
    i += 1

#Banking Scenario --> PIN authentication if more than 3 attempts --> account blocked..
pin = '2345'
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    enter_pin = input('Enter pin:')
    if enter_pin == pin:
        print('Login succesful')
        break    #using break --> stops loop execution
        #continue --> it holds for this condition and skips to the next part of the code
    else:
        print('Entered wrong pin.Try again...')
        current_attempt = current_attempt + 1
else:
    print('Account blocked.Try after 24 hours...')
    
    
