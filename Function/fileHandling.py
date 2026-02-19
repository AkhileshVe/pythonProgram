# mode 
# w for write
# r for read
# a for append 

# w+ for write and read
# r+ for read and write
# a+ for append and read


fobj = open("f1.txt", "w")

print(fobj.name)     # File name
print(fobj.mode)     # Mode (w)
print(fobj.closed)   # False (file open hai)

fobj.close()         # File close kar di

print(fobj.closed)   # True