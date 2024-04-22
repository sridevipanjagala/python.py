print('hello world')
l=[1,2,3,4,5,6,7,8,9]
sum=0
for i in l:
    sum=sum+i
print(sum)

m=[1,3,5,7,9,0]
for j in m:
    print(j) #if print (m) the list will repeat number of elements times 
else:
   print('list is over we are out side')

#range function
print(range(10))
print(list(range(10)))

print(range(3,8))
print(list(range(3,8)))

print(list(range(2,20,5)))

#range function in for loop
l=['sun','moon','earth']
for i in range(len(l)):
    print(l[i])

l=[1,2,3,5]
for i in range(len(l)-1):
    print(l[i])

#while loop program
num=9
i=1
sum=0
while i<=num:
    sum=sum+i
    i=i+1
print(sum)


count=4
i=0
while(i<=count):   #first here i will be 0 then 1,then,2,3,4,5 then loop will break
    print('sridevi')
    i=i+1 #incrementor
else:
    print('we are out side the loop')

#break statement terminate the loop 
for val in 'abcde':
    if val=='d':
        break
    print(val)
print('we are out the loop')    

for val in 'sridevi':
    if val=='i':
        break
    print(val)
    if val=='r':
        break
    print(val)
print('we are out side the loop')

for val in 'sridevi':
    if val=='d':
        break
    else:
        print('we are in else')
        print(val)
print('we are out the loop')        

#continue will skip the loop
for value in 'sridevi':
    if value=='v':
        continue
    print(value)
print('out side the loop')    


for value in 'earth':
    if value=='t':
        continue
    else:
        print('we are in else')
        print(value)
print('we are in out of loop')

for value in 'devi':
    if value=='d':
        continue
    else:
        break
    print(value)
print('out side the loop')   

#function 
def greet(name,place):
    print(name+','+place)
greet('sridevi','chinthakunta')

def mul(y):
    return y*y
print(mul(5))

#default arugument
def function(name,msg='Hello'):
    print('my name is',name+','+msg)
function('sridevi')
function('sridevi','I am a programmer')

#function with for loop and star indicate that n number of names can be given
def stu_name(*name):
    for names in name:
        print('my name is',names)
stu_name('sridevi','pavan','ruthvik','chervik')

#factorial program in function with recursion
def factorial(k):
    if k==1:
        return 1
    else:
        return(k*factorial(k-1))
print('factorial value of given number is',factorial(5))

#lambda function
mul=lambda x:x*x
print(mul(5))

sridevi_list=[1,2,3,4,5,6,7,8,9]
newlist=list(filter(lambda x:(x%2==0), sridevi_list))
newlist1=list(filter(lambda x:(x%2!=0), sridevi_list))
print(newlist)
print(newlist1)

#map function
list1=[1,2,3]
list2=[4,5,6]

result=list(map(lambda x,y:x+y,list1,list2))
print(result)

list3=[1,2,3]
list4=[4,5,6]
result1=list(map(lambda x,y:x*y,list3,list4))
print(result1)

list5=[1,2,3,4,5,6,7,8,9]
result2=list(map(lambda x:x*5,list5))
print(result2) #here also specify the list like print(list(result2))

#math library program
import math
print('value of pi',math.pi)
print('value of e is',math.e)
print(math.log10(10))
print(math.factorial(5))
print(math.sqrt(27))
import math
print(math.pow(2,4))
print(math.ceil(5.567))
print(math.floor(10.567))

#exception program or exception handling
import sys
random=['b',0,5]
for entry in random:
    try:
        print('The entry is',entry)
        d=1/int(entry)
        break
    except:
        print('oops!!',sys.exc_info(),'occurred')
        print('next entry')
print('the reciprocal of',entry,'is',d)


#class,object and constructor

class myclass:
    a=100   
    def func(self):
        print('sridevi')

print(myclass.a)
print(myclass.func(1)) #we did not used return statement so function use none


class myclass1:
    b=50
    def mul(x):
        print(x*x)
print(myclass1.mul(10))

# defining object in python

class sridevi:
    a=100
    b=200
    def func(self):
        print('Inside a function')
print(sridevi.func(1))


class ruthvik:
    a=500
    b=600
    def func(self):
        print('inside a function')
object=ruthvik()
object1=ruthvik()
print(object.a)
print(object.b)
print(object.func())
print(object1.func())


#constructors in python program

#default constructor in python 
class geek:
    def __init__(self):
        self.geek='geeks' #constructor

    def print_geek(self):
        print(self.geek) #method

obj=geek()
obj.print_geek()

class add:
    first=0
    second=0
    addition=0

    def __init__(self,f,s):
        # Define the constructor method '__init__' which initializes the object with two parameters 'f' and 's'
        self.first=f
        # Assign the value of 'f' to the instance variable 'first'
        self.second=s
         # Assign the value of 's' to the instance variable 'second'
    def display(self):
         # Define a method named 'display' which displays the values of 'first', 'second', and 'addition'
        print('first number is',self.first)
        # Print the value of 'first'
        print('second number is',self.second)
         # Print the value of 'second'
        print('addition is',self.addtion)
            # Print the value of 'addition' (Note: 'addtion' is a typo, it should be 'addition')
    def calculation(self):
         # Define a method named 'calculation' which calculates the sum of 'first' and 'second'
        self.addtion=self.first+self.second
obje=add(100,200)
# Create an instance of the 'add' class with the values 100 and 200, and assign it to the variable 'obje'
obje.calculation()
# Call the 'calculation' method on the 'obje' object to calculate the addition
obje.display()
# Call the 'display' method on the 'obje' object to display the values

#guess the number game in python
import random
print('number guessing game')
number=random.randint(1,20)
#computer will select the number between 1 and 20
chances=0
print('guess the number between  1 and 20')
while (chances<5):
    #user has only 5 chances
    guess=int(input())
    if guess==number:
        print('congratulations! you win')
        break
    elif guess<number:
        print('the guess is low kindly select higher number')
    else:
        print('your guess is higher kindly select lower number')
    chances+=1
if not chances<5:
    print('you loss!!!,the number is',number)

    #rock, paper, scissors game in python
import random
while true:
    print('Enter choice \n1.Rock \n2.Paper \n3.Scissor\n')
    choice=int(input("user's turn"))
    while choice>3 or choice<1:
        choice=int(input('Enter valid input'))
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissor'
    print('user choice is:',choice_name)
    print("now computer's turn...")
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'
    print('computer choice is..'+comp_choice_name)
    print(choice_name+"V/S"+comp_choice_name)
    if ((choice==1 and comp_choice==2) or (choice==2 and comp_choice==1)):
      print('paper wins...')
      result="Paper"
    elif((choice==1 and comp_choice==3)or (choice==3 and comp_choice==1)):
        print('rock wins...')
        result='Rock'
    else:
        print('Scissor wins...')
        result='Scissor'

    if result==choice_name:
        print('user wins...')
    else:
        print('computer wins...')
    print('do you want to play again? (Y/N)')
    ans=input()
    if ans=='n' or ans=='N':
        break
    print('thank you for playing')





