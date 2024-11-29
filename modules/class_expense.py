""" Expense class """

class Expense():
    def __init__(self, date, name, category, cost):
        self.date = date
        self.name = name
        self.category = category
        self.cost = cost
    
    def print_exp(self):
        print(f"{self.name} in {self.category} €{self.cost}")