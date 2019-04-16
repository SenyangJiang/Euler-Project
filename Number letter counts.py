d = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8];
t = [0,0,6,6,5,5,5,7,6,6]
def letter(num):
	if(num < 20):
		return d[num];
	if(num >= 20 and num < 100):
		return t[num // 10] + d[num % 10];
	if(num == 1000):
		return 11;
	if(num >= 100):
		if(num % 100 == 0):
			return d[num // 100] + 7;
		else:
			return d[num // 100] + 10 + letter(num % 100);
s = 0;
for i in range(1, 1001):
	s = s + letter(i);
	print([i,s]);

print(s);
