#while loop example
'''i =1 
while i <=10:
    print ("Number is :",i)
    i += 1
    '''

#infinite loop hobe
'''
i = 1
while i <= 5:
    print(i)
    '''

#for loop example
'''
for i in range(5):
    print(i)
'''
#range function example
'''

for i in range(5):
    print(i)

'''
#list example
'''
fruits = ["apple", "banana", "lichu"]
for fruit in fruits:
    print("Fruit:", fruit)
'''
#string example

name = "Alien"
for letter in name:
    print(letter)

#Loop Control — break & continue

#break example

for i in range(1, 6):
    if i == 4:
        break
    print(i)  
#continue example
    if i == 3:
        continue
    print(i) 
#start, stop, step
    for i in range(1, 10, 3):
    print(i)

