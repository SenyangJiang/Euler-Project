import math;

def factor(num):
	count = 0;
	i = 1;
	while(i <= int(math.sqrt(num))):
		if(num == i*i):
			count = count + 1;
		if(num % i == 0):
			count = count + 2;
		i = i + 1;
	print(count);
	return count;

num = 1;
while(factor((num+1)*num/2)<501):
	num = num + 1;

print((num+1)*num/2);