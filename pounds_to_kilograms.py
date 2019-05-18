# welcomes user to program
print("Welcome to Pounds to Kilogram Converter!")
print()

# prompts user for amount of pounds
pound_input = input("Enter the weight in Pounds:")
weight_outcome = int(pound_input) * 0.453592                   # converts pounds to kg
print("Weight in Kilograms is : " + str(weight_outcome))       # returns kg
print()

# end of program
print("Goodbye!")
