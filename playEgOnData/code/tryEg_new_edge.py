from include import *



def difference_between(fn_old,fn_new) -> None:
    file_old = open(fn_old,'r')
    file_new = open(fn_new,'r')
    
    version_new = fn_new[31:39]        
    version_old = fn_old[31:39]        

    node_old = set()
    for line in file_old:
        if line[0] == '#': # comment
            continue
        listLine = line.split('|')  # ASN|ASN|type
        # type_edge = int(listLine[2])
        node_old.add(listLine[0])
        node_old.add(listLine[1])

    node_new = set()
    for line in file_new:
        if line[0] == '#': # comment
            continue
        listLine = line.split('|')  # ASN|ASN|type
        # type_edge = int(listLine[2])
        node_new.add(listLine[0])
        node_new.add(listLine[1])
    
    list_node_added = node_new - node_old
    dict_degree = readDict('playEgOnData/results/'+version_new+'/degree_top')
    dict_es = readDict('playEgOnData/results/'+version_new+'/effective_size')
    ofile_added = open('playEgOnData/results/'+version_new+'/node_added','w')
    for i in list_node_added:
        ofile_added.write(str(i)+"|"+str(dict_degree[str(i)])+"|"+str(dict_es[str(i)])+'\n')

    list_node_removed = node_old - node_new
    dict_degree = readDict('playEgOnData/results/'+version_old+'/degree_top')
    dict_es = readDict('playEgOnData/results/'+version_old+'/effective_size')
    ofile_removed = open('playEgOnData/results/'+version_new+'/node_removed','w')
    for i in list_node_removed:
        ofile_removed.write(str(i)+"|"+str(dict_degree[str(i)])+"|"+str(dict_es[str(i)])+'\n')






if __name__ == '__main__':
    for i in range(1,12):
        difference_between(listFileName_1998[i-1],listFileName_1998[i])