filename = input("Enter the new filename: ")
strings = [
'new strings\n',
'new new strings\n',
'new new new strings\n',
]

fopen = open(filename, 'w') #a - append (append text)
try:
	for i in strings:
		fopen.writelines(i)
except Exception as e:
	print('Error caught', e)
finally:
	fopen.close()
	print('Closed')