#Student Marks Manager

marks = []
for i in range(3):
    mark = int(input('Enter marks:'))
    marks.append(mark)
print(marks)
marks.insert(0,90)
marks.extend([75,85])
print(marks)
if 75 in marks:
    marks.remove(75)
    print(f'marks:{marks}')
print(marks.pop())
print(f'Final marks list: {marks}')
print(f'Length of marks: {len(marks)}')


#Number List Analyser
numbers = [20,10,30,20,40,20]
numbers.sort()
print(f'Ascending order of list:{numbers}')
numbers.reverse()
print(f'Descending order of list: {numbers}')
search = int(input('Enter a number:'))
if search in numbers:
    print('Number found')
    count = numbers.count(search)
    print(f'Count of number:{count}')
    index = numbers.index(search)
    print(f'First index: {index}')
else:
    print('Number not found..')
print(f'Smallest Value:{min(numbers)}')
print(f'Largest Value:{max(numbers)}')
print(f'Total:{sum(numbers)}')


#Even and Odd number Separator

numbers = [10,15,20,25,30,35]
even = []
odd = []
for i in numbers:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f'Even List: {even}')
print(f'Odd List: {odd}')
print(f'First 3 values:{numbers[:3]}')
print(f'Last 3 values:{numbers[-3:]}')
backup = numbers.copy()
numbers.clear()
print(f'Original List: {numbers}')
print(f'Backup List:{backup}')


#Unique Name Manager

names = ['Asha','Rahul','Asha','John','Rahul']
sets = set(names)
sets.add('Meera')
sets.update({'Arun','Priya'})
print(f'Names:{sets}')
if 'John' in sets:
    sets.remove('John')
    print(f'Names:{sets}')
print(sets.discard('David'))
for ch in sets:
    print(ch)


#Courses Student Comparision

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"} 
total_students = python_students.union(da_students)
print(f'Total Studens: {total_students}')
both = python_students.intersection(da_students)
print(f'Students learning both courses: {both}')
python = python_students.difference(da_students)
print(f'Students learning only python:{python}')
one_course = python_students.symmetric_difference(da_students)
print(f'Students learning only one course:{one_course}')
subset = da_students.issubset(python_students)
print(f'Subset: {subset}')
superset = python_students.issuperset(da_students)
print(f'Superset:{superset}')
disjoint = python_students.isdisjoint(da_students)
print(f'Disjoint:{disjoint}')

