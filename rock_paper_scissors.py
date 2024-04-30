import random  ## import the random libraly

CHOICES = ['rock', 'paper', 'scissors']


def play(): ## defining a main func
    user = input(f'Choose one {CHOICES}: ')
    computer = (random.choice(CHOICES))
    print('Computer choice is: ', computer)

    winner = None

    if user.lower() not in CHOICES: ## handle the user input.
        raise ValueError('Please select valid choice.')

    if user == 'rock' and computer == 'paper':
        winner = 'computer'

    elif user == 'rock' and computer == 'scissors':
        winner = 'user'

    elif user == 'paper' and computer == 'scissors':
        winner = 'computer'

    elif user == 'paper' and computer == 'rock':
        winner = 'user'

    elif user == 'scissors' and computer == 'rock':
        winner = 'computer'

    elif user == 'scissors' and computer == 'paper':
        winner = 'user'

    elif user == computer:
        print('Tie game !')

    return winner


result = play() ## calling the func

points = { 
        'user': 0,
        'computer': 0,
    }

if result:
    points[result] += 1

print(points)

while True: ## Endless playing if user decide.
    restart = input('To restart press "r", to exit press everything else. ')
    if restart.lower() == 'r':
        play()
        points[result] += 1
        print(points)
    else:
        raise SystemExit

