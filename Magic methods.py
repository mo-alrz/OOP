class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee('Roy', 'Kent', 120000)
emp2 = Employee('Reza', 'Aghaee', 70000)

print(emp1 + emp2)

print(repr(emp1), '-', str(emp1))

print(emp1.__repr__(), '-', emp1.__str__())
