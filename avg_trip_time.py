# welcomes user to the program
print("Welcome to the Trip Time Calculator")
print()

# ask user for miles to be traveled and average mph
travel = input("Enter the amount of miles to be traveled: ")
while travel.isdigit() is False or int(travel) < 0:  # check for valid input
    travel = input("Please enter a valid input: ")
mph = input("Enter the average mph of the trip: ")
while mph.isdigit() is False or int(mph) <= 0:  # check for valid input (cannot divide by 0)
    mph = input("Please enter a valid input:")
print()

# calculate based on given information
hours = int(travel)//int(mph)
minutes = int(travel) - hours*int(mph)

# return calculations
print("Estimated travel time")
print("Hours: " + str(hours))
print("Minutes: " + str(minutes))

