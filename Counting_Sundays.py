month = [0,31,28,31,30,31,30,31,31,30,31,30,31];
count = 0;
s = 1; #day 1 is Tuesday. day 6 is Sunday
for i in range(1, 101):
	for j in range(1,13):
		if(i % 4 == 0 and j == 2):
			s = s + 1;
		s = s + month[j];
		if((s + 1) % 7 == 0):
			count = count + 1;

print(count);