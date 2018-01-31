try:
	print('res', 10/0)
except ZeroDivisionError as e:
	print('Cant')
else:
	print('Works when all ok')
finally:
	print('This always print on screen')