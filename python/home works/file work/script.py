with open('chuck.txt','r') as f: 
    k = f.read()
    length_of_symbols = len(k)


with open('abc.txt', 'w') as f:
	f.write(str(length_of_symbols))

with open('chuck.txt', 'a') as f:
	f.write('sadfk')

with open('chuck.txt', 'r') as a:
	k = a.read().upper()
	print(k.count('CHUCK NORRIS'))
