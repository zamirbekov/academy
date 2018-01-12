from functools import reduce
#lambda
f = lambda x: x**2 

print((lambda x: x**2)(9))

def func1(x):
	def f(y):
		return x+y
	return f
print(func1(10)(2))

#filter

a = [1, 2, 3, 4, 5, 6]
def filter_func(x):
	return x%2==0
even_number = list(filter(filter_func, a)) #list(filter(lamba x: x % 2 == 0))
print(even_number)

#map

new_list = list(map(lambda x: x**2, a)) #delaet chto to s kajdym elementom
print(new_list)

#reduce

reduced_value = reduce(lambda x, y: x*y, a) #umnojaet vseh drug s drugom
print(reduced_value)

def transform(x,y):
	x['key-{}'.format(y)] = y
	return x
red_map = reduce(transform, [1,2,3], {})
print(red_map)

#a teper' farsh
obj = [
	{'year':1999, 'item':'a'},
	{'year':1355, 'item':'b'},
	{'year':1332, 'item':'c'},
	{'year':1999, 'item':'d'},
]
print(list(map(lambda x:x['item'], list(filter(lambda x:x['year']==1999, obj)))))
