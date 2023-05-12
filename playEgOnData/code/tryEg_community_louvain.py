from include import *
from time import *
import community

def check_community(version) -> None:
    ifile = open(f'playEgOnData/results/{version}/community_louvain','r')
    list_len = []
    for line in ifile:
        line_list = line.split(',')
        list_len.append(len(line_list))
    
    ic(sum(list_len)/len(list_len),len(list_len), min(list_len),max(list_len))
    
def community_size(version) -> None:
    ifile = open(f'playEgOnData/results/{version}/community_louvain','r')
    dict_len = {}
    for line in ifile:
        line_list = line.split(',')
        if len(line_list) not in dict_len:
            dict_len[len(line_list)] = 1
        else:
            dict_len[len(line_list)] += 1
    ofile = open(f'playEgOnData/results/{version}/community_louvain_size_distribution','w')
    for k,v in sorted(dict_len.items()):
        ofile.write(f'{k}:{v}\n')
    ofile.close()


if __name__ == '__main__':
    DEBUG = True
    check_community('20200101')
    # versions = ['19980101','19980201','19980301','19980401']
    # for year in range(2000,2023+1):

    #     version = f"{year}0101"
        # community_size(version)

        # G = getG(version, flag_directed = False, flag_nx = True)

        # # run community detection louvain
        # # Run Louvain community detection algorithm
        # partition = community.best_partition(G)

        # # Create a dictionary to store the communities
        # communities = {}

        # # Loop through each node and its community assignment
        # for node, community_id in partition.items():
        #     # If the community doesn't exist yet, create a new one
        #     if community_id not in communities:
        #         communities[community_id] = []

        #     # Add the node to the community
        #     communities[community_id].append(str(node))
        # ofile = open(f"playEgOnData/results/{version}/community_louvain","w")
        # # Print the communities in an easy-to-read format
        # for i, nodes in communities.items():
        #     ofile.write(f"{','.join(sorted(nodes))}\n")
        #     # print(f"Community {i}: {', '.join(sorted(nodes))}")

        # ofile.close()

    

    
    
    
    