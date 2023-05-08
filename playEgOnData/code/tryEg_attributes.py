from include import getG,nx


def calc_attributes(year:int, version:str= '0101') -> list:
    g = getG(f"{year}{version}",flag_directed=False, flag_nx=True)
    # mean_distance = nx.average_shortest_path_length(g)
    # ic(mean_distance)
    # avg_cluter_coef =  nx.average_clustering(g)
    # ic(avg_cluter_coef)
    # avg_connectivity =  nx.average_node_connectivity(g)
    # ic(avg_connectivity)
    diameter = nx.diameter(g)

    ofile = open(f'playEgOnData/results/{year}{version}/diameter','w')
    ofile.write(f"{diameter}\n")
    # radius = nx.radius(g)
    # ic(radius)
    



if __name__ == '__main__':
    for year in range(2001,2005):
        calc_attributes(year)
    