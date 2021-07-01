'''
You have to build a "Number Guessing Game," in which a winning number is set to some integer value. 
The Program should take input from the user, and if the entered number is less than the winning number, 
a message should display that the number is smaller and vice versa.

Instructions:
1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
You are advised to participate in solving this problem. This task helps you to become a good problem solver and helps you accepting the challenge and acquiring new skills.'''

# solution
no_of_guesses = 0
num = 45
while (True):
    no_of_guesses +=1
    if no_of_guesses<=9:
        user_inp = int(input("Enter your choice here:"))
        if user_inp<num:
            print("you have try to enter a greater number." )
        elif user_inp>num:
            print("you have try to enter a lesser number." )
        else:
            print('congrates!, you enter successfully correct number.\nGame over!')
            print(no_of_guesses,'no. of guesses, you use to finish the game..')
            quit()
        print("total chance of gussess is 9.")
        print('and you have',9-no_of_guesses,'no. of guesses left.')


    elif no_of_guesses==10:
        print('your guess limit finished.')
        print('Game over!')
        exit()
            


