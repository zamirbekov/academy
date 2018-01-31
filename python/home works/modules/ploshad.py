from math import pi,sqrt

def area_of_triange(a,b,c):
	s = (a + b + c) / 2
	return (s*(s-a)*(s-b)*(s-c)) ** 0.5

def area_of_square(a,b):
	return a*b

def area_of_circle(a):
	return pi*r*r

def second_formula(a,b):
	return (a**a)+(3*(a*a)*b)+(3*a*(b*b))+(b**b)

def diskriminant(a,b,c):
	d = (b*b)-(4*a*b)
	if d>0:
		x1 = (-b+sqrt(d))/(2*a)
		x2 = (-b-sqrt(d))/(2*a)
		return a*(x1*x1)+(b*x2)+c
	elif d==0:
		x = (-b+sqrt(d))/(2*a)
		return a*(x*x)+(b*x)+c
	else d<0:
		return print("Kornei net!")
	 