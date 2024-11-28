"""
This module contains the functions that are used by the program.
"""
from datetime import date
import calendar
import regex as re
from csv import DictReader, DictWriter, reader, writer

import modules.class_expense as ce

def intro():
    """Prints the welcome message."""
    print("\n\U0001F4B0 Expense Tracker \U0001F4B0\n")

def view_or_insert():
    """Asks the user if they want to see the expenses list or add a new expense."""
    options = ['A','B','C','D','E','F','G','H','0']

    print("""
Would you like to:
       °*°*°
[Expense]
A) add a new expense
B) view all the expenses
C) view the expenses in a category
D) search for an expense
E) delete an expense
       °*°*°
[Balance]
F) view balance
G) add money
H) subtract money
       °*°*°         
0) Exit the program""")

    answer = input("\nEnter the corresponding letter/number: ")

    if answer.upper() == 'A':
        # ask the user the name of the expense
        name = get_expense_name()
        # ask the user the cost of the expense
        cost = get_exp_cost()
        # show the categories
        print("The current categories are:")
        print_categories()
        # ask the user if they need a new category
        new_cat = input("If you need to add a new category, please enter \"y\": ")
        if new_cat.lower() == 'y':
            cat = new_category()
            if cat:
                write_new_cat(cat)
                print_categories()

        # ask the user the category of the expense
        category = choose_category()

        # create a new expense
        new_exp = ce.Expense(name, category, cost)

        # write the new expense in the csv file
        write_expense(new_exp)

        # print a confirmation
        confirm(name, cost, category)

        # subtract the expense from the balance
        add_sub_money('sub',cost)

        exit()

    if answer.upper() == 'B':
        print_expenses()
        exit()

    if answer.upper() == 'C':
        print_categories()
        choosen_cat = choose_category()
        print_expenses(None, choosen_cat)
        exit()

    if answer.upper() == 'D':
        exp_name = get_expense_name()
        checked_exp_name = check_name(exp_name)
        print_expenses(checked_exp_name, None)
        exit()

    if answer.upper() == 'E':
        pass
        exit()

    if answer.upper() == 'F':
        try:
            bal = get_balance()
            if bal:
                print(f"Current balance: {bal}€")
                money_left_per_day()
                exit()
        except:
            print("You have not set a balance yet.")
        exit()
    
    if answer.upper() == 'G':
        add_sub_money()
        exit()

    if answer.upper() == 'H':
        add_sub_money('sub')
        exit()

    if answer.upper() == '0':
        print("Bye!")
        exit()

    if answer not in options:
        print(f"Option {answer} does not exists. Please, run the program again and choose a valid option.")
        exit()

