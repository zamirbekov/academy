def not_zero(func):
	def wrap(x,y):
		if y==0:
			print("DELIT NA NOL NELZYA!")
		else:
			return func(x,y)
	return wrap

@not_zero
def div(x, y):
    return x / y

print(div(6,2))
print('**'*30)
def dec(func):
	def wrap(x):
		if int(x) and len(x)==12:
			print('Vash nomer pravilnyi')
	return wrap
@dec
def print_phone_number(phone):
    print(phone)

print_phone_number('996771010427')