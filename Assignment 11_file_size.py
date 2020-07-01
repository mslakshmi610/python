def file_size(fname):
    import os
    startinfo=os.start(fname)
    return startinfo.st_size
print("file size in bytes of a plain file:", file_size("abc.txt"))