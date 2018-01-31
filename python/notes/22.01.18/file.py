filename = input("Enter the new filename: ")

fopen = open(filename, 'r') #failovyi deskriptor
try:
	data = fopen.read() #readlines - kajdaya stroka kak massiv spiska, readline - pervaya stroka tol'ko
	data = int(data)
	print(data)
except Exception as e:
	print('Error caught', e)
finally:
	fopen.close()
	print('Closed')