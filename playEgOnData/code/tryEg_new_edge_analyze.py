from include import *

# new list format: [node1|node2|type|degree1|degree2|es1|es2|constraint1|contraint2|community1:size|community2:size]
def analyze_edge(edges:list,dictDegree,dictEffcsize,dictConstraint,dictCommunity) -> list:
    list_edges_annotated = []
    for edge_line in edges:
        list_edge = (edge_line[:-1]).split("|")
        node1 = list_edge[0]
        node2 = list_edge[1]
        community1 = None
        community2 = None
        for id,community in dictCommunity.items():
            if node1 in community:
                community1 = id
            if node2 in community:
                community2 = id
            if community1 != None and community2 != None:
                break
        for toadd in [
            dictDegree[node1],dictDegree[node2],
            dictEffcsize[node1],dictEffcsize[node2],
            dictConstraint[node1],dictConstraint[node2],
            community1, len(dictCommunity[community1]), community2, len(dictCommunity[community2])
            ]:
            list_edge.append(toadd)
        list_edges_annotated.append(list_edge)
    return list_edges_annotated


def readCommunity(fn) -> dict:
    ifile = open(fn,'r')
    dictCommunity = {}
    lastCommunity = None
    for line in ifile:
        if line.startswith('community'):
            lastCommunity = ((line[:-1]).split(' '))[1]
        else:
            dictCommunity[lastCommunity] = (line[1:-2]).split(', ')
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
    version_new = getVersionFromName(fn)
    dict_constraint = readDict('playEgOnData/results/'+version_new+'/constraint')
    dict_effective_size = readDict('playEgOnData/results/'+version_new+'/effective_size')
    dict_degree = readDict('playEgOnData/results/'+version_new+'/degree_top',': ')
    dict_community = readCommunity('playEgOnData/results/'+version_new+'/communityDetection_LPA')
    edge_new_anotated = analyze_edge(edge_new,dict_degree,dict_effective_size,dict_constraint,dict_community)
    ofile = open('playEgOnData/results/'+version_new+'/edge_added_annotated','w')
    # new list format: [node1|node2|type|degree1|degree2|es1|es2|constraint1|contraint2|community1:size|community2:size]

    for list_edge in edge_new_anotated:
        ofile.write(str(list_edge[0])+' | '+str(list_edge[1])+ '|'+str(list_edge[2])+'\n')
        ofile.write("degree: " + str(list_edge[3])+' | '+str(list_edge[4])+'\n')
        ofile.write("eff size: " + str(list_edge[5])+' | '+str(list_edge[6])+'\n')
        ofile.write("constraint: " + str(list_edge[7])+' | '+str(list_edge[8])+'\n')
        ofile.write("community: " + str(list_edge[9])+'('+str(list_edge[10])+ ') | '+str(list_edge[11])+'('+str(list_edge[12])+  ')\n\n')

    edge_removed = list(seto - setn) 
    version_old = getVersionFromName(fo)
    dict_constraint = readDict('playEgOnData/results/'+version_old+'/constraint')
    dict_effective_size = readDict('playEgOnData/results/'+version_old+'/effective_size')
    dict_degree = readDict('playEgOnData/results/'+version_old+'/degree_top',': ')
    dict_community = readCommunity('playEgOnData/results/'+version_old+'/communityDetection_LPA')
    edge_removed_anotated = analyze_edge(edge_removed,dict_degree,dict_effective_size,dict_constraint,dict_community)

    ofile = open('playEgOnData/results/'+version_new+'/edge_reomved_annotated','w')
    # new list format: [node1|node2|type|degree1|degree2|es1|es2|constraint1|contraint2|community1:size|community2:size]

    for list_edge in edge_removed_anotated:
        ofile.write(str(list_edge[0])+' | '+str(list_edge[1])+ '|'+str(list_edge[2])+'\n')
        ofile.write("degree: " + str(list_edge[3])+' | '+str(list_edge[4])+'\n')
        ofile.write("eff size: " + str(list_edge[5])+' | '+str(list_edge[6])+'\n')
        ofile.write("constraint: " + str(list_edge[7])+' | '+str(list_edge[8])+'\n')
        ofile.write("community: " + str(list_edge[9])+'('+str(list_edge[10])+ ') | '+str(list_edge[11])+'('+str(list_edge[12])+  ')\n\n')



def analyze_result(fn) -> None:
    ifile = open(fn,'r')
    count_same_community = 0
    count_both_small = 0
    count_big_small = 0
    for line in ifile:
        if line.startswith("community:"):
            line_list = (line[11:-1].replace(" ", "")).split('|')
            if line_list[0] == line_list[1]:
                count_same_community += 1 
    # print("# " + str(count_both_small) + "are both small communities\n")
    




    






if __name__ == '__main__':
    for i in range(1,4):
        # analyze_new_edges(listFileName_1998[i-1],listFileName_1998[i])
        analyze_result('playEgOnData/results/'+getVersionFromName(listFileName_1998[i])+'/edge_added_annotated')