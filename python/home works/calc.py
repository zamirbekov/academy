op = input("Enter the operation: ")
num = input("Enter the numbers for operation: ").split()

def calc(op, *num):
	s=0
	if op=='+':
		for x in num:
			s=int(x)+s
	if op=='-':
		s= int(num[0])-int(num[1])
		for x in num[2:]:
			s=s-int(x)
	if op=='*':
		s=1
		for x in num:
			s=int(x)*s
	if op=='/':
		if int(num[1])==0:
			print('dele')
		else: s= int(num[0])/int(num[1])
		for x in num[2:]:
			if x=='0':
				s=0
				print("Deleni na nol:")
				break
			s=s/int(x)
	print(s)

calc(op, *num)