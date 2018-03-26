#esli izmenit' atribut klassa ono izmenyetsya vesde
#else izmenit' atr objecta to tolko object
class  B(object):
	p = 'aaa'
	def __init__(self, n):
		self.name = n


if __name__=='__main__':
	a = B('Test')
	b = B('Abc')

	print(a.name,a.p)
	print(b.name,b.p)

	B.p = 'qwerty'

	print(a.name,a.p)
	print(b.name,b.p)

	b.p = '23'

	print(a.name,a.p)
	print(b.name,b.p)
		