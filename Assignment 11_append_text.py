def file_read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write("python assignments\n")
        myfile.write("online classes")
    txt=open(fname)
    print(txt.read())
file_read('abc.txt')