def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

original_str = "ababa"
num_queries = 4
queries = [[2,3,3,4], [1,2,3,4], [1,3,3,5], [2,4,1,5]]

for i in range(num_queries):
	query = queries[i]
	middle_part = reverse(original_str[query[0]-1:query[1]])
	new_str = original_str[0:query[0]-1] + middle_part + original_str[query[1]:]
	print("News string formed: " + new_str)
	p_str = new_str[query[2]-1:query[3]]
	print("Substring extracted: " + p_str)
	if reverse(p_str) == p_str:
		print("Yes")
	else:
		print("No")