import re
from colorama import Fore, Style

print(Fore.RED + 'This is red text')
print(Style.RESET_ALL + 'Back to normal text')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

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
    elif choice == 2:
        results = subtract(a, b)
        print(Fore.GREEN + f"Results {results}")
    else:
        print(Fore.RED + "invalid option")

restart = True
while restart:
    main()

check = input("Do you want to exit? (y / N)")
if check == "N" or "n":
    pass
elif check == "Y" or "y":
    exit()

