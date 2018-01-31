def div(x,y):
	return x/y

is_running = 'Y'

while is_running== 'Y':
	try:
		x,y = [int(i) for i in input("enter 2 numbers: ").split()]
		print('result', div(x,y))
	except ZeroDivisionError as e:
		print("Error: Cant divide",e)
	except ValueError as e:
		print('X or Y is invalid:', e)
	is_running = input("Do you want to continue? (Y,N)")

