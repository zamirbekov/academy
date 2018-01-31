class A(object):
	def __init__ (self, id, name, age): #constructor - create new object
		self.name = name
		self.id = id
		self.age = age
		self.is_dead = False


	def set_new_name(self,name):
		self.name = name

	def clear_name(self):
		self.name = ''

	def get_age(self):
		return self.age

	def celebrate_birthday(self):
		new_age = self.age +1
		if new_age>30:
			self.is_dead = True
			print('{} died at {}'.format(self.name, new_age))
		else:
			self.age = new_age




if __name__ == '__main__':
	a = A(1, 'first', 12) #sozdaem noviy object
	b = A(2, 'second', 22)
	print(a.id, a.name)
	print(b.id, b.name)
	b.set_new_name('aaaa')
	a.clear_name()
	print(a.id, a.name)
	print(b.id, b.name)
	print('a is {} years old'.format(a.get_age()))
	print('b is {} years old'.format(b.get_age()))
	b.celebrate_birthday()
	print('a', a.get_age())
	print('b', b.get_age())
	while(not b.is_dead):
		b.celebrate_birthday()
		print('{} has reached {}'.format(b.name, b.get_age()))