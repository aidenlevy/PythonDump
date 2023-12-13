#Table Top Essential Tools!
#Python CLI based tool for various tools related to table-top games.
#included are a cool dice roller allowing you to pick the amount of sides
# a coinflip function bc why not
# a random card selector
# a random name drawing system given inputs
import random

def diceroll():
    print('How many sides on the Dice?')
    x = int(input('> '))
    print(f'Rolling a {x} sided dice')
    xy = random.randint(1,x)
    print(f'You rolled a {xy} !')
#allows me to let user pick 

def coinflip():
    fl = random.randint(0,1)
    if fl == 0:
        print('Coin Flip:   Heads')
    else:
        print('Coin Flip:   Tails')
#really easy coinflip function bc its just like a 1/2 kinda thing.

def carddraw():
    cd = random.randint(0,3)
    cs = {0:'Hearts',1:'Clubs',2:'Diamonds',3:'Spades'}
    cv = random.randint(1,13)
    cvv = {1:'Ace',11:'Jack',12:'Queen',13:'King'}
    r = cvv.get(cv, str(cv))  # Use the dictionary to get the rank name
    suit = cs[cd]  # Use the dictionary to get the suit name
    print(f'You pulled a {r} of {suit}')

#card draw that shows suit, value
def random_name_pick():
    names = []
    while True:
        print("Enter a name (or type '!draw' to pick from the names):")
        name = input('> ')
        if name.lower() == '!draw':
            break
        names.append(name)
    if not names:
        print("You have 0 names entered\nPlease provide at least 1 more name to continue.")
        return
    random_name = random.choice(names)
    print(f"The random name is: {random_name}")
#a name drawing system for turn based games or selection

while True:
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('Table Top Essential Tools Menu')
    print('')
    print('1: Dice Roll')
    print('2: Coin Flip')
    print('3: Card Draw')
    print('4: Name Drawing')
    print('')
    print('Type   !quit   to terminate the program')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    J = input('> ')
    if J == '1':
        diceroll()
    elif J == '2':
        coinflip()
    elif J == '3':
        carddraw()
    elif J == '4':
        random_name_pick()
    elif J == '!quit':
        print('Quitting...')
        break
    else:
        print('Invalid Choice!')
#Main Menu be like..
