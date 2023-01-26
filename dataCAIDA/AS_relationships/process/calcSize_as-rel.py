
fName = 'raw/20230101.as-rel.txt'

ifile = open(fName,'r')


li0 = []
li1 = []
setAS0 = set()
setAS1 = set()
countEdge0 = 0
countEdge1 = 0
max0 = 0
max1 = 0
# dictEdge0 = {}
# dictEdge1 = {}
for line in ifile:
    if line[0] == '#':
        continue # comment
    listLine = line.split('|')
    if int(listLine[-1]) == 0:
        max0 = max(max0,max(int(listLine[0]),int(listLine[1])))
        countEdge0 += 1
        setAS0.add(listLine[0])
        setAS0.add(listLine[1])

        # if int(listLine[0]) not in dictEdge0:   
        #     dictEdge0[int(listLine[0])] = [int(listLine[1])]
        # else:
        #     dictEdge0[int(listLine[0])].append(int(listLine[1]))


    else:
        max1 = max(max1,max(int(listLine[0]),int(listLine[1])))
        countEdge1 += 1
        setAS1.add(listLine[0])
        setAS1.add(listLine[1])


print(countEdge0,countEdge1,len(setAS0),len(setAS1),countEdge0/len(setAS0),countEdge1/len(setAS1))