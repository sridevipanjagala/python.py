import random

while True:
    print('Enter choice \n1. Rock \n2. Paper \n3. Scissor\n')
    choice = int(input("user's turn: "))
    
    while choice > 3 or choice < 1:
        choice = int(input('Enter valid input: '))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
        
    print('User choice is:', choice_name)
    print("Now computer's turn...")
    
    comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
        
    print('Computer choice is:', comp_choice_name)
    print(choice_name + " vs " + comp_choice_name)
    
    if ((choice == 1 and comp_choice == 2) or 
        (choice == 2 and comp_choice == 1)):
        print('Paper wins...')
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or 
         (choice == 3 and comp_choice == 1)):
        print('Rock wins...')
        result = 'Rock'
    elif ((choice==1 and comp_choice==1)or (choice==2 and comp_choice==2)or (choice==3 and comp_choice==3)):
        print('Game draw')
        result = 'Draw'
    else:
        print('Scissor wins...')
        result = 'Scissor'
    if result == 'Draw':
        print('Game draw')
    if result == choice_name:
        print('User wins...')
    if result == comp_choice_name:
        print('Computer wins')
    
        
    print('Do you want to play again? (Y/N)')
    ans = input()
    if ans == 'n'or ans=='N':
        break

print('Thank you for playing')
print('hello world')

