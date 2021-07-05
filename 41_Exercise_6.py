'''This is a two-player game where each player chooses one object.
As we know, there are three objects, snake, water, and gun. 
So, the result will be 

1.Snake vs. Water: Snake drinks the water hence wins.
2.Water vs. Gun: The gun will drown in water, hence a point for water
3.Gun vs. Snake: Gun will kill the snake and win.
4.In situations where both players choose the same object, the result will be a draw.'''

# solution
import random
print('welcome on snake water gun game.')
no_of_chance = 0
chance = 10
human_points = 0
com_points = 0
l1 = ['s','w','g']
while no_of_chance<chance:
    _user = input('Enter your choice:\n1.s(snake)\n2.w(water)\n3.g(gun)\ntype here:')
    _random = random.choice(l1)
    if _user == _random:
        print('Tie both 0 point to each\n')

    # if s
    elif _user=='s' and _random=='w':
        human_points+=1
        print(f'your guess is {_user} and computer guess is {_random}.\n')
        print('you wins 1 point.\n')
        print(f'your points is {human_points} and computer points is {com_points}.\n')
    elif _user =='s' and _random=='g':
        com_points+=1
        print(f'your guess is {_user} and computer guess is {_random}.\n')
        print('computer wins 1 point.\n')
        print(f'your points is {human_points} and computer points is {com_points}.\n')
    # if w      
    elif _user=='w' and _random=='s':
        com_points+=1
        print(f'your guess is {_user} and computer guess is {_random}.\n')
        print('you computer 1 point.\n')
        print(f'your points is {human_points} and computer points is {com_points}.\n')
    elif _user=='w' and _random=='g':
        human_points+=1
        print(f'your guess is {_user} and computer guess is {_random}.\n')
        print('you wins 1 point.\n')
        print(f'your points is {human_points} and computer points is {com_points}.\n')
    # if g   
    elif _user=='g' and _random=='w':
        com_points+=1
        print(f'your guess is {_user} and computer guess is {_random}.\n')
        print('you computer 1 point.\n')
        print(f'your points is {human_points} and computer points is {com_points}.\n')
    elif _user=='g' and _random=='s':
        human_points+=1
        print(f'your guess is {_user} and computer guess is {_random}.\n')
        print('you wins 1 point.\n')
        print(f'your points is {human_points} and computer points is {com_points}.\n')
    else:
        print('enter valid values!')
    no_of_chance+=1
    print(f'{chance-no_of_chance} is left out of {chance}.\n')
print('Game over.')
if human_points==com_points:
    print(f'Tie\n')
elif human_points>com_points:
    print('you win.\n')
else:
    print('computer win.\n')
print(f'your total points is {human_points} and computer total points is {com_points}.\n')
        




