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

def node_edge_diff_count(version1:str,version2:str) -> list:
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
        list_fluc = node_edge_diff_count(cur_version, nxt_version)
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
        list_fluc = node_edge_diff_count(cur_version, nxt_version)
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

def ratio_delete_add() -> None:
    iofile = open('playEgOnData/results/2000-2023/edge_fluc','r+')
    list_add = []
    list_del = []
    for line in iofile:
        if list_add == []:
            list_add = line[:-1].split(',')
        elif list_del == []:
            list_del = line[:-1].split(',')
    list_ratio = []
    for i in range(len(list_add)):
        list_ratio.append(str("{:.2f}".format(float(list_add[i])/float(list_del[i]))))
    # ic(list_ratio)
    iofile.write(",".join(list_ratio))
    iofile.write('\n')

def add_del_nodes_degree(version:str = "0101") -> None:
    for year in range(2000,2000+1):
        dic_degree_distribution_del = {}
        dic_degree_distribution_add = {}

        version1 = f"{year}{version}"
        version2 = f"{year+1}{version}"
        # both added and deleted result will be written to version2 directory
        g1 = getG(version1)
        g2 = getG(version2)
        set_node1 = set(g1.nodes)
        set_node2 = set(g2.nodes)

        set_node_del = set_node1 - set_node2
        set_node_add = set_node2 - set_node1
        dict_degree1 = g1.degree()
        dict_degree2 = g2.degree()
        # deleted nodes
        for node in set_node_del:
            degree_cur = dict_degree1[node]
            if degree_cur not in dic_degree_distribution_del:
                dic_degree_distribution_del[degree_cur] = 1
            else:
                dic_degree_distribution_del[degree_cur] += 1

        ofile_del = open(f'playEgOnData/results/{version2}/deleted_AS_degree_distribution','w')
        for k in sorted(dic_degree_distribution_del.keys()):
            ofile_del.write(f"{k}:{dic_degree_distribution_del[k]}\n")
        ofile_del.close()
        # added nodes
        for node in set_node_add:
            degree_cur = dict_degree2[node]
            if degree_cur not in dic_degree_distribution_add:
                dic_degree_distribution_add[degree_cur] = 1
            else:
                dic_degree_distribution_add[degree_cur] += 1

        ofile_add = open(f'playEgOnData/results/{version2}/added_AS_degree_distribution','w')
        for k in sorted(dic_degree_distribution_add.keys()):
            ofile_add.write(f"{k}:{dic_degree_distribution_add[k]}\n")
        ofile_add.close()

def add_del_nodes_degree_aggregated(version:str = "0101") -> None:
    for year in range(2023,2023+1):
        dict_standards = {
            1: "<= 1",
            2: "<= 2",
            5: "<= 5",
            10: "<= 10",
            100: "<= 100",
            999999: ">100"
        }
        list_standards = list(dict_standards.keys())

        # deleted nodes
        dic_degree_distribution_del = readDict(f"playEgOnData/results/{year}{version}/deleted_AS_degree_distribution")
        
        list_aggregate_count = [0]*len(list_standards)
        for _degree, _count in dic_degree_distribution_del.items():
            degree = int(_degree)
            count = int(_count)
            which = 0
            while degree > list_standards[which]:
                which += 1
            list_aggregate_count[which] += count

        ofile_del = open(f'playEgOnData/results/{year}{version}/deleted_AS_degree_distribution_aggregated','w')
        for i in range(len(list_aggregate_count)):
            ofile_del.write(f"{dict_standards[list_standards[i]]}:{list_aggregate_count[i]}\n")
        ofile_del.close()
        # added nodes
        dic_degree_distribution_add = readDict(f"playEgOnData/results/{year}{version}/added_AS_degree_distribution")
                
        list_aggregate_count = [0]*len(list_standards)
        for _degree, _count in dic_degree_distribution_add.items():
            degree = int(_degree)
            count = int(_count)
            which = 0
            while degree > list_standards[which]:
                which += 1
            list_aggregate_count[which] += count

        ofile_add = open(f'playEgOnData/results/{year}{version}/added_AS_degree_distribution_aggregated','w')
        for i in range(len(list_aggregate_count)):
            ofile_add.write(f"{dict_standards[list_standards[i]]}:{list_aggregate_count[i]}\n")
        ofile_add.close()


