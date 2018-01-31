def hello():
	x=1
	def f1():
		y=2
		print("F1", x, y)
	def f2():
		z=3
		print("F2",x,z)
	f1()
	print("Hello world",x)
	f2()
hello()
print('-'*20)

#kompozisiya 
def func(n):
	def mul():
		return n*3
	return mul
new_func = func(7)
print(func(7)) #object
print(new_func()) #znachenie
print(func(7)()) #dob skobki
print("*"*20)

def calc_sum(a,b):
	res = a + b
	print("sum a and b", res)
	return res
x=calc_sum(2,4)
calc_sum(4,4) #print
print(x) # return

def logger(fn):
	def wrapper(a,b):
		res = fn(a,b)
		print("sum a and b", res)
		return res
	return wrapper
logger(calc_sum)(4,5)

#decorator
def pow(fn):
	def wrap(a,b):
		return fn(a**b,b)
	return wrap
@pow
def sum(a,b):
	return a+b
print(sum(2,2))


