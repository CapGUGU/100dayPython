import random

choice = ['rock','paper','scissors']

userChoice = input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n')
userChoice = int(userChoice)
print(f'You chose {choice[userChoice]}')

machineChoice = random.randint(0, 2)
print(f'Computer chose {choice[machineChoice]}')
if userChoice < 0 or userChoice > 2:
    print('You typed an invalid value')
elif userChoice == 0 and machineChoice == 2:
    print('You win!')
elif userChoice == 2 and machineChoice == 0:
    print('You lose!')
elif userChoice < machineChoice:
    print('You lose!')
elif userChoice == machineChoice:
    print('Draw!')
elif userChoice > machineChoice:
    print('You win!')
