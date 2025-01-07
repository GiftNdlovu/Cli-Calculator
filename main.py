import re
from colorama import Fore, Style

print(Fore.RED + 'This is red text')
print(Style.RESET_ALL + 'Back to normal text')

#calculations
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

#user options and such
def main():
    print(Fore.CYAN + "choose type of operation")
    print(Style.RESET_ALL + "1. Addition")
    print("2. Subtract")
    choice = int(input(".... "))

    a = int(input("digit 1: "))
    b = int(input("digit 2: "))

    if choice == 1:
        results = add(a, b)
        print(Fore.GREEN + f"Results {results}")
        print(Style.RESET_ALL + "..")
    elif choice == 2:
        results = subtract(a, b)
        print(Fore.GREEN + f"Results {results}")
        print(Style.RESET_ALL + "..")
    else:
        print(Fore.RED + "invalid option")
        print(Style.RESET_ALL + "..")

#this is the exit mechanisim
restart = True
while restart:
    check = input("Do you want to exit? (y / N)")
    if check == "n":
        main()
    elif check == "Y" or "y":
        exit()
    else:
        print("invalid option, continuing")
        main()

