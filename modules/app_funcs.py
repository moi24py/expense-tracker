"""
This module contains the functions that are used by the program.
"""
from datetime import date
import calendar
import regex as re
from csv import DictReader, DictWriter, reader, writer
from tabulate import tabulate

import modules.class_expense as ce

def intro():
    """Prints the welcome message."""
    print("\n\U0001F4B0 expense-tracker \U0001F4B0")

def view_or_insert():
    """Asks the user if they want to see the expenses list or add a new expense."""
    options = ['A','B','C','D','E','F','G','H','0']

    print("""
Would you like to:
       
[Expense]
A) add a new expense
B) view all the expenses
C) view expenses in a category
D) search for an expense by name
E) delete an expense by name
       
[Balance]
F) view balance
G) add an amount
H) subtract an amount
       - - -         
0) exit the program""")

    answer = input("\nEnter the corresponding letter/number: ")
    if answer.upper() in options:
        return answer.upper()

    print(f"Option {answer} does not exists. Please, run the program again and choose a valid option.")
    exit()


def add_new_expense():
    """Adds a new expense to expense_list.csv."""

    name = get_expense_name()       
    cost = get_exp_cost()
    
    print("The current categories are:")
    print_categories()
  
    new_cat = input("If you need to add a new category, please enter \"y\": ")
    if new_cat.lower() == 'y':
        cat = new_category()
        if cat:
            write_new_cat(cat)
            print_categories()

    category = choose_category()
    today = str(date.today())

    # Initialize a new expense
    new_exp = ce.Expense(today, name, category, cost)

    write_expense(new_exp)
    print_confirm(name, cost, category)

    # subtract the expense from the balance
    add_sub_money('sub',cost)

    exit()


def print_category_expenses():
    """Print the expenses of a category."""
    print_categories()
    choosen_cat = choose_category()
    exp_list = search_expenses(None,choosen_cat)
    print('\n')
    print_expenses(exp_list)
    exit()

def print_expenses_matched_by_name():
    """Print the expenses with a specific name."""
    exp_name = get_expense_name()
    checked_exp_name = check_name(exp_name)
    matched_exps = search_expenses(checked_exp_name, None)
    print_expenses(matched_exps)
    exit()

def search_and_delete_expense():
    """Delete an expense from expense_list.csv."""
    name = get_expense_name()
    checked_name = check_name(name)
    matched_exp = search_expenses(checked_name,None)
    exp_to_delete = select_to_delete(matched_exp)
    delete_expense(exp_to_delete)
    exit()

def view_balance():
    try:
        bal = get_balance()
        if type(bal) == float:
            print(f"Current balance: {bal}€")
            money_left_per_day()
            return None
    # if there is none
    except:
        print("You have not set a balance yet.")
        # ask the user if they want to enter an amount
        answer_set_amount = input("If you'd like to set an amount enter \"y\": ")
        if answer_set_amount.lower() == "y":
            # add the amount to the balance
            add_sub_money()
        else:
            print("No amount has been entered.")
    exit()

name_regex = re.compile(r'^[a-zA-Z\ ]{1,30}$', re.I)

def check_name(name:str) -> str:
    """Checks if the name entered by the user matches the regex (only letters and spaces).
    
    Parameters
    ----------
    name
        A string representing the name of the expense.

    Returns
    -------
    str
        A string representing the name of the expense after the regex check.
    """
    try:
        exp_name = name_regex.fullmatch(name)
        if exp_name:
            return exp_name.group()
    except:
        return None


def new_category() -> str:
    """Adds a new category to the list.
    
    Returns
    -------
    str
        A string representing the name of the new category.
    """
    i = 0
    while i <= 3:
        new_cat = input("\nEnter the new category name: ")
        try:
            checked_cat = check_name(new_cat)
            if checked_cat:
                return checked_cat.capitalize()
        except:
            i += 1
    return None

def write_new_cat(category:str):
    """Opens categories.csv file and adds the category just entered by the user.
    
    Parameters
    ----------
    category
        A string representing the name of the new category.
    """
    with open('modules/categories.csv', 'a', newline='') as csvfile:
        fieldnames = ['name']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'name': category})

def get_categories() -> list[dict]:
    """Opens categories.csv file and reads its content.

    Returns
    -------
    list[dict]
        A list of dictionaries representing the name of each category.
    """
    with open('modules/categories.csv','r') as csvfile:
        categories = list(DictReader(csvfile))
        return categories


def print_categories():
    """Prints the categories stored in categories.csv."""
    categories = get_categories()
    categories_qty = len(categories)
    for i in range(categories_qty):
        print(f"{i+1}) {categories[i]['name']}")

def choose_category() -> str:
    """Asks the user to select a category.
    
    Returns
    -------
    str
        A string representing the selected category.
    """
    categories = get_categories()
    categories_qty = len(categories)
    i = 0
    while i <= 3:
        cat_num = input("Enter the category number: ")
        try:
            cat = categories[int(cat_num)-1]
            if cat and cat in categories:
                return cat['name']
        except:
            i += 1
            print(f"Please, only enter numbers from 1 to {categories_qty}.")
    raise TypeError(f"You have not choosen a category from 1 to {categories_qty}")
        

def get_expense_name() -> str:
    """Asks the user for the expense name.
    
    Returns
    -------
    str
        A string representing the name of the expense.
    """
    i = 0
    while i <= 3:
        name = input("\nEnter expense name: ")
        checked_name = check_name(name)
        if checked_name:
            return checked_name.lower()
        else:
            i += 1
            print("Only enter letters and spaces.")
    raise TypeError("You have entered one or more invalid characters. Maximum attempts reached.")


cost_regex = re.compile(r'[\d]{1,10}\.?[\d]{0,2}$', re.I)
def get_exp_cost() -> float:
    """Asks the user for the expense amount.
    
    Returns
    -------
    float
        A float representing the amount of the expense.
    """
    i = 0
    while i <= 3:
        cost = input("\nEnter the expense cost: ")
        try:
            exp_cost = cost_regex.fullmatch(cost)
            if exp_cost:
                rounded_cost = round(float(exp_cost.group()),2)
                return rounded_cost
            else:
                raise TypeError("Invalid input, only digits are allowed.")
        except:
            print("Try again. Please only insert decimals up to two digits.")
            i += 1
    raise TypeError("Maximum attemps reached.")


def write_expense(expense):
    """Opens expense_list.csv and writes the list of expenses.
    
    Parameters
    ----------
    expense
        An instance of Expense class representing the expense data.
    """
    with open('expense_list.csv', 'a', newline='') as csvfile:
        fieldnames = ['date', 'name', 'cost', 'category']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'date': expense.date, 'name': expense.name, 'cost': expense.cost, 'category' : expense.category})


def print_confirm(exp_name:str, exp_cost:float, category:str):
    print(f"\nYou've successfully added \"{exp_name}\" ({exp_cost}€) in {category} to your expenses.")


def search_expenses(name:str=None, category:str=None) -> list[dict]:
    """Searches for the expenses in the expense_list.csv file.
    
    Parameters
    ----------
    name
        optional: a string representing the name of the expense.
    category 
        optional: a string representing the category of the expense.

    Returns
    -------
    list[dict]
        A list of dictionaries with the matching expenses.
    """
    with open('expense_list.csv', newline='') as csvfile:
        reader = list(DictReader(csvfile))
        # If there are no expenses
        if len(reader) < 1:
            return None
        # If there are expenses
        exp_list = []
        # all the expenses
        if name == None and category == None:
            for row in reader:
                exp_list.append(row)
            return exp_list
        # all the expenses by category
        if category:
            for row in reader:
                if category.capitalize() == row['category']:
                    exp_list.append(row)
            if len(exp_list) < 1:
                return None
            return exp_list
        # all the expenses by name
        if name:
            for row in reader:
                if name.lower() in row['name']:
                    exp_list.append(row)
            if len(exp_list) < 1:
                return None
            return exp_list
        

def print_expenses(exp_list:list[dict]=None):
    """Prints the expenses if a list of expenses is passed in.
    
    Parameters
    ----------
    list[dict]
        optional: a list of dictionaries representing each expense.
    """
    # No expenses
    if exp_list == None:
        print("There are no expenses.")
        return None
    # Print the expenses and their total
    if exp_list:
        table = []
        tot = 0
        for exp in exp_list:
            tot += float(exp['cost'])
            table.append([exp['date'],exp['name'],exp['cost'],exp['category']])
        print(tabulate(table, headers=['Date','Name','Cost','Category'], floatfmt=".2f"))
        print(f"\nThe total is {round(tot,2)}€.\n")
        return None

def select_to_delete(exp_list:list[dict]=None) -> dict:
    """Asks the user to select the expense to delete and deletes it.
    
    Parameters
    ----------
    exp_list
        A list of dictionaries that represents the matched expenses.
        
    Returns
    -------
    dict
        A dict that represents the expense to be deleted."""
    if exp_list == None:
        print("No list provided.")
        return None
    
    for i in range(len(exp_list)):
        print(f"{i+1}#  {exp_list[i]['name']} {exp_list[i]['cost']}€ in {exp_list[i]['category']}")
    i = 0
    while i <= 3:
        exp_num = input("Enter the expense number: ")
        try:
            exp_dict = exp_list[int(exp_num)-1]
            if exp_dict and exp_dict in exp_list:
                return exp_dict
        except:
            i += 1
            print(f"Please, only enter numbers from 1 to {len(exp_list)}.")
    raise TypeError(f"Invalid input. No expense have been choosen.")

def delete_expense(expense_to_delete:dict=None):
    """Deletes an expense from the expense_list.csv file.
    
    Parameters
    ----------
    list[dict]
        A list of dictionaries representing each expense.
    """
    if expense_to_delete == None:
        print("There is no expense to delete.")
        return None
    
    # If there is an expense list

    # Create a list of the expenses but not the one to delete
    new_expense_list = []
    with open('expense_list.csv', 'r') as csvfile:
        readcsv = list(DictReader(csvfile))
        # make a list with all the non-matching expenses
        for exp_dict in readcsv:
            if exp_dict != expense_to_delete:
                new_expense_list.append(exp_dict)
    # write the new list in expense_list.csv
    with open('expense_list.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'name', 'cost', 'category']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for exp in new_expense_list:
            writer.writerow({'date': exp['date'], 'name': exp['name'], 'cost': exp['cost'], 'category' : exp['category']})
        print("Expense successfully deleted.")
    
    # Add the expense cost to the balance
    expense_cost_to_add_to_balance = float(expense_to_delete['cost'])
    add_sub_money(None,expense_cost_to_add_to_balance)

def expenses_tot() -> float:
    """Sums the expenses of the current month.
    
    Returns
    -------
    float
        A float representing the sum of this month expenses.
    """
    
    # Get today's year and month
    today = str(date.today())
    this_year_month = today[:7]
    # Sums the expenses of the current month
    with open('expense_list.csv', 'r', newline='') as csvfile:
        tot = 0
        read_exps = DictReader(csvfile)
        for row in read_exps:
            if row['date'][:7] == this_year_month:
                tot += float(row['cost'])
        if tot == 0:
            print(f"No expenses in {this_year_month}.")
            return None
        return round(tot,2)

def days() -> int:
    """Gets today's date, gets the number of days in the current month and returns how many days are left.
    
    Returns
    -------
    int
        A number representing the amount of days remains in the current month.
    """
    today = str(date.today())
    year = int(today[:4])
    month = int(today[5:7])
    today_day = int(today[8:])
    _, month_days = calendar.monthrange(year, month)
    days_left = month_days - today_day
    return days_left

def get_balance() -> float:
    """Gets the current balance from "balance.csv" file.

    Returns
    -------
    float
        A float representing the current balance
    """
    with open('modules/balance.csv','r') as csvfile:
        read_balance = tuple(reader(csvfile))
        if len(read_balance) < 1:
            print("You have not set a balanace yet.")
            return None
        else:
            return round(float(read_balance[0][0]),2)
        
def print_balance():
    """Prints the balance."""
    amount = get_balance()
    if amount:
        print(f"Current balance is {amount}€.")

def add_sub_money(sub:str=None, exp_cost:float=None):
    """Adds an amount entered by the user to the balance.
    
    Parameters
    ----------
    sub
        optional: A string that represents the subtraction operation.
    exp_cost
        optional: A float that represents the cost of the expense. 
    """
    rounded_amount = 0.0
    if not exp_cost:
        i = 0
        while i <= 3:
            amount = input("\nEnter the amount: ")
            try:
                checked_amount = cost_regex.fullmatch(amount)
                if checked_amount:
                    rounded_amount = round(float(checked_amount.group()),2)
                    break
                else:
                    raise TypeError
            except:
                print("Try again. Please only insert decimals up to two digits.")
                i += 1
            if i == 4:
                raise TypeError("Invalid input, only digits are allowed.")
    total = 0
    try:
        current_balance = get_balance()
        if type(current_balance) == float:
            if sub and exp_cost:
                total = round(current_balance - exp_cost,2)
            elif exp_cost:
                total = round(current_balance + exp_cost,2)
            elif sub:
                total = current_balance - rounded_amount
            else:
                total = current_balance + rounded_amount
    except:
        if sub and exp_cost:
            total -= round(exp_cost,2)
        elif sub:
            total -= rounded_amount
        else:
            total += rounded_amount
    with open('modules/balance.csv','w') as csvfile:
        balance_writer = writer(csvfile)
        balance_writer.writerow((total,))
    print_balance()


def money_left_per_day():
    """Prints the mean amount that can be spent per day."""
    curr_balance = 0
    remaining_days = 0
    expenses_t = 0

    try:
        curr_balance = get_balance()
    except:
        print("Cannot access to the current balance.")
        return None
    
    try:
        remaining_days = days()
    except:
        print("Cannot access the quantity of days left in this month.")
        return None
    
    try:
       expenses_t = expenses_tot()
    except:
        print("Cannot access the total amount of expenses of this month.")
        return None
    
    if expenses_t >= curr_balance:
        message = f"\U0001F4B8 You have spent {expenses_t}€ so far this month. You have no money left for the rest of the month."
    else:
        remaining_amount = round(curr_balance/remaining_days,2)
        message = f"\U0001F4B8 You have spent {expenses_t}€ so far this month. You have roughly {remaining_amount}€ left this month."
    print(message)

if __name__ == "__main__":
    intro
    choose_category
    get_exp_cost
    get_expense_name
    write_expense
    print_confirm
    days
    money_left_per_day

