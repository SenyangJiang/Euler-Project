i = 3;
max_count = 1;
while(i < 1000000):
	j = i;
	count = 1;
	while(j != 1):
		if(j % 2 == 0):
			j = int(j / 2);
			count = count + 1;
		else:
			j = 3*j + 1;
			count = count + 1;
	if(count > max_count):
		max_count = count;
		print(i);
	i = i + 2;

