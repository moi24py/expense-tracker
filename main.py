import modules.app_funcs as a

def main():
    # welcome message
    a.intro()
    # ask the user what they want to do
    option = a.view_or_insert()
    
    if option:
        match option:
            case 'A':
                a.add_new_expense()
            case 'B':
                # Print all the expenses in expense_list.csv
                print("List of expenses:\n")
                a.print_expenses(a.search_expenses())
                exit()
            case 'C':
                a.print_category_expenses()
            case 'D':
                a.print_expenses_matched_by_name()
            case 'E':
                a.search_and_delete_expense()
            case 'F':
                a.view_balance()
            case 'G':
                # Add an amount to the balance
                a.add_sub_money()
                exit()
            case 'H':
                # Subtract an amount from the balance
                a.add_sub_money('sub')
                exit()
            case '0':
                print("Bye!\n")
                exit()

if __name__ == '__main__':
    main()
