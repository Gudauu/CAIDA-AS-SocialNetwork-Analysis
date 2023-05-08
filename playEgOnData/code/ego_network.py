from include import *

def get_ego(asn:int, year:int,version:str="0101"):
    g = getG(f"{year}{version}", flag_directed=True, flag_nx=True)

    # Create an ego network around the central node
    ego_network = nx.ego_graph(g, asn, 1)
    dict_degree = {n:nx.degree(g,n) for n in ego_network.nodes}

    ofile_dict = open(f"report/R/AS_ego_network/middle/degree_{asn}_{year}{version}",'w')
    for _asn, degree in dict_degree.items():
        ofile_dict.write(f"{_asn}:{degree}\n")
    ofile_dict.close()

    nx.write_graphml(ego_network, f"report/R/AS_ego_network/middle/{asn}_{year}{version}.graphml")

    


if __name__ == '__main__':
    asn = 855 #6295 # 9186
    for year in range(2000,2023 + 1):
        get_ego(asn, year)  #12683 49102
    # test()




# def test():
#     # Create a graph in networkx
#     G = nx.Graph()
#     G.add_edges_from([(1,2),(2,3),(3,4),(4,1),(2,4),(1,3)])

#     # Save the graph in GraphML format
#     nx.write_graphml(G, "report/R/AS_ego_network/middle/test.graphml")
#     # Show the plot
#     # plt.show()
