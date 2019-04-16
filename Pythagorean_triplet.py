def Pythagorean(a,b,c):
	return a**2 + b**2 == c**2;
a = 100;
while(a < 500):
	b = a;
	while(b < 500):
		if(Pythagorean(a,b,1000-a-b)):
			print([a,b,1000-a-b]);
		b = b + 1;
	a = a + 1;
