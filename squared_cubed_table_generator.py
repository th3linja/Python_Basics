# write the main function
def main():
    # welcomes user to program
    print("Welcome to the square-cube table generator.")

    # asks user for starting and ending input with checks
    starting_number = input("Please enter your starting number: ")
    while digitCheck(starting_number) is False:
        starting_number = input("Please enter a valid integer: ")
    starting_number = int(starting_number)
    ending_number = input("Please enter your ending number: ")
    while digitCheck(ending_number) == False or int(ending_number) < starting_number:
        ending_number = input("Ending number has to be a valid integer greater than starting number: ")
    ending_number = int(ending_number)

    # print separator and identifiers
    print("=" * 7, "=" * 7, "=" * 7, sep="\t")
    print("Number", "Squared", "Cubed", sep="\t")
    print("=" * 7, "=" * 7, "=" * 7, sep="\t")

    # while starting number is less than ending, keep printing
    while starting_number <= ending_number:
        print(number(starting_number), squared(int(starting_number)), cubed(int(starting_number)), sep="\t")
        starting_number += 1


# define functions of number, squared, and cubed
def number(x):
    return x


def squared(x):
    return x * x


def cubed(x):
    return x * x * x


# define digit check
def digitCheck(x):
    try:
        int(x)
    except ValueError:
        return False


# invoke main
main()
