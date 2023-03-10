# Create a class named Order that stores The name of the burger, How many times it has been ordered, The price of the
# burger
# Create a method named GenerateOrders This method will return a List of Order, Generate 100 orders, Add the orders
# to the list
# Create a method named FindPopular that takes a List as a parameter The method should return with the following tuple:
# The name of the most ordered burger, How many times it has been ordered, The amount of income
# Test your solution in the Main method

import random


class Order:
    orders = []

    def __init__(self):
        """
        assume we have a restaurant with a menu of 4 types product and maximum number of 5 order for each customer, it's
        possible to have a dictionary for menu as well but for the sake of clarity i used list for both names and price
        """
        self.max_orders = 5
        self.burg_name = ['A', 'B', 'C', 'D']
        self.how_many = random.randint(0, self.max_orders)
        self.price = [12, 10, 8, 4]

    def generateOrders(self):
        for i in range(0, 100):
            which = random.choice(self.burg_name)
            price = self.price[self.burg_name.index(which)]
            self.orders.append((which, self.how_many, price))

        return self.orders

    def findPopular(self):
        frequency = {}
        for order in self.orders:
            if order[0] not in frequency:
                frequency[order[0]] = 1
            frequency[order[0]] += 1
        most_freq = max(frequency.keys(), key=(lambda x: x[0]))
        data = most_freq, frequency[most_freq], frequency[most_freq] * self.price[self.burg_name.index(most_freq)]
        return tuple(data)


if __name__ == '__main__':
    prod = Order()
    print(prod.generateOrders())
    print(prod.findPopular())
