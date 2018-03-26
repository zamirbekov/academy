class  A(object):
	def __init__(self, x, y, metrics = 'm'):
		self.x = x
		self.y = y
		self.metrics = 'm'

	def calc_area(self):
		return self.x*self.y

	@staticmethod #1y statichnyi metod - prostoya funksiya v klasse, ne menyet object
	def m2km(n):
		return n / 1000
		
	@classmethod #2y stat method - ssylaetsya na klass
	def another(cls, x, y):
		return cls(x / 1000, y / 1000, 'km')


if __name__=='__main__':
	x = A.m2km(4000)
	print(x)

		