def factor(num):
	s = 0;
	for i in range(1,num):
		if(num % i == 0):
			s = s + i;
	return s;
abundant_num = [];
for i in range(1, 28124):
	if(factor(i) > i):
		abundant_num.append(i);

print(abundant_num);



