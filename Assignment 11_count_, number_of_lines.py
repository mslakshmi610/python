fname="abc.txt"
count = 0
with open(fname,"r") as f:
	for line in f:
		count += 1
		print("Total numbers of lines is:",count)