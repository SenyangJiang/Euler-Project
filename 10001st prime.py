count = 1;
num = 1;
prime = 0;
while(count < 10001):
	num = num + 2;
	p = True;
	for i in range(2, num):
		if(num % i == 0):
			p = False;
			break;
	if(p == True):
		prime = num;
		count = count + 1;
		print(count);
print(prime);
