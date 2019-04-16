def prime(num, p):
	for i in p:
		if(num % i == 0):
			return False;
	return True;

s = 2;
p = [2];
i = 3;
while(i < 2000000):
	if(prime(i,p)):
		s = s + i;
		print(i);
		p.append(i);
	i = i + 2;
print(s);