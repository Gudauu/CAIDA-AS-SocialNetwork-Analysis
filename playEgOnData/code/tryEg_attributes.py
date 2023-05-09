from include import getG,nx,ic,readDict


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

def calc_center(year:int, version:str= '0101') -> list:
    g = getG(f"{year}{version}",flag_directed=False, flag_nx=True)
    list_center = [str(n) for n in nx.center(g)]

    ofile = open(f'playEgOnData/results/{year}{version}/center','w')
    ofile.write(','.join(list_center))
    ofile.write("\n")
    
def annotate_center(dict_asn_info, year:int, version:str= '0101') -> None:
    with open(f'playEgOnData/results/{year}{version}/center') as f:
        first_line = f.readline().strip('\n')
    li_asnCenter = first_line.split(',')
    
    ofile = open(f'playEgOnData/results/{year}{version}/center_annotated','w')

    for asn in li_asnCenter:
        ofile.write(f'{asn}:{dict_asn_info[asn]}\n')
    ofile.close()





if __name__ == '__main__':
    dict_asn_info = readDict('dataCAIDA/ASN_lookup/ASN_lookup')
    ofile_exception = open('playEgOnData/results/log_exception','w')
    for year in range(2000,2000+1):
        try:
            # calc_attributes(year)
            annotate_center(dict_asn_info, year, version = '0101')
        except Exception as e:
            ic(e)
            ofile_exception.write(f'{e}\n')
            pass
    ofile_exception.close()



    