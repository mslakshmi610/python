f = open("xyz.txt","w")
s=' ' ' hello world ! ! ! everyone ' ' '
f.write(s)
f.close()

f2 = open("xyz1.txt","w")
f1 = open("xyz.txt","r")
for line in f1 :
	f2.write(line)
	f1.close()
	f2.close()
	
	f3 = open("xyz1.txt","r")
	s1 = f3.read()
	print(s1)
	f3.close()