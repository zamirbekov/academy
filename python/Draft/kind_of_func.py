#FUNCTION

def multiply(a=0, b=0): #argument scall "imennovannye"
	print('a is {0}, b is {1} and summ is {2}'.format(a,b,a+b)) #Print with new format 
multiply(2)
multiply(a=2, b=3)

def func(a,b): #pozissionirovannye
	print(a+b)
func(1,2)

#neogranichennoe kol argumentov
def simpleArgument(*args): #vse elementy budut cortejami
	print("Arguments:")
	print("len:", len(args))
	for i in range(len(args)):
		print('{i}: {el}'.format(i=i, el=args[i]))
def KeyArgument(**kwargs): #znachenie=kluch
	print("Keyword Arguments")
	print(kwargs)
simpleArgument(1,2,4)
KeyArgument(a=4, b=4, x=True)
