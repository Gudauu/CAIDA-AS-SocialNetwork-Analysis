
from include import *
from icecream import ic
# 25462: gone after 2008, had a degree of 1174 

def track_asn(asn:int,version_first:str,version_second:str):  # 776 6939:1576 | 630
    G_first = getG(version_first)
    G_second = getG(version_second)

    neighbors_ori = {n for n in G_first.neighbors(asn)}
    print(f"original length of neighbors: {len(neighbors_ori)}\n")

    thresh = len(neighbors_ori)*3/7
    cand_limit = 3

    

    for G in [G_first,G_second]:
        # print(f'version:{version_first}')
        cand_nodes = []
        for nodes, degree in sorted(G.out_degree().items(),key = lambda x:-x[1]):
            # if degree < len(neighbors_ori):
                # break 
            if int(nodes) == asn:
                continue
            neighbors_cur = {n for n in G.neighbors(int(nodes))}
            len_common = len(neighbors_ori & neighbors_cur)
            if  len_common > thresh:
                print(f'{nodes}:{degree} | {len(neighbors_ori & neighbors_cur) }')
                cand_nodes.append(nodes)
        # cand_nodes = sorted(cand_nodes, key=lambda x:x[-1])[:cand_limit]

        set_covered = set()
        set_common = neighbors_ori
        # ic(len(set_common),len(set_covered))
        for cand_node in cand_nodes:
            # if cand_node not in G.nodes:
            #     continue
            set_covered = (set(G.neighbors(int(cand_node))) & neighbors_ori).union(set_covered)
            set_common = set(G.neighbors(int(cand_node))) & set_common
            # ic(len(set_common),len(set_covered))

        print(f'len common: {len(set_common)}   len covered: {len(set_covered)}\n')


if __name__ == '__main__':
    # track_asn(25462,'20080101','20090101')
    track_asn(22822,'20100101','20110101')

    # track_22822()
    

