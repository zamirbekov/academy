#inkapsulyasiya

class  A(object):
	def __init__(self):
		self.public_attr = 1111
		self.__privat_attr = 2222

	def print_public_attr(self):
		print(self.public_attr)

	def print_private_attr(self):
		print(self.__privat_attr) 

if __name__ =='__main__':
	a = A()
	print('public', a.public_attr)
	a.print_public_attr
