"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces.

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
from statistics import mean, median, mode, multimode


def start_game():
    welcome = print("Welcome to the Number Guessing Game!")
    random_number = random.randint(1, 100)
    attempts = []
    high_score = 0
    print(f"The current best score is {len(attempts)}.")

    while True:
        try:
            guess_number = int(input("Please guess a number between 1 and 100: "))
            if guess_number < 1 or guess_number > 100:
                raise ValueError("Your choice must be a whole number between 1 and 100.")
            elif guess_number > random_number:
                print("The correct number is lower.")
                attempts.append(guess_number)
                continue
            elif guess_number < random_number:
                print("The correct number is higher.")
                attempts.append(guess_number)
                continue
            elif guess_number == random_number:
                attempts.append(guess_number)
                attempts.sort()
                mean_number = mean(attempts)
                median_number = median(attempts)
                mode_number = mode(attempts)
                print(f"""You got it! It took you {len(attempts)} tries. The correct number was {random_number}.

                ** Overall Statistics **
                Mean: {mean_number}
                Median: {median_number}
                Mode: {mode_number}

                """)
                play_again = input("Would you like to play again? (Yes/No): ")
                if play_again.lower() == 'yes' or play_again.lower() == 'y':
                    if high_score == 0 or len(attempts) < high_score:
                        high_score = len(attempts)
                    print(f"The lowest # of attempts is {high_score}.")
                    attempts = []
                    random_number = random.randint(1, 100)
                    continue
        except ValueError as err:
            print("Oh No! That's not a valid value. Please try again.")
            print(f"({err})")
        else:
            print("Thank you for playing!")
            break


    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


# Kick off the program by calling the start_game function.
start_game()
