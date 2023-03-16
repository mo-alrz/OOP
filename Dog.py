class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Dog):
            return self.name == other.name and self.age == other.age
        return False


dog1 = Dog('Furkesz', 5)
dog2 = Dog('Furkesz', 5)
print(dog1 == dog2)
