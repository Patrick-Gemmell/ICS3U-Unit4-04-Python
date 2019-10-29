#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: october 2019
# This program does a guessing game


import random


def main():
    # this function guess and compares number
    while True:
        guessed_number_string = input("Guess an integer from 0-9 ")
        try:
            # input
            guessed_number_int = int(guessed_number_string)
            # process and output
            print("")
            if guessed_number_int == random.randint(0, 9+1):
                print("Correct!")
                break
            else:
                print("Sorry that's wrong, guess again?")
        except Exception:
            print("Sorry that is not an integer")


if __name__ == "__main__":
    main()
