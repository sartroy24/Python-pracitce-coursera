name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    if "From" in words:
        formedWord = words[5].split(':')
        counts[formedWord[0]] = counts.get(formedWord[0],0)+1
for k,v in sorted(counts.items()):
    print(k,v)
    

       
    