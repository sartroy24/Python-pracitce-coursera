import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for key,val in lst:
    print(key,val)

   