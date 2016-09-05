""" CP1404 Assignment 1
    Shopping List 1.0
    Sanio Vincent
    20/08/16

Pseudocode:
function main()
    get csv file
    get name
    display welcome_prompt
    display item_count
    display options
    get option_input
    while option_input is not q:
        if option_input is 'r'
            call read_contents()
        otherwise option_input is 'c'
            print completed_list
        otherwise option_input is 'a'
            call add_items()
        otherwise option_input is 'm'
            print required_list
    display item_count
    display goodbye message


function item_count()
    open items.csv as count_file for reading
    get the length of file from count_file
    return length_file

function read_contents()
    open items.csv as read_item for reading
    for each line in read_item
        add item to required items
        return required_list

function add_item()
    get item_name
    if item_name is empty
        print error message
    get item_price
    while item_price > 0
        get item_priority
        print added to shopping list
        add item_price, item_name, item_priority to required_list
        print required_list
    print error message



"""

required_items = []
OPTIONS = "\n Menu: \n R - List required items \n C - List Completed items \n A - Add new item \n M - Mark an item as completed \n Q - Quit"


def main():
    print("Welcome to Shopping List v1.0")
    name = input("Please enter your name")
    print("Welcome {}".format(name))
    print("{} items loaded from items.csv".format(count_lines("items.csv"), ))
    print(OPTIONS)
    input_option = input("-> ")
    while input_option != "q" and input_option != "Q":
        if input_option == "r" or input_option == "R":
            show_items = read_contents("items.csv")
            for item in required_items:
                print(item[0], ', '.join(map(str, item[1:])))
        elif input_option == "a" or input_option == "A":
            add_items()
        elif input_option == "m" or input_option == "M":
            for item in required_items:
                print(item[0], ', '.join(map(str, item[1:])))
        else:
            print("Please enter the correct value")
        print(OPTIONS)
        input_option = input("->")
    print("{} items loaded from items.csv".format(count_lines("items.csv"), ))
    print("Thank you for using Shopping List")


def count_lines(filename):
    count_file = open(filename, "r")
    read_lines = count_file.readlines()
    count_file.close()
    number_of_lines = len(read_lines)
    return number_of_lines


def read_contents(filename):
    read_item = open(filename, "r")
    for line in read_item:
        required_items.append(line.rstrip().split(","))




def add_items():
    input_item_name = input("Item name: ")
    item_name_length = len(input_item_name)
    if item_name_length == 0:
        print("Item name cannot be left blank")
    else:
        try:
            input_item_price = float(input("Price: $"))
            while input_item_price >= 0:
                item_priority = int(input("Priority: "))
                if item_priority > 0 and item_priority <= 3:
                    print("{}, ${:.2f} (priority {}) added to shopping list".format(input_item_name, input_item_price,
                                                                                    item_priority))
                    item_to_add = input_item_name, input_item_price, item_priority
                    required_items.append(item_to_add)
                    return required_items
                else:
                    print("Priority value must be 1,2 or 3")
            else:
                print("Price must be greater than $0")
        except ValueError:
            print("Please enter a valid number")


main()
