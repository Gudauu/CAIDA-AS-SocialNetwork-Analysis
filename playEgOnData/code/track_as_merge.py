
from include import *
from icecream import ic
# 25462: gone after 2008, had a degree of 1174 

def track_25462():  # 9002: 1031 | 570
    G_first = getG("20080101")
    G_second = getG("20090101")
    asn = 25462

    neighbors_ori = {n for n in G_first.neighbors(asn)}
    # mark all edges with one end at node X red
    print(f"original length of neighbors: {len(neighbors_ori)}\n")

    cand_nodes = []
    for nodes, degree in sorted(G_second.out_degree().items(),key = lambda x:-x[1]):
        # if degree < len(neighbors_ori):
            # break 
        neighbors_cur = {n for n in G_second.neighbors(int(nodes))}
        if len(neighbors_ori & neighbors_cur) > 400:
            print(f'{nodes}:{degree} | {len(neighbors_ori & neighbors_cur) }')
            cand_nodes.append(nodes)

    for G in [G_first,G_second]:
        print(f'new year\n')
        set_covered = set()
        set_common = neighbors_ori
        for cand_node in cand_nodes:
            if cand_node not in G.nodes:
                continue
            set_covered = (set(G.neighbors(int(cand_node))) & neighbors_ori).union(set_covered)
            set_common = set(G.neighbors(int(cand_node))) & set_common

        print(f'len common: {len(set_common)}   len covered: {len(set_covered)}\n')

def track_asn(asn:int,version_first:str,version_second:str):  # 776 6939:1576 | 630
    G_first = getG(version_first)
    G_second = getG(version_second)

    neighbors_ori = {n for n in G_first.neighbors(asn)}
    print(f"original length of neighbors: {len(neighbors_ori)}\n")

    thresh = len(neighbors_ori)*2/3
    cand_limit = 3

    cand_nodes = []
    for nodes, degree in sorted(G_second.out_degree().items(),key = lambda x:-x[1]):
        # if degree < len(neighbors_ori):
            # break 
        neighbors_cur = {n for n in G_second.neighbors(int(nodes))}
        len_common = len(neighbors_ori & neighbors_cur)
        if  len_common > thresh:
            # print(f'{nodes}:{degree} | {len(neighbors_ori & neighbors_cur) }')
            cand_nodes.append((nodes,degree,len_common))
    cand_nodes = sorted(cand_nodes, key=lambda x:x[-1])[:cand_limit]

    for G in [G_first,G_second]:
        # print(f'version:{version_first}')
        set_covered = set()
        set_common = neighbors_ori
        for cand_node in cand_nodes:
            if cand_node not in G.nodes:
                continue
            set_covered = (set(G.neighbors(int(cand_node))) & neighbors_ori).union(set_covered)
            set_common = set(G.neighbors(int(cand_node))) & set_common
        print(f'len common: {len(set_common)}   len covered: {len(set_covered)}')


if __name__ == '__main__':
    # track_25462()
    track_asn(25462,'20080101','20090101')

    # track_22822()
    

