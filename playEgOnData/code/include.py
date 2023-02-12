import easygraph as eg 

dictInfile = {
    '20230101':'dataCAIDA/AS_relationships/raw/20230101.as-rel.txt',
    '20221001':'dataCAIDA/AS_relationships/raw/20221001.as-rel.txt',
    '20180701':'dataCAIDA/AS_relationships/raw/20180701.as-rel.txt',
    '19980101':'dataCAIDA/AS_relationships/raw/19980101.as-rel.txt',
    '20110401':'dataCAIDA/AS_relationships/raw/20110401.as-rel.txt',
    '20000301':'dataCAIDA/AS_relationships/raw/20000301.as-rel.txt',
    '19980201':'dataCAIDA/AS_relationships/raw/19980201.as-rel.txt',
    '19980301':'dataCAIDA/AS_relationships/raw/19980301.as-rel.txt',
    '19980401':'dataCAIDA/AS_relationships/raw/19980401.as-rel.txt'
}

def buildAsRelGraph(ifileName) -> eg.DiGraph:
    ifile = open(ifileName,'r')
    G = eg.DiGraph()

    for line in ifile:
        if line[0] == '#': # comment
            continue
        listLine = line.split('|')  # ASN|ASN|type
        type_edge = int(listLine[2])
        G.add_edge(int(listLine[0]),int(listLine[1]),edge_attr={'type':type_edge})
        if type_edge == 0: # peer edge
            G.add_edge(int(listLine[1]),int(listLine[0]),edge_attr={'type':type_edge})
    return G

def getG(version,DEBUG = False) -> eg.DiGraph:
    if DEBUG:
        G = eg.DiGraph()
        G.add_edges([(5,6),(7,8),(6,5),(1,20),(2,1)])
    else:  
        fn = dictInfile[version]
        G = buildAsRelGraph(fn)
    return G

