def divisible(num):
	i = 2;
	while(i < 21):
		if(num % i != 0):
			return False;
		i = i + 1;
	return True;

num = 2*3*5*7*11*13*17*19;
while(divisible(num) == False):
	print(num);
	num = num + 2*3*5*7*11*13*17*19;
print(num);