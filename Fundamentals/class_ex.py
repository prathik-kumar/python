class Snake:
	name = 'python'

	def change_name(self, new_name):   #the first argument is 'self' always
		self.name = new_name       #access the class attribute with self keyword

#instantiate the class
snake = Snake()

#print the current object name
#to access the attributes that are present inside the class using the dot . 
print(snake.name) 

 # change the name using the change_name method
snake.change_name('anaconda')
print(snake.name)

