print("***Stroka naoborot:***")
st = input("Vvedite stroku: ")
def reverse(st):
	res = st[::-1]
	print(res)
reverse(st)


print("***Proverka vhojdeniya v diapazon:***")
dia = input("Vvedite diapazon:").split()
num = input("Vvedite chislo:")
def proverka(dia,num):
	if (num>dia[0]) and (num<dia[1]):
		print('True')
	else: print("False")
proverka(dia,num)


print("***Ne palindrom?***")
pali = input("Vvedite slovo:")
def pal(pali):
	a = pali[::-1]
	if pali == a:
		print("True")
	else: print("False")
pal(pali)