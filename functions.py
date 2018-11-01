# exploring functions
# and what they do


def greeting():
	#say hello
	print("Hello from your first function!");


#this will call or invoke a function
greeting()


def greetings(msg="Hello there!", num=0):
	print("Our function says", msg, "the second arg is", num)


greetings()
greetings("This is an argument", 1)
greetings("Why are we arguing?", 2)


def add_numbers(x, y, z):
	a = x + y
	b = y + z
	c = z + x
	print(a, b, c)


add_numbers(44, 53, 120)


myvarnum = 0


def somemath(num1=2, num2=5):
	global myvarnum

	myvarnum = num1 + num2
	return num1 + num2


sum = somemath()
print("our sum var is:", sum, "myvarnum is also", sum)


