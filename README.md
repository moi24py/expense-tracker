# expense-tracker

Just like the name says, this program helps you track expenses.

## Table of Contents
- [Why & How](#why--how)
- [Installation](#installation)
- [Usage](#usage)
- [Bugs](#bugs)
- [Lesson Learned](#lessons-learned)
- [Resources](#resources)

## Why & How
I came across a list of project ideas and decided to challenge myself by developing an expense tracker to practice reading and writing files.

## Installation
1. Clone the repository:
```bash
 git clone https://github.com/moi24py/expense-tracker.git
```

2. Install dependencies:
```bash
 pip install requirements.txt
 ```

## Usage

### Run
Use the Terminal to run the app:
```
expense-tracker % Python3 main.py
```

### How does it work
A menu will allow the user to choose an option.

<img width="247" alt="menu" src="https://github.com/user-attachments/assets/53055793-59d6-4a7f-91f6-1bc026bb8a3c">

If this is the first time using the app, select option ```G``` to add funds to the balance (see option G).

#### Add a new expense (option A)
The user is asked to enter the name of the expense and the expense cost, select the category or make a new one if needed.

<img width="518" alt="add_an_expense" src="https://github.com/user-attachments/assets/f4ff9e69-f1a3-4b1a-abd9-f30749792c78">

#### View all the expenses (option B)
The list of expenses added to the ```expense_list.csv``` file and the total amount are printed.

<img width="315" alt="print_expenses" src="https://github.com/user-attachments/assets/754ea40d-ba9f-45e1-918f-d03fbe79a441">

If there are no expenses, a message will be printed instead.

<img width="295" alt="no_expenses" src="https://github.com/user-attachments/assets/7fca12d3-2e0c-4cd8-b1d1-a24bcc396fb4">

#### View expenses in a category (option C)
The user is asked to select a category.
If there are expenses a list will be printed.
<img width="313" alt="exp_by_category" src="https://github.com/user-attachments/assets/41a257dc-cd00-4d7b-baa5-029b47c1ed33">

otherwise a message will let the user know.
<img width="296" alt="no_exp_by_category" src="https://github.com/user-attachments/assets/7a476106-4ea9-454c-9613-0fc6224eb856">

#### Search for an expense by name (option D)
To search for an expense by name, the user is asked to enter the expense's name, which can be full or partial.
If at least one expense is found, a list of those expenses will be displayed.
<img width="287" alt="search_by_partial_name" src="https://github.com/user-attachments/assets/bed00c4d-0c9d-4ba7-9c48-65f579bd28a8">

If no matches are found, a message will be displayed.
<img width="297" alt="no_result_by_name" src="https://github.com/user-attachments/assets/4a91cbf3-fe20-40fe-aca4-27ecf6b32765">

#### Delete an expense by name (option E)
The user will be prompted to enter the expense name. If at least one matching expense is found, a list of those expenses will be displayed.

The user must then enter the corresponding number of the expense they wish to delete.
<img width="304" alt="delete_expense" src="https://github.com/user-attachments/assets/e6706a62-798b-4d70-a118-dc7db943e238">

If no matches are found, a message will be displayed.
<img width="293" alt="no_exp_to_delete" src="https://github.com/user-attachments/assets/682cd36a-7322-4a87-8bfa-962be4377797">

#### View balance (option F)
If a balance has been set in the ```balance.csv``` file (with option G), this option displays the current balance.

Otherwise, a message will be displayed.
<img width="317" alt="view_balance_with_empty_balance_csv" src="https://github.com/user-attachments/assets/e9cda504-822e-403d-acea-7bd659680f95">

If the total amount of expenses does not exceed the balance, the average amount that can be spent in the remaining days of the month is also displayed.
<img width="605" alt="view_balance_money_left" src="https://github.com/user-attachments/assets/779de00d-a458-4124-b80a-0a716788f03e">

Otherwise, the user will see a message saying that there is no money left for the rest of the month.
<img width="668" alt="view_balance" src="https://github.com/user-attachments/assets/ffa6d55c-b0aa-491f-9836-c15a23307c06">

#### Add an amount (option G)
The user is prompted to enter a numeric amount to add to the balance. If the input is successful, the current balance will be displayed.
<img width="295" alt="add_to_balance" src="https://github.com/user-attachments/assets/94a874c1-d2a2-4056-80ef-a74fc9b7b6d5">
Otherwise, an error will occur and the program will stop.
<img width="719" alt="add_amount_invalid_input" src="https://github.com/user-attachments/assets/18974e38-eb69-41ac-a44d-e0974eccd061">

#### Subtract an amount (option H)
The user is prompted to enter a numeric amount to subtract from the balance. If the input is successful, the current balance will be displayed.
<img width="289" alt="sub_to_balance" src="https://github.com/user-attachments/assets/7a63cff1-7139-4d6d-afa5-0553e12f0887">
Otherwise, an error will occur and the program will stop.
<img width="719" alt="sub_amount_invalid_input" src="https://github.com/user-attachments/assets/e0c09dfc-0f62-49c7-93e2-18c26660790a">

#### Exit (option 0)
If this option is selected, the program will terminate.

### Bugs
If you found a bug, please contact me at moi24py@gmail.com
<img width="296" alt="exit" src="https://github.com/user-attachments/assets/3521d4e1-58cd-4e94-886a-6f4cb0f978ad">

### Lessons Learned
[Match statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement), reading and writing CSV files.

### Resources
* [Python CSV documentation](https://docs.python.org/3/library/csv.html)
* [Stack overflow - print tabular data](https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data)
