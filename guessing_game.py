import random

print("Welcome to my guessing game!")

print("I am thinking of a number between 1 and 100," +
      " can you guess my secret number?")
print()

count = 0
random_int = random.randint(1, 100)
user_guess = input("Your guess? ")
while user_guess != random_int:
    if int(user_guess) > 100 or int(user_guess) < 0:
        print("Please guess a number between 1 and 100.")
        user_guess = input("Your guess? ")
    elif int(user_guess) < int(random_int):
        print("Too low!")
        user_guess = input("Your guess? ")
        count += 1
    elif int(user_guess) > int(random_int):
        print("Too high!")
        user_guess = input("Your guess? ")
        count += 1
    if int(user_guess) == int(random_int):
        count += 1
        break

print("Congratulations!! You guess my number in " + str(count) + " tries!")
