def factor(num):
	prime = 3;
	prime_factor = 0;
	i = 2;
	while(prime <= num):
		while(i < prime and prime % i != 0):
			i = i + 1;
		if(i == prime):
			if(num % prime == 0):
				prime_factor = prime;
				num = num/ prime_factor;
		prime = prime + 1;
	return prime_factor;
print(factor(600851475143));
