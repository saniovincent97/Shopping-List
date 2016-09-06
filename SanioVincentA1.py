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

OPTIONS = "\n Menu: \n R - List required items \n C - List Completed items \n A - Add new item" \
          " \n M - Mark an item as completed \n Q - Quit"


def main():
    print("Welcome to Shopping List v1.0")
    name = input("Please enter your name")
    print("Welcome {}".format(name))
    print("{} items loaded from items.csv".format(count_lines("items.csv"), ))
    print(OPTIONS)
    input_option = input("-> ")
    while input_option != "q" and input_option != "Q":
        if input_option == "r" or input_option == "R":
            show_content = read_contents()
        elif input_option == "a" or input_option == "A":
            add_items()
        elif input_option == "m" or input_option == "M":
            show_content = read_contents()

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


def read_contents():
    number = 0
    read_items = open("items.csv")
    item_file = csv.reader(read_items)
    items = list(item_file)
    for row in items:
        print("{}. {:20} $ {:5} ({})".format(number, row[0], row[1], row[2]))
        number += 1
    print("Total expected price for {} item is:".format(number))


def add_items():
    open_file = open("items.csv", "a+")
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
                    print("{}, ${:.2f} (priority {}) added to shopping list".format(item_name, item_price,
                                                                                    item_priority))
                    print(item_name, ",", item_price, ",", item_priority, file=open_file)
                    open_file.close()
                else:
                    print("Priority value must be 1,2 or 3")
            else:
                print("Price must be greater than $0")
        except ValueError:
            print("Please enter a valid number")


main()
