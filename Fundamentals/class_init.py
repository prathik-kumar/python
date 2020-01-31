#attributes can be provided during runtime, using init method
class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

# two variables are instantiated
python = Snake('python')
anaconda = Snake('anaconda')

# print the names of the two variables
print(python.name)
print(anaconda.name)
