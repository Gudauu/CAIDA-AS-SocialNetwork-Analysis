
from include import *
from icecream import ic
# 25462: gone after 2008, had a degree of 1174 

def track_asn(asn:int,version_first:str,version_second:str,thresh:float):  # 776 6939:1576 | 630
    G_first = getG(version_first)
    G_second = getG(version_second)

    neighbors_ori = {n for n in G_first.neighbors(asn)}
    print(f"original length of neighbors: {len(neighbors_ori)}\n")

    cand_limit = 6

    
    cand_nodes = []
    for nodes, degree in sorted(G_second.out_degree().items(),key = lambda x:-x[1]):
        # if degree < len(neighbors_ori):
            # break 
        if int(nodes) == asn:
            continue
        neighbors_cur = {n for n in G_second.neighbors(int(nodes))}
        len_common = len(neighbors_ori & neighbors_cur)
        if  len_common > thresh:
            # print(f'{nodes}:{degree} | {len(neighbors_ori & neighbors_cur) }')
            cand_nodes.append((nodes,len_common))
    cand_nodes = sorted(cand_nodes, key=lambda x:-x[-1])[:cand_limit]

    for G in [G_first,G_second]:
        # print(f'version:{version_first}')
        set_covered = set()
        set_common = neighbors_ori
        # ic(len(set_common),len(set_covered))

        for cand_node,_ in cand_nodes:
            if cand_node not in G.nodes:
                print(f'{cand_node}: None')
                continue
            else:
                degree = G.out_degree()[int(cand_node)]
                neighbors_cur = {n for n in G.neighbors(int(cand_node))}
                print(f'{cand_node}:{degree} | {len(neighbors_ori & neighbors_cur) }')

            set_covered = (set(G.neighbors(int(cand_node))) & neighbors_ori).union(set_covered)
            set_common = set(G.neighbors(int(cand_node))) & set_common
            # ic(len(set_common),len(set_covered))

        print(f'len common: {len(set_common)}   len covered: {len(set_covered)}\n')


if __name__ == '__main__':
    # track_asn(25462,'20080101','20090101',float(3/7))   # new node 9002 by the "same" company take up its role US->US
    # original length of neighbors: 646

    # 9002: None
    # 13030:133 | 66
    # len common: 39   len covered: 512

    # 9002:1031 | 570
    # 13030:928 | 425
    # len common: 237   len covered: 600

    # track_asn(22822,'20100101','20110101',float(3/7))  # no other node seems to be taking up its role. neighbors before: 776
    # track_asn(1,'20030101','20040101',float(2/7))  # node 3356 grow a lot while 1 reduce from 663 to 161 US->US
    # original length of neighbors: 621

    # 3356:558 | 74
    # len common: 19   len covered: 408

    # 3356:1003 | 332
    # len common: 15   len covered: 476
    # track_asn(3303,'20060101','20070101',float(2/7))  # 1051 -> 629
    # original length of neighbors: 564

    # 25462:125 | 47
    # len common: 22   len covered: 491

    # 25462:501 | 284
    # len common: 119   len covered: 478
    # track_asn(14840,'20220101','20230101',float(2/7))  # 9554 -> 759, Brazil -> France
    # original length of neighbors: 4895

    # 35280:956 | 651
    # len common: 524   len covered: 4316

    # 35280:4339 | 2371
    # len common: 1144   len covered: 4018

    # track_asn(8359,'20150101','20160101',float(3/7))  # 2380 -> 1140, Russian -> Singapore
    # original length of neighbors: 1367

    # 24482:97 | 72
    # len common: 50   len covered: 1062

    # 24482:2705 | 911
    # len common: 584   len covered: 1038

    # track_asn(8220,'20060101','20070101',float(3/7))  # 1133 -> 653, no specific change
    # track_asn(39120,'20200101','20210101',float(3/7))  # 7563 -> 6407, Italy -> Hungarian
    # original length of neighbors: 3781

    # 39533:543 | 474
    # len common: 366   len covered: 3770

    # 39533:3698 | 2410
    # len common: 1293   len covered: 3456

    # track_asn(49605,'20200101','20210101',float(2/7))  # 4891 -> 777, no specific change
    # track_asn(31500,'20150101','20160101',float(2/7))  # 2363 -> 243, Antigua and Barbuda -> Singapore
    # original length of neighbors: 1205

    # 24482:97 | 70
    # len common: 29   len covered: 1188

    # 24482:2705 | 1025
    # len common: 449   len covered: 1116
    # track_asn(28260,'20190101','20200101',float(3/7))  # 4772 -> 3056, Brazil -> Brazil
    # original length of neighbors: 2418

    # 267613:160 | 126
    # len common: 4   len covered: 2337

    # 267613:2853 | 1779
    # len common: 1358   len covered: 2137

    track_asn(25462,'20080101','20090101',float(3/7))  # 1174 -> None
    # original length of neighbors: 646

    # 9002: None
    # 13030:133 | 66
    # len common: 39   len covered: 512

    # 9002:1031 | 570
    # 13030:928 | 425
    # len common: 237   len covered: 600








    
     

    

