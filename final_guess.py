#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This function asks the user to guess a number between
# 1 and 10 with a loop and tells the user if the input is too low or high

import random


def main():
    # This function asks the user to guess a number between
    # 1 and 10 with a loop and tells the user if the input is too low or high

    # input, process & output
    random_number = random.randint(1, 10)

    while True:
        try:
            guessed_string = input("Enter a whole number between 1 and 10: ")
            print("")
            guessed_number = int(guessed_string)
            if guessed_number == random_number:
                print("YAAAAY you guessed it right!!!")
                break
            else:
                if guessed_number > random_number:
                    print("too high, please try again")
                else:
                    if guessed_number < random_number:
                        print("too low, please try again")
        except Exception:
            print("{0} is an invalid input.".format(guessed_string))

    print("Thanks for playing")
    print("\nDone.")


if __name__ == "__main__":
    main()
