class Car(object):
	def __init__(self, year, color):
		self.year = year
		self.color = color
		self.wheels = 4
		self.distance = 0

	def ride(self):
		self.distance += 500

class MersedezBenz(Car):
	def __init__(self,year,color):
		self.name = 'Mersedes-Benz'
		super(MersedezBenz, self).__init__(year,color) #peregruzka
#else sozdat' svoi konstruktor u dochernego klassa, on ne budet ispol'zovat konstruktor roditelya
	
#sled eto polimorfizm:	
	def ride(self,n=None):
		if n is None:
			self.distance = super(MersedezBenz, self).ride()
		else:
			self.distance+=n
#mnojestvlennoe nasledie ne ispolzovat' (dva+ klassa)
class Toyota(Car):
	pass	

if __name__ == '__main__':
	c = Car(1999, 'red')
	print(c.year, c.color, c.wheels)

	m = MersedezBenz(200,'black')
	print(m.year, m.color, m.wheels)