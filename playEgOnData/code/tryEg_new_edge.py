import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from include import *

from pathlib import Path
from icecream import ic


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

def node_edge_diff(version1:str,version2:str) -> list:
    g1 = getG(version1)
    g2 = getG(version2)
    set_node1 = set(g1.nodes)
    set_node2 = set(g2.nodes)

    count_node_new = len(set_node2 - set_node1)
    count_node_gone = len(set_node1 - set_node2)

    set_edge1 = set([(na,nb) for na,nb,_ in g1.edges])
    set_edge2 = set([(na,nb) for na,nb,_ in g2.edges])

    count_edge_new = len(set_edge2 - set_edge1)
    count_edge_gone = len(set_edge1 - set_edge2)

    # ic(count_node_new,count_node_gone,count_edge_new,count_edge_gone)
    return [count_node_new, count_node_gone, count_edge_new, count_edge_gone]

def across_2000_2023(version:str = "0101") -> None:
    list_node_new = []
    list_node_gone = []
    list_edge_new = []
    list_edge_gone = []

    
    for year in range(2000,2022+1):
        cur_version = f"{year}{version}"
        nxt_version = f"{year+1}{version}"
        list_fluc = node_edge_diff(cur_version, nxt_version)
        list_node_new.append(str(list_fluc[0]))
        list_node_gone.append(str(list_fluc[1]))
        list_edge_new.append(str(list_fluc[2]))
        list_edge_gone.append(str(list_fluc[3]))


    ofile = open('playEgOnData/results/2000-2023/node_edge_fluc','w')
    ofile.write(",".join(list_node_new))
    ofile.write("\n")
    ofile.write(",".join(list_node_gone))
    ofile.write("\n")
    ofile.write(",".join(list_edge_new))
    ofile.write("\n")
    ofile.write(",".join(list_edge_gone))
    ofile.write("\n")

def across_months(year:str) -> None:
    list_node_new = []
    list_node_gone = []
    list_edge_new = []
    list_edge_gone = []

        
    for month in range(1,11+1):
        def get_version(month:int):
            if month < 10:
                return f"0{month}01"
            else:
                return f"{month}01"

        cur_version = f"{year}{get_version(month)}"
        nxt_version = f"{year}{get_version(month + 1)}"
        list_fluc = node_edge_diff(cur_version, nxt_version)
        list_node_new.append(str(list_fluc[0]))
        list_node_gone.append(str(list_fluc[1]))
        list_edge_new.append(str(list_fluc[2]))
        list_edge_gone.append(str(list_fluc[3]))

    ofile_directory = f'playEgOnData/results/{year}'
    Path(ofile_directory).mkdir(parents=True, exist_ok=True)
    ofile = open(ofile_directory+'/node_edge_fluc_by_month','w')

    ofile.write(",".join(list_node_new))
    ofile.write("\n")
    ofile.write(",".join(list_node_gone))
    ofile.write("\n")
    ofile.write(",".join(list_edge_new))
    ofile.write("\n")
    ofile.write(",".join(list_edge_gone))
    ofile.write("\n")




if __name__ == '__main__':
    # across_2000_2023("0101")
    across_months("2003")