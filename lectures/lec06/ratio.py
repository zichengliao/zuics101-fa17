def GoldenRatio(n):
	if n == 1:
		return 10
	else:
		return 1 + 1.0/GoldenRatio(n-1)	

n = int(input('Approximating golden ratio\ntype in a positive number: '))
print(GoldenRatio(n))
