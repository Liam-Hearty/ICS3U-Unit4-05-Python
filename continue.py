#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program adds only positive numbers.


def main():
    # This program adds only positive numbers.

    answer = 0

    # input, process & output in loop
    try:
        adding_numbers = int(input("How many numbers are you going to add: "))
        for loop_counter in range(adding_numbers):
            chosen_number = int(input("Enter your number: "))
            # Process
            loop_counter = loop_counter + 1
            if chosen_number < 0:
                continue
            else:
                # Output
                answer = answer + chosen_number
                continue
        print("{0}".format(answer))
    except(ValueError):
        print("Please input a whole number.")


if __name__ == "__main__":
    main()
