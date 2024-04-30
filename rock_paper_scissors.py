import random

CHOICES = ['rock', 'paper', 'scissors']


def play():
    user = input(f'Choose one {CHOICES}: ')
    computer = (random.choice(CHOICES))
    print('Computer choice is: ', computer)

    winner = None

    if user.lower() not in CHOICES:
        raise ValueError('Please select valid variable.')

    if user == 'rock' and computer == 'paper':
        winner = 'computer'
        print('Winner is computer !')

    elif user == 'rock' and computer == 'scissors':
        winner = 'user'
        print("Winner is user !")

    elif user == 'paper' and computer == 'scissors':
        winner = 'computer'
        print('Winner is computer !')

    elif user == 'paper' and computer == 'rock':
        winner = 'user'
        print('Winner is user !')

    elif user == 'scissors' and computer == 'rock':
        winner = 'computer'
        print('Winner is computer !')

    elif user == 'scissors' and computer == 'paper':
        winner = 'user'
        print('Winner is user !')

    elif user == computer:
        print('Tie game !')

    return winner


result = play()

points = {
        'user': 0,
        'computer': 0,
    }
if result:
    points[result] += 1

print(points)

while True:
    restart = input('To restart press "r", to exit press everything else. ')
    if restart.lower() == 'r':
        play()
        points[result] += 1
        print(points)
    else:
        raise SystemExit

