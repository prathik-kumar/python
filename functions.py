#import math gives access to math modules
import math

def my_func():
	print("my function") #indentation ends the function here

def another_func(val):
	return val*100

def repeat_print(s, times):
	print(s*times)

def hypotenuse(x,y):
	return math.sqrt(x**2 + y**2)

my_func()

a = another_func(5)
print("a:"+str(a))

repeat_print("$", 5)

b=5
print("hypotenuse: "+str(hypotenuse(a, another_func(b))))
