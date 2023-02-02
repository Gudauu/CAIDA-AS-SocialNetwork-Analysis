

import easygraph as eg 

def buildAsRelGraph(ifileName) -> eg.Graph:
    ifile = open(ifileName,'r')
    G = eg.Graph()

    for line in ifile:
        if line[0] == '#': # comment
            continue
        listLine = line.split('|')  # ASN|ASN|type
        G.add_edge(int(listLine[0]),int(listLine[1]),edge_attr={'type':int(listLine[2])})
    return G


if __name__ == '__main__':
    # G = eg.Graph()
    # G.add_edges([(5,6),(7,8)])
    # ofile.write(G.nodes)
    # G.edges
    ifileNames = [
        'dataCAIDA/AS_relationships/raw/20230101.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20221001.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20180701.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20110401.as-rel.txt'
    ]
    ofile = open('result','w')
    listG = []
    listNodes = []
    # basic property of each G
    for fn in ifileNames:
        G = buildAsRelGraph(fn)
        # print((list((G.degree()).values()))[:100])
        # break

        listG.append(G)
        listNodes.append(G.nodes)
        # ofile.write(G.size())
        ofile.write('size: '+str(len(G.nodes))+'\n')
        ofile.write('number of connected comp:'+str(eg.number_connected_components(G))+'\n')
        ofile.write('average degree:'+str(sum(G.degree())/len(G.degree()))+'\n')
    # node (AS) number fluctuation between adjacent G
    for i in range(len(listNodes)-1):
        ofile.write(str(i)+'-'+str(i+1)+' difference:  '+str(len(set(listNodes[i])-set(listNodes[i+1])))+'\n')
        ofile.write(str(i+1)+'-'+str(i)+' difference:  '+str(len(set(listNodes[i+1])-set(listNodes[i])))+'\n')
    # max ASN (to roughly check the change)
    for i in range(len(listNodes)):
        ofile.write('max ASN in '+str(i)+': '+str(max(listNodes[i]))+'\n')

    
    