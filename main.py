import modules.app_funcs as a

def main():
    # welcome message
    a.intro()
    # ask the user what they want to do
    option = a.view_or_insert()
    
    if option:
        if option == 'A':
            a.add_new_expense()
        if option == 'B':
            # Print all the expenses in expense_list.csv
            print("List of expenses:\n")
            a.print_expenses(a.search_expenses())
            exit()
        if option == 'C':
            a.print_category_expenses()
        if option == 'D':
            a.print_expenses_matched_by_name()
        if option == 'E':
            a.search_and_delete_expense()
        if option == 'F':
            a.view_balance()
        if option == 'G':
            # Add an amount to the balance
            a.add_sub_money()
            exit()
        if option == 'H':
            # Subtract an amount from the balance
            a.add_sub_money('sub')
            exit()
        if option == '0':
            print("Bye!\n")
            exit()

if __name__ == '__main__':
    main()
