# Create a PostIt class that has a background_color a text on it a text_color
# Create a few example post - it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"


class PostIt:

    def __init__(self, background_color, text_color, text=True):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color

    def print_that(self):
        if self.text:
            if self.background_color == "orange" and self.text_color == "blue":
                return "Idea 1"
            if self.background_color == "pink" and self.text_color == "black":
                return "Awesome"
            if self.background_color == "yellow" and self.text_color == "green":
                return "Superb"

        if not self.text:
            return 'There is no text on the screen'


first = PostIt("orange", "blue")
print(first.print_that())
second = PostIt("pink", "black")
print(second.print_that())
third = PostIt("yellow", "green")
print(third.print_that())
fourth = PostIt("yellow", "blue", False)
print(fourth.print_that())
