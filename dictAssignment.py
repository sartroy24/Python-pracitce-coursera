name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if "But" in words:
        counts[words[1]] = counts.get(words[1],0)+1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigword is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)       
    
    # if words[0]== 'From':
    #     newWord = words[1]
    # 	counts[newWord] = counts.get(newWord,0)+1