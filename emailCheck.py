# checks email validity of student emails in Bellevue College where email format is:
# first_name.last_name@bellevuecollege.edu


def isEmailValid(email):
    countA = 0  # count '@'
    countPd = 0  # count '.'

    for c in email:  # tally characters
        if c == '@':
            countA += 1
        if c == '.':
            countPd += 1

    # conditional check
    if (email.endswith("@bellevuecollege.edu") and (email.find('.') < email.find('@'))
            and email.find('@') is not email.find('.')+1 and countA == 1 and countPd == 2):
        return True
    else:
        return False


def main():
    ans = "y"
    while ans == "y":
        email = input("Enter the email address: ")
        valid = isEmailValid(email)
        if valid:
            print("Valid email")
        else:
            print("Invalid email")
        ans = input("Want to continue(y/n)? ").lower()
        while ans != "y" and ans != "n":
            ans = input("Please enter a valid choice (y/n): ")


if __name__ == "__main__":
    main()

