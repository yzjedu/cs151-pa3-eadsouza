# Programmer: Ethan D'Souza
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/7/2024
# Programming Assignment: 03
# Problem Statement: Create a program to display ASCII art and string decorations to the user.
# Purpose: Let the user pick a design, and output that said design.


import random


def main():
    print("Welcome to the ASCII Art and String Decoration Program!")
    print("Choose an option:")

    choice = 0
    while choice != 4:
        print("\n1. Draw Circle")
        print("2. Draw Lines")
        print("3. Random Design")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid input! Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            draw_circle()
        elif choice == 2:
            draw_lines()
        elif choice == 3:
            random_design()
        elif choice == 4:
            print("Thank you for using the program. Goodbye!")
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")


def draw_circle():
    print("\nCircle Design:")
    print(f"   ****")
    print(f" *      *")
    print(f"*        *")
    print(f" *      *")
    print(f"   ****")


def draw_lines():
    print("\nLine Design:")

    num_lines = input("Enter the number of lines to draw: ")
    if num_lines.isdigit():
        num_lines = int(num_lines)
    else:
        print("Invalid input! Please enter a whole number.")
        return

    character = input("Enter the character(s) to repeat for the line: ")

    repeat_count = input("Enter how many times to repeat the character(s): ")
    if repeat_count.isdigit():
        repeat_count = int(repeat_count)
    else:
        print("Invalid input! Please enter a whole number.")
        return

    print("\nYour Pattern:")
    for i in range(num_lines):
        print(f"{character * repeat_count}")


def random_design():
    design_choice = random.choice([design1, design2, design3])
    design_choice()


def design1():
    print("\nRandom Design 1: Christmas Tree")
    print(f"    ^")
    print(f"   / \\")
    print(f"  /   \\")
    print(f" /     \\")
    print(f"/_______\\")
    print(f"    | |")

#inspired, and shown in Stack Overflow: https://stackoverflow.com/questions/39548099/printing-simple-diamond-pattern-in-python
def design2():
    print("\nRandom Design 2: Diamond Shape")
    print(f"    *")
    print(f"   ***")
    print(f"  *****")
    print(f"   ***")
    print(f"    *")


def design3():
    print("\nRandom Design 3: Spiral")
    print(f"o----o")
    print(f"|    |")
    print(f"o----o")


# Run the main function
main()



