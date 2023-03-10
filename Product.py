# Create a class named Product that stores The name of a product The price of a product The discount of a product
# (given in percentage)
# Create a method named GetDiscount that returns the following tuple: The name of the product The old Price of the
# product The newPrice of the product which is based on the discount Test your solution in the Main method

class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def getDiscount(self):
        new_price = self.price - (self.price * self.discount)
        data = self.name, self.price, new_price
        return f'(Name, oldPrice, newPrice) = {tuple(data)}'


if __name__ == '__main__':
    prod = Product('product1', 10, 0.2)
    print(prod.getDiscount())
