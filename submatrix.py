t = int(input("Enter number of test cases: "))
for count in range(t):
	n = int(input("Enter length of square matrix: "))
	ar = []
	for i in range(n):
		ar.append(input("Enter line " + str(i+1) + ": ").split(" "))
		for j in range(n):
			ar[i][j] = int(ar[i][j])
	max_v = 0
	for i in range(n-1):
		for j in range(i, n):
			for k in range(n-1):
				for l in range(k, n):
					c = 0
					for c1 in range(i, j+1):
						for c2 in range(k, l+1):
							c = c^ar[c1][c2]
					if c > max_v:
						max_v = c
	print(max_v)