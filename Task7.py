#Task1
#create a nested tuple and work on slicing,striding,list functions:
a = ('qwe','wsd','srgbc',[12,45,67],'vfghn')
print(a)
print(a[1:4])
print(a[:-1])
print(a[::2])
print(a[3][1:])
a[3].append('Jash')
print(a)
a[3].append([12,56,9])
print(a)
a[3].pop()
print(a)
a[3].remove(67)
print(a)
del a[3][2:4]
print(a)
a[3].insert(0,'jsg')
print(a)
a[3].clear()
print(a)
print(a.count('qwe'))


#Task2
#Take a user input as string , do this in two ways
word = input('Enter word:')
name = []
new = []
for ch in word:
    if ch not in new:
        new.append(ch)
        count = word.count(ch)
        if count > 1:
            print(f'{ch} is repeating {count} times')


name = input('Enter word:')
word = []
new = []
word.extend(name)
print(word)
for ch in word:
    if ch not in new:
        index = []
        new.append(ch)
        count = word.count(ch)
        if count > 1:
            start = 0
            print(f'{ch} is repeating {count} times')
            #print(f'index = [{word.index(ch)},{word.index(ch,word.index(ch)+1)}]')
            for i in range(count):
                index.append(word.index(ch,start))
                start = word.index(ch,start)+1
            print(f'Index = {index}')
            
