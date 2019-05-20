def greet():
    print("Welcome to the Prime Number Checker")


def getFactors():
    cont = 'y'
    while cont == 'y':
        print()
        integer_input = (input("Please enter an integer between 1 and 5000: "))
        while integer_input.isdigit() == False or int(integer_input) > 5000 or int(integer_input) < 1:
            integer_input = input("Invald integer. Please enter an integer between 1 and 5000: ")
        integer_input = int(integer_input)

        factors = []
        for i in range(integer_input):              # find factors of inputted number
            if integer_input % (i + 1) == 0:
                factors.append(i + 1)
        print("Factors: " + str(factors))
        print("It has " + str(len(factors)) + " factors.")

        if len(factors) == 2:                                               # if only two factors are found - prime
            print(str(integer_input) + " is a prime number. \n")
        else:                                                               # otherwise - not prime
            print(str(integer_input) + " is NOT a prime number. \n")

        cont = input("Try again? (y/n): ")                                  # repeat
        while cont.lower() != 'y' and cont.lower() != 'n':
            cont = input("Invalid input. Try again? (y/n): ")
    print("Bye!")


def main():
    greet()
    getFactors()


main()

