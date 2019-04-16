def fibonacci(num):
	c = 0;
	a = 0;
	b = 1;
	for i in range(1,num):
		c = a + b;
		a = b;
		b = c;
	return c;
i = 1;
while(len(str(fibonacci(i))) < 1000):
	i = i + 1;
print(i);
