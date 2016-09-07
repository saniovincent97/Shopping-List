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
import csv

OPTIONS = "\n Menu:\n R - List required items \n C - List Completed items \n A - Add new item" \
          " \n M - Mark an item as completed \n Q - Quit"


def main():
    items = load_contents()
    print("Shopping List v1.0 - by Sanio Vincent")
    print("{} items loaded from items.csv".format(len(items)))
    print(OPTIONS)
    input_option = input("-> ")
    while input_option != "q" and input_option != "Q":
        if input_option == "r" or input_option == "R":
            required_items(items)
        elif input_option == "c" or input_option == "C":
            completed_items(items)
        elif input_option == "a" or input_option == "A":
            add_items(items)
        elif input_option == "m" or input_option == "M":
            required_items(items)
            input_number = int(input("Enter the number of an item to mark as completed"))
            mark_as_completed(items, input_number)

        else:
            print("Please enter the correct value")
        print(OPTIONS)
        input_option = input("->")
    print("{} items loaded from items.csv".format(len(items)))
    print("Thank you for using Shopping List")

def mark_as_completed(items, input_number):
    for number, item in enumerate(items):
        if input_number == number:
            item[3] = "c"
            print("{} marked as complete".format(item[0]))


def load_contents():
    items = []
    read_items = open("items.csv", "r")
    item_file = csv.reader(read_items)
    for item in item_file:
        items.append([item[0], float(item[1]), int(item[2]), item[3]])
    read_items.close()
    return items


def required_items(items):
    total = 0
    print("Required items:")
    for number, item in enumerate(items):
        if item[3] == "r":
            print("{}. {:20} ${:.2f} ({})".format(number, item[0], float(item[1]), int(item[2],)))
            total += item[1]
    print("Total expected price for {} items: ${}".format(len(items), total))


def completed_items(items):
    total = 0
    for number, item in enumerate(items):
        if item[3] == "c":
            print("{}. {:20} ${:.2f} ({})".format(number, item[0], float(item[1]), int(item[2],)))
            total += item[1]
    print("Total expected price for {} items: ${}".format(len(items), total))



def add_items(items):
    item_name = input("Item name: ")
    item_name_length = len(item_name)
    if item_name_length == 0:
        print("Item name cannot be left blank")
    else:
        try:
            item_price = float(input("Price: $"))
            while item_price >= 0:
                item_priority = int(input("Priority: "))
                if item_priority > 0 and item_priority <= 3:
                    print("{} ${:.2f} (priority {}) added to shopping list".format(item_name, item_price,
                                                                                    item_priority))
                    required = "r"
                    items.append([item_name, item_price, item_priority, required])
                    return items
                else:
                    print("Priority value must be 1,2 or 3")
            else:
                print("Price must be greater than $0")
        except ValueError:
            print("Please enter a valid number")


main()
