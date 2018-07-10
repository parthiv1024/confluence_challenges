t = int(input("Enter number of test cases: "))
for i in range(t):
	tags = input("Enter the string of tags: ")
	balance = 0
	longest_prefix = 0
	prefix = 1
	for tag in tags:
		if tag == "<":
			balance += 1
		if tag == ">":
			balance -= 1
		if balance == 0:
			longest_prefix = prefix
		if balance < 0:
			break
		prefix += 1
	print(longest_prefix)