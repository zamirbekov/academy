#filter
a = [1, 2, 3, 4, 5, 6]
def my_filter(x,y):
	for x in y:
		return x

def filter_func(x):
	return x%2==0

even_filter= list(my_filter(filter_func, a)) 
print("Filter:",	even_filter)

#reduce
