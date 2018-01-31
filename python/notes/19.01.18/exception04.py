res = input('Do you want to proceed? (Y/N)')

if res =='Y':
	print('Yes')
elif res=='N':
	print('No')
else:
	raise ValueError('{} command is not supported'.format(res))