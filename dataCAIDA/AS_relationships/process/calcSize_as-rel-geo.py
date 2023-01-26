
fName = 'raw/201603.as-rel-geo.txt'

ifile = open(fName,'r')


li = []
setAS = set()
countEdge = 0
max = 0
for line in ifile:
    if line[0] == '#':
        continue # comment
    listLine = line.split('|')
    countEdge += 1
    setAS.add(listLine[0])
    setAS.add(listLine[1])


print(countEdge,len(setAS),countEdge/len(setAS))