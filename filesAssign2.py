# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read().rstrip()
doubltxt = inp.split()
finalArr = list()
for word in doubltxt:
    if word in finalArr:
        continue
    finalArr.append(word)
finalArr.sort()
print(finalArr) 
