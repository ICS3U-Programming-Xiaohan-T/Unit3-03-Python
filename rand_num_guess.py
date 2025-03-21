#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Mar 21, 2025
# This program is a random number generator between 0 and 9

import random

# a range between 0 and 9
random_variable = random.randint(0, 9)


def main():
    # ask to get user's input
    user_input = int(input("Guess a number between 0 to 9:"))
    # if else statement and compare with the correct variable
    if user_input != random_variable:
        # display it is not correct
        print("You are not correct, the correct number is: {}".format(random_variable))
    else:
        # display it is correct
        print("You guessed correct! nice job!")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
