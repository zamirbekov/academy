class Figure(object):
	def __init__ (self, name, *args): 
		self.name = name

	def square_of_rectangle(self,a,b):
		return a*2+2*b

	def area_of_rectangle(self,a,b):
		return a*b

	def square_of_trianle(self,a,b,c):
		return a+b+c

	def area_of_triangle(self,a,b,c):
		s = (a + b + c) / 2
		return (s*(s-a)*(s-b)*(s-c)) ** 0.5



if __name__ == '__main__':
	while input("Do you want to cont? (Y/N) ")=='Y':
		select = int(input("1.) Rectangle\n2.) Triangle\nEnter your figure: "))
		if select ==1:
			a,b = [int(x) for x in input("Enter side of rectangle: ").split()]
			rectangle = Figure('Rectanle')
			print('The area of your {} is - {} and square is - {}'.format(rectangle.name, rectangle.area_of_rectangle(a,b), rectangle.square_of_rectangle(a,b)))
		elif select==2:
			a,b,c = [int(x) for x in input("Enter sides of triange: ").split()]
			triange = Figure('Triangle')
			print('The area of your {} is - {} and square is - {}'.format(triange.name,triange.area_of_triangle(a,b,c),triange.square_of_trianle(a,b,c)))
		print('*'*40)
		