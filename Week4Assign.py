fname = input("Enter file name: ")
fh = open(fname)
count = 0
for name in fh:
    if name.startswith('From '):
        count = count + 1
        val = name.split()
        print(val[1])
print("There were", count, "lines in the file with From as the first word")