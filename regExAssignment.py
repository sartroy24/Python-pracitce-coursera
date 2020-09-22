import re
fname = input("Enter the file Name Dude: ")
fh = open(fname)
text = fh.read()
words = re.findall('[0-9]+',text)
sum = 0
for i in range(len(words)):
    sum= int(words[i])+sum
print(sum)
