# Create a Sharpie class
#
# We should know the followings about each sharpie:
#     color (which should be a string),
#     width (which will be a number) and the
#     inkAmount (another number)
# We need to specify the color and the width at creation
# Every sharpie is created with a default ink_amount value: 100
# We can use() the sharpie objects: using it decreases ink_amount by 10


class Sharpie:
    def __init__(self, color, width, inkAmount=100):
        self.color = color
        self.width = int(width)
        self.inkAmount = int(inkAmount)

    def use(self):
        self.inkAmount -= 10
        return self.inkAmount


sharpie1 = Sharpie("Blue", 10)
print(sharpie1.use())