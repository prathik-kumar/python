#superclass definition
class Person:
	#initializaing variables
	name = ''
	age = 0
	#constructor
	def __init__(self, personName, personAge):
		self.name = personName
		self.age = personAge
	
	#class methods
	def showName(self):
		print(self.name)
	def showAge(self):
		print(self.age)
#end of superclass

#subclass
class Student(Person): #student is subclass person is superclass
	studentID = ''
	
	def __init__(self, studentName, studentAge, studentID):
		Person.__init__(self, studentName, studentAge) #Calling the superclass constructor and sending values of attributes
		self.studentID = studentID
	
	def getID(self):
		return self.studentID  #returns the value of studentID
#end of subclass

#create an object of superclass
p1 = Person("Richard", 33)
p1.showAge() #call method

#create an object of subclass
s1 = Student('Max', 22, 10120)
print(s1.getID())
s1.showAge()
s1.showName()

