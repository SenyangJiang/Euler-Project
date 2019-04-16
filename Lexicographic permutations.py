import itertools;
lexi = [];
a = ['0','1','2','3','4','5','6','7','8','9'];
for item in itertools.permutations(a,9):
	print(item);
	lexi.append(item);

lexi.sort();2783915406