#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 25, 2025
# Program that checks the sign of an integer provided by the user


def main():
    # Get integer from user, user_int
    user_int = int(input("Enter an integer: "))

    # If it's greater than 0, it's positive
    if user_int > 0:
        # Tell the user that the integer is positive
        print(f"{user_int} is Positive!")
    # If it's equal to 0, the integer is 0
    elif user_int == 0:
        # Zero is neither positive nor negative
        # Tell the user that the integer is Zero
        print(f"{user_int} is Zero!")
    # If it's not positive and not zero, it must be negative
    else:
        # Tell the user that the integer is negative
        print(f"{user_int} is Negative!")


if __name__ == "__main__":
    main()
