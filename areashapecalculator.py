from math import pi, sqrt

class Shape:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def get_area(self):
		return self.length*self.breadth

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'

class Rectangle(Shape):
	pass

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)

class Triangle(Rectangle):
	def __init__(self, base, height):
		super().__init__(base, height)

	def get_area(self):
		area = super().get_area()
		return area/2

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		return pi*(self.radius**2)

class Hexagon(Square):
	def get_area(self):
		return (3*sqrt(3)*self.length**2)/2

class Run:
	def __init__(self):
		pass

	def run(self):
		print("""
		Which Shape size do you want to calculate 
		1. Rectangle
		2. Square
		3. Triangle
		4. Circle
		5. Hexagon
		6. Exit
		""")

Run().run()

selection = int(input("Please select: "))

if selection == 1:
	side1 = float(input("Enter length of Rectangle: "))
	side2 = float(input("Enter breadth of Rectangle: "))
	print(Rectangle(side1, side2))

elif selection == 2:
	side = float(input("Enter side of Square: "))
	print(Square(side))

elif selection == 3:
	base = float(input("Enter base of Triangle: "))
	height = float(input("Enter height of Triangle: "))
	print(Triangle(base, height))

elif selection == 4:
	radius = float(input("Enter radius of Circle: "))
	print(Circle(radius))

elif selection == 5:
	side = float(input("Enter side of Hexagon: "))
	print(Hexagon(side))

elif selection == 6:
	exit("Exit")

else:
	exit("Please select between 1-6!!!")