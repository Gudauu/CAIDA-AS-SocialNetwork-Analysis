import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from include import *

from pathlib import Path

# read degree_top file but only those of country "c_code"
def read_degree_top_by_country(ifile_name:str,c_code:str) -> dict:
    ifile = open(ifile_name,'r')
    dict_result = {}
    for line in ifile:
        line_list = (line[:-1].replace(' ','')).split(':')
        if line_list[-1][-2:] == c_code:
            dict_result[line_list[0]] = (line_list[1],line_list[2])  # {asn:(degree,info)}
    return dict_result





def track_neighbor(version:str,country_code:str) -> None:
    ifile = "playEgOnData/results/"+version+"/degree_top"
    G = getG(version)
    # 6939: 5048:HURRICANE, US
    dict_asn = read_degree_top_by_country(ifile,country_code)
    # print(len(dict_CN))
    dict_asn_info = readDict('dataCAIDA/ASN_lookup/ASN_lookup')
    dict_count_neighbor_by_country = {}
    for asn in dict_asn.keys():
        neighbors = G.neighbors(int(asn))
        for n in neighbors:
            code = dict_asn_info[str(n)][-2:] if str(n) in dict_asn_info else '00'
            if code not in dict_count_neighbor_by_country:
                dict_count_neighbor_by_country[code] = 1
            else:
                dict_count_neighbor_by_country[code] += 1
    # print(len(dict_count_neighbor_by_country))
    ofile_directory_name = 'playEgOnData/results/'+ version + '/by_country/'+ country_code
    Path(ofile_directory_name).mkdir(parents=True, exist_ok=True)
    ofile = open(ofile_directory_name+'/neighbors_count_by_country','w')
    for asn, count in sorted(dict_count_neighbor_by_country.items(),key = lambda x:-x[1]):
        ofile.write(f'{asn}:{count}\n')




if __name__ == '__main__':
    list_country = readList('dataCAIDA/ASN_lookup/country_list') 
    for year in range(2000,2023):
        version = str(year) + '0101'
        for cc in list_country:
            track_neighbor(version,cc)
    # track_neighbor("20230101",'US')


    