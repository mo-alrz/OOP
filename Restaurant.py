# Write a program that is capable of handling simple restaurants! These restaurants have only one product: menu.
# Different restaurants can have different prices for their menus. We’d like to create a new restaurant in the
# program by giving the name of the restaurant and the price of the menu there. The restaurants give a discount to
# their employees, they get a menu for half price, while a guest needs to pay the full price. The restaurants can sit
# customers at tables (without limitations) and can serve menus to all the current customers. Whenever a menu is
# served, the customer pays, which is added to the income of the restaurant, and the customer also stands up from the
# table. Using your solution, the following code should run without errors and print the expected results.


class Employee:
    def __init__(self, name):
        self.name = name


class Guest:
    def __init__(self, name):
        self.name = name


class Restaurant:
    customers = []
    income = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} | {len(self.customers)} customers | Menu for {self.price}$ | Income : {self.income}'

    def sit(self, *clients):
        for c in clients:
            self.customers.append(c)

    def serve_menu(self):
        global emp_name, guest_name
        for c in self.customers:
            if type(c) == Employee:
                emp_name = c
                self.income += self.price / 2
            if type(c) == Guest:
                guest_name = c
                self.income += self.price

        print(f"{emp_name.name} is eating for {self.price / 2} and "
              f"{guest_name.name} is eating for {self.price}")

        self.customers = []


john = Employee('John')
jane = Guest('Jane')
restaurant = Restaurant('Galactica', 10)
print(restaurant)  # should print: Galactica | 0 customers | menu for 10$ | income: 0
restaurant.sit(john, jane)
print(restaurant)  # should print: Galactica | 2 customers | menu for 10$ | income: 0
restaurant.serve_menu()  # should print: John is eating for 5.0\nJane is eating for 10
print(restaurant)  # should print: Galactica | 0 customers | menu for 10$ | income: 15
