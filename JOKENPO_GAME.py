# JOKENPO GAME

from random import randint
from time import sleep

print('=+'*20)
print('Welcome! You are playing Jokenpo! Enjoy!')
print('=+'*20)

print('Select an option: \n[ 0 ] Stone \n[ 1 ] Paper \n[ 2 ] Scissors')


your_choice = int(input('What is your choice? '))
pc_choice = randint(0,2)
options = ('stone', 'paper', 'scissors')
print('='*30)

print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!')

print('*--'*10)
print(f'PC choose {options[pc_choice]} \nYou choose {options[your_choice]}.')
print('*--'*10)
if pc_choice == 0 and your_choice == 1:
    print('You won!')
elif pc_choice == 0 and your_choice == 2:
    print('The computer won!')
elif pc_choice == 1 and your_choice == 0:
    print('The computer won!')
elif pc_choice == 1 and your_choice == 2:
    print('You won!')
elif pc_choice == 2 and your_choice == 0:
    print('You won!')
elif pc_choice == 2 and your_choice == 1:
    print('The computer won!')
else:
    print('We have a tie, play again!')




