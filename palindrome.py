def palindrome(num):
	string_num = str(num);
	i = 0;
	j = len(string_num) - 1;
	while(j > i):
		if(int(string_num[i]) != int(string_num[j])):
			return False;
		i = i + 1;
		j = j - 1;
	return True;

palin = 0;
i = 100;

while(i <= 999):
	j = 100;
	while(j <= 999):
		if(palindrome(i * j)):
			if(i * j > palin):
				palin = i * j;
		j = j + 1;
	i = i + 1;
print(palin);