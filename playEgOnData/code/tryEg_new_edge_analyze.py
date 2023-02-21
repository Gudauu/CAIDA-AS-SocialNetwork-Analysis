from include import *


def analyze_edge(edges:list,dictDegree,dictEffcsize,dictConstraint,dictCommunity) -> list:
    
    for edge_line in edges:
        list_edge = (edge_line[:-1]).split("|")


def readCommunity(fn) -> dict:
    ifile = open(fn,'r')
    dictCommunity = {}
    lastCommunity = None
    for line in ifile:
        if line.startswith('community'):
            lastCommunity = ((line[:-1]).split(' '))[1]
        else:
            dictCommunity[lastCommunity] = list(line[:-1])
    return dictCommunity




def analyze_new_edges(fo,fn) -> None:
    ifo = open(fo,'r')
    ifn = open(fn,'r')
    seto = set()
    setn = set()
    for line in ifo:
        if line[0] == '#':
            continue
        seto.add(line)
    for line in ifn:
        if line[0] == '#':
            continue
        setn.add(line)
    edge_new = list(setn - seto)
    edge_removed = list(seto - setn) 
    version_new = getVersionFromName(fn)
    dict_constraint = readDict('playEgOnData/results/'+version_new+'/constraint')
    dict_effective_size = readDict('playEgOnData/results/'+version_new+'/effective_size')
    dict_degree = readDict('playEgOnData/results/'+version_new+'/degree_top')
    dict_community = readCommunity('playEgOnData/results/'+version_new+'/communityDetection_LPA')
    edge_new_anotated = analyze_edge(edge_new,dict_degree,dict_effective_size,dict_constraint,dict_community)




    






if __name__ == '__main__':
    for i in range(1,12):
        analyze_new_edges(listFileName_1998[i-1],listFileName_1998[i])