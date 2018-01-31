#first version
# x,y = [int(i) for i in input("enter 2 numbers: ").split()]
# res = None
# try:
# 	res=x/y
# except:
# 	print('Cant divide {} by {}'.format(x,y))

# print(res)

#second version
def div(x,y):
	return x/y

is_running = 'Y'

while is_running= 'Y':
	try:
		x,y = [int(i) for i in input("enter 2 numbers: ").split()]
		print('result', div(x,y))
	except:
		print("Error: Cant divide")
	is_running = input("Do you want to continue? (Y,N)")