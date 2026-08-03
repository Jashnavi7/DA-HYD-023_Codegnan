'''
Control statements:
Repitition Statments(Loops) --> for,while,(for with else),(while with else)
Jumping Statments --> break,continue,pass
Loops --> loops are helpful for repetition (automative tasks)


for:keyword will be helpful to itarate over a sequence / range
Syntax:
for <temp_var> in sequence/range:
     statemen(s).....
     .......
#range(start,stop,step) --> by default range picks 0 as starting value
range(stop) --> default 0 ends at stop-1
range(start,stop,step) --> here step --> interval...
'''
for i in range(10):
    print(i)           #in this case we got 10 iterations

for i in range (1,10):        
    if i > 5:
        print(f'Value i  is {i}')      #greater than 5 
        
for i in range (1,10):
    if i > 5 and (i%2==0):
        print(f'Value i  is {i}')     #even and greater than 5

for i in range (1,10,4):
    print(i)
print('Done')

#print -10 to -1:
for i in range(-10,0,1):
    print(i)

names = ['jash','jangili','patel']
print(len(names))      #len(object) --> returns the number of items in the container
for name in names:
    if name == 'jash':
        print(f'student name is {name}')

#Caluculate the sum of first 10 numbers:
result = 0
for i in range (11):
    result = result + i
print(result)

#calculate sum of first 10 even numbers:
result = 0
for i in range(21):
    if i%2 == 0:
        result += i
print(f'sum of first 10 even numbers is {result}')
'''
understanding the loops using fitcheck strak example:
work_out --> 1 , work_out_missed --> 0
result variable longest streak
'''
work_log = [0,1,0,0,0,0,1,1,1,0,1]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0;
print(f'Longest streak is {longest_streak}')
