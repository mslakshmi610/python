list = [1, 2, 3, 4, 5, 6]
print("original list:")
print (list)
for i in list:
	if(i%2 == 0):
		list.remove(i)
	print ("list after removing even numbers:")
	print (list)