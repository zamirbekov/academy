class Figure(object):
	def __init__(self, a,b,*args):
		self.a = a
		self.b = b
		

class Rectangle(Figure):
	def __init__(self,a,b):
		self.name = 'Rectangle'
		self.a = a
		self.b = b
		super(Rectangle, self).__init__(a,b)

	def square(self,a,b):
		return a*2+2*b

	def area(self,a,b):
		return a*b
	

class Triangle(Figure):
	def __init__(self,a,b,c):
		self.name = 'Triangle'
		super(Triangle, self).__init__(a,b,c)

	def squares(self,a,b,c):
		s = (a + b + c) / 2
		return (s*(s-a)*(s-b)*(s-c)) ** 0.5 

if __name__ == '__main__':
	a = Rectangle(20,30)
	print('The square of {} is - {} and area - {}'.format(a.name, a.square(4,5), a.area(4,6)))

	b = Triangle(20,30,40)
	print('The square of {} is - {}'.format(b.name, b.squares(4,5,6)))