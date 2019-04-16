def d(n):
	s = 0;
	for i in range(1,n):
		if(n % i == 0):
			s = s + i;
	return s;
s = 0;
for i in range(1, 10000):
	if(d(i) != i and i == d(d(i))):
		print(i);
		s = s + i;
print(s);