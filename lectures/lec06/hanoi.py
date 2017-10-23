def Hanoi(n, S, V, T):
	if n == 1:
		print('Move %i: from %s to %s'%(n, S, T))
	else:
		Hanoi(n-1, S, T, V)
		print('Move %i: from %s to %s'%(n, S, T))
		Hanoi(n-1, V, S, T)	

n = int(input('Computing Hanoi Tower solution\ntype in a positive number: '))
Hanoi(n, 'A', 'B', 'C')
