# create main function
def main():
    greet()
    command_menu()
    command()


# greet the user of the program
def greet():
    print("The Wizard Inventory Program")
    print()


# print out the command menu
def command_menu():
    print("COMMAND MENU")
    print("show - Show all items" +
          "\ngrab - Grab an item" +
          "\nedit - Edit an item" +
          "\ndrop - Drop an item" +
          "\nexit = Exit Program")
    print()


# take the input of the user and validate the command
def command():
    cmd = input("Command: ")
    while(cmd.lower() != 'exit'):
        while(cmd.lower() != 'show' and cmd.lower() != 'grab' and cmd.lower() != 'edit'
              and cmd.lower() != 'drop' and cmd.lower() != 'exit'):
            print("Invalid command. Please try again.\n")
            cmd = input("Command: ")
        if(cmd.lower() == 'show'):
            show()
            cmd = input("Command: ")
        elif(cmd.lower() == 'grab'):
            grab()
            cmd = input("Command: ")
        elif(cmd.lower() == 'edit'):
            edit()
            cmd = input("Command: ")
        elif(cmd.lower() == 'drop'):
            drop()
            cmd = input("Command: ")
    print("Bye!")


# show function that will display the list when called upon
def show():
    for i in range(len(item_list)):
        print(str(i+1) +'. ' + color_list[i] + " " + name_list[i] + weight_list[i])     # print color, name, weight
    print()


# grab function that will limit the list and append the list with an item
def grab():
    global item_number                                                      # import global item_number (nonstatic)
    if len(item_list) == COUNT_LIMIT:                                       # check if inventory is full
        print("You can't carry any more items. Drop something first.")
        print()
    else:
        name_item = input("Name: ")                                         # Ask user for name input
        color_item = input("Color: ")                                       # Ask user for color input
        weight_item = input("Weight in lbs: ")                              # Ask user for weight input
        if numCheck(weight_item) == False or int(weight_item) < 0:          # check if item weight is a number and is not negative
            print("Invalid item weight.")
            print()
            return
        name_list.append(name_item.lower())                                 # add name_item to name_list
        color_list.append(color_item.capitalize())                          # add color_item to color_list
        weight_list.append("(" + weight_item + " lbs)")                     # add weight_item to weight_list
        item_list.append(color_item.capitalize() + " " +
                         name_item.lower() + " (" + weight_item + " lbs)")  # add item to item_list
        item_number += 1                                                    # item_number + 1
        print(item_list[item_number] + " was added.")
        print()


# edit function to change the value or name of an element in the list
def edit():
    global item_number                                                      # import global item_number (nonstatic variable)
    number_item = input("Number: ")                                         # ask user for number input
    if(numCheck(number_item) == False or int(number_item) > len(item_list)  # check input if it is a valid input
          or int(number_item) < 0):
        print("Invalid item number.")
        print()
        return
    update_name = input("Updated name: ")                                   # ask user for updated name
    name_list[int(number_item) - 1] = update_name                           # change the name in list at item_number to updated name
    print("Item number " + str(number_item) + " was updated.")
    print()


# drop function to remove an item from the list
def drop():
    global item_number                                                      # import item_number (nonstatic variable)
    user_drop = input("Drop by number or by color? ")                       # ask user whether they want to drop by number or by color
    if user_drop.lower() != "number" and user_drop.lower() != "color":     # if input is invalid - invalid choice
        print("Invalid choice. Should be either number or color.")
        print()
        return
    elif(user_drop.lower() == 'number'):                                        # if it is number
        number_item = input("Number: ")                                         # ask user for number input
        if(numCheck(number_item) == False or int(number_item) > len(item_list)  # validate input
              or int(number_item) < 0):
            print("Invalid item number.")
            print()
            return
        memory_store_item = item_list.pop(int(number_item) - 1)         # store removed item
        name_list.pop(int(number_item) - 1)                             # remove name of item from list
        color_list.pop(int(number_item) - 1)                            # remove color of item from list
        weight_list.pop(int(number_item) - 1)                           # remove weight of item from list
        print(memory_store_item + " was dropped.")                      # print dropped item number
        item_number -= 1                                                # item_number - 1
        print()
    elif(user_drop.lower() == 'color'):                             # if input is color
        color_item = input("Color: ")                               # ask user for color input
        for i in range(len(item_list)):                             # loop through item list
            if(item_list[i].startswith(color_item.capitalize())):   # if item starts with color
                memory_store_item = item_list.pop(i)                # store removed item
                name_list.pop(i)                                    # remove name from list
                color_list.pop(i)                                   # remove color from list
                weight_list.pop(i)                                  # remove weight from list
                print(memory_store_item + " was dropped.")          # print dropped item number
                item_number -= 1                                    # item number -1
                print()
                return
        print("No items of color found. No items were dropped.")
        print()


# checks if the user input is an integer
def numCheck(x):
    try:
        x = int(x)
    except:
        return False


# run main
if __name__ == '__main__':
    COUNT_LIMIT = 4         # global variable of inventory space
    item_number = 3-1       # number of items in list - 1
    name_list = ['wooden staff', 'wizard hat', 'cloth shoes']   # list of names in the order of items
    color_list = ['Brown', 'Black', 'Blue']                     # list of color in the order of items
    weight_list = ['(30.0 lbs)', '(1.5 lbs)', '(5.3) lbs' ]     # list of weight in the order of items
    item_list = ['Brown wooden staff (30.0 lbs)', 'Black wizard hat (1.5 lbs)', 'Blue cloth shoes (5.3 lbs)']
    main()
