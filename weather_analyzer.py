# greets user to program
print("Welcome to the Weather Analyzer")

# gets degree (type) input from user (also checks whether input is valid)
degree_letter = input("Please enter the units for temperature (Enter 'F' for Fahrenheit / 'C' for Celcius): ")
degree_letter = degree_letter.lower()
while degree_letter not in ("f", "c"):
    degree_letter = input("Please enter a valid unit: ")
    degree_letter = degree_letter.lower()

# gets the temperature from the user
degree = input("Please enter the temperature: ")
while degree.isdigit() is False:
    degree = float(input("Please enter a valid temperature: "))
print()

# calculates and forcasts the weather
if degree_letter == 'c':
    degree = float(degree) * (9 / 5) + 32
    print("The temperature is: " + str(degree) + "F")
elif degree_letter == 'f':
    print("The temperature is: " + str(degree) + "F")

if float(degree) > 80:
    print("It is too hot outside.")
else:
    if float(degree) > 60:
        print("It is very pleasant outside.")
    else:
        if float(degree) < 60:
            print("It is chilly outside.")
