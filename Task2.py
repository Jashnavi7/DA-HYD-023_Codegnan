#Task:workout with all posiible of slicing and striding on an example
#slicing
name = 'Jashnavi'
print(name[:])  
print(name[1:])    
print(name[:4])    
print(name[2:5])   
print(name[0:5])
print(name[7:2])  
print(name[:90])  
print(name[-1:-6])   
print(name[-5:-2])   
print(name[-5:])
print(name[4:8])
print(name[-6:4])
print(name[1:-8]) 

#striding
sen = 'Iamgoodgirl'
print(len(sen))
print(sen[::])
print(sen[::1])    
print(sen[::2])    
print(sen[1:11:3])
print(sen[2::3])
print(sen[::-1])
print(sen[-9:-1:2])
print(sen[-12::1])
print(sen[-1:-12:1])

#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z-->
#use loops and strings to  return A - Z
for i in range(65,91):
    print(chr(i),end = ' ')