def add_del_edges_community(year1:int, year2:int, version:str = "0101", flag_add = True) -> None:
    g1 = getG(f"{year1}{version}",flag_community=True)
    g2 = getG(f"{year2}{version}",flag_community=True)

    set_edge1 = set([(na,nb) for na,nb,_ in g1.edges])
    set_edge2 = set([(na,nb) for na,nb,_ in g2.edges])

    def compare(pair1, pair2):
        if pair1[0] == pair1[1]:
            if pair2[0] == pair2[1]:
                return pair1[0] - pair2[0]
            else:
                return -1
        elif pair2[0] == pair2[1]:
            return 1
        else:
            return pair1[0] - pair2[0] or pair1[1] - pair2[1]

    # add 
    if flag_add:
        set_edges = set_edge2 - set_edge1
        dict_node_community = g2.nodes
        dict_community_len = {num:len(asList) for num,asList in readCommunity(f"{year2}{version}").items()}

    else: # del
        set_edges = set_edge1 - set_edge2
        dict_node_community = g1.nodes
        dict_community_len = {num:len(asList) for num,asList in readCommunity(f"{year1}{version}").items()}

    # community info
    dict_community_len = dict(sorted(dict_community_len.items(), key = lambda x:-x[1]))
    dict_community_order = {}  # community:order
    order = 1
    for community in dict_community_len:
        dict_community_order[community] = order
        order += 1

    def compare_rank(tup):
        return (dict_community_order[tup[0]], dict_community_order[tup[1]])

    dict_communityPair_count = {}
    for n1,n2 in set_edges:
        pair_community = (dict_node_community[n1]['node_attr']['community'],dict_node_community[n2]['node_attr']['community'])
        # keep order
        if dict_community_order[pair_community[0]] > dict_community_order[pair_community[1]]:
            pair_community = (pair_community[1],pair_community[0])

        if pair_community not in dict_communityPair_count:
            dict_communityPair_count[pair_community] = 1
        else:
            dict_communityPair_count[pair_community] += 1

    # count edges from same community <> diff community
    count_same = 0
    count_all = 0
    for pair, count in dict_communityPair_count.items():
        if pair[0] == pair[1]:
            count_same += count
        count_all += count 
    ofile_R_count_same_percentage = open(f"report/R/edge_fluc_community_distribution/middle/{year2}{version}{int(flag_add)}",'w')
    percentage = "{:.2f}".format(float(count_same)/count_all)
    ofile_R_count_same_percentage.write(f"{percentage}\n")
    ofile_R_count_same_percentage.close()



    # whatever add or del, write to year2
    if flag_add:
        ofile = open(f'playEgOnData/results/{year2}{version}/added_ASR_community_distribution','w')
    else:
        ofile = open(f'playEgOnData/results/{year2}{version}/deleted_ASR_community_distribution','w')
    from functools import cmp_to_key
    for pa in sorted(dict_communityPair_count.keys(), key = compare_rank): #cmp_to_key(compare)
        ofile.write(f"{pa[0]}:{pa[1]}:{dict_communityPair_count[pa]}:{dict_community_order[pa[0]]}:{dict_community_order[pa[1]]}\n")
    ofile.close()

# if delta edges come from delta nodes
def add_del_edges_nodes_relation(year1:int, year2:int, version:str = "0101") -> list:
    g1 = getG(f"{year1}{version}",flag_community=True)
    g2 = getG(f"{year2}{version}",flag_community=True)
    set_node1 = set(g1.nodes)
    set_node2 = set(g2.nodes)
    set_node_added = set_node2 - set_node1
    set_node_deleted = set_node1 - set_node2


    set_edge1 = set([(na,nb) for na,nb,_ in g1.edges])
    set_edge2 = set([(na,nb) for na,nb,_ in g2.edges])
    set_edge_added = set_edge2 - set_edge1
    set_edge_deleted = set_edge1 - set_edge2

    # added
    count_one_end = 0
    count_both_end = 0
    for na,nb in set_edge_added:
        flag_a = na in set_node_added
        flag_b = nb in set_node_added
        if flag_a and flag_b:
            count_both_end += 1
        elif flag_a or flag_b:
            count_one_end += 1
    add_ratio = count_one_end/len(set_edge_added)
    add_ratio_both = count_both_end/len(set_edge_added)
    pct_added = len(set_node_added)/len(set_node2)
    # ic(count_one_end/len(set_edge_added), pct_added)
    # ic(count_both_end/len(set_edge_added), pct_added*pct_added)
    # deleted
    count_one_end = 0
    count_both_end = 0
    for na,nb in set_edge_deleted:
        flag_a = na in set_node_deleted
        flag_b = nb in set_node_deleted
        if flag_a and flag_b:
            count_both_end += 1
        elif flag_a or flag_b:
            count_one_end += 1
    del_ratio = count_one_end/len(set_edge_deleted)
    del_ratio_both = count_both_end/len(set_edge_deleted)
    pct_del = len(set_node_deleted)/len(set_node1)
    # ic(count_both_end/len(set_edge_deleted), pct_del*pct_del)

    return [add_ratio, pct_added, del_ratio, pct_del, add_ratio_both,del_ratio_both]
        #add_ratio_both, pct_added*pct_added, del_ratio_both, pct_del*pct_del]


def fluc_dege_node_relation_across_years(year_start:int, year_end:int,gap:int = 1) -> None:
    list_add_ratio = []  # added edges with one end in added nodes
    list_add_ratio_both = []  # added edges with no end in added nodes
    list_add_std = []
    list_del_ratio = []
    list_del_ratio_both = []
    list_del_std = []

    for year in range(year_start + 1, year_end + 1, gap):
        list_add_std_del_std = add_del_edges_nodes_relation(year_start, year)
        # ic(list_add_std_del_std)
        list_add_ratio.append(str(list_add_std_del_std[0]))
        list_add_std.append(str(list_add_std_del_std[1]))
        list_del_ratio.append(str(list_add_std_del_std[2]))
        list_del_std.append(str(list_add_std_del_std[3]))
        list_add_ratio_both.append(str(list_add_std_del_std[4]))
        list_del_ratio_both.append(str(list_add_std_del_std[5]))

    ofile = open(f'report/R/node_edge_fluc_relation/middle/{year_start}_{year_end}','w')
    for li in [list_add_ratio, list_add_std,list_del_ratio,list_del_std,list_add_ratio_both,list_del_ratio_both]:
        ofile.write(",".join(li)+'\n')


    

      





     




if __name__ == '__main__':
    # across_2000_2023("0101")
    # for year in [2006, 2010, 2014, 2018]:
    #     across_months(year)
    # ratio_delete_add()
    # add_del_nodes_degree()
    # add_del_nodes_degree_aggregated()
    # for year in range(2000, 2022 +1):
    #     add_del_edges_community(year,year + 1, flag_add=False)
    #     add_del_edges_community(year,year + 1, flag_add=True)
    across_months(2015)
    across_months(2016)
    # fluc_dege_node_relation_across_years(2000,2020)
    # fluc_dege_node_relation_across_years(2002,2022)
    # fluc_dege_node_relation_across_years(2002,2022)

