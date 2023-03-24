# from "playEgOnData/code/include.py" import *
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path



def check_top_neighbor_across_year(country:str,year_start:int,year_end:int,month:str='0101',limit:int=10):
    ofile_directory_name = 'playEgOnData/results/by_country/'+ country
    Path(ofile_directory_name).mkdir(parents=True, exist_ok=True)
    ofile = open(f'{ofile_directory_name}/top_{limit}_neighbor_across_{year_start}_{year_end}','w')

    dict_year_neib = {}

    format_width = 10
    for year in range(year_start,year_end+1):
        ofile.write(f'{year:<{format_width}}')
        dict_year_neib[year] = []
        ifile = open(f"playEgOnData/results/{year}{month}/by_country/{country}/neighbors_count_by_country",'r')
        count = 0
        for line in ifile:
            dict_year_neib[year].append(line[:-1])  # strip the last '\n'
            count += 1
            if count >= limit:
                break 

    ofile.write('\n\n')
    for i in range(limit):
        for _,list_lines in dict_year_neib.items():
            if i < len(list_lines):
                ofile.write(f'{list_lines[i]:<{format_width}}')
            else:
                ofile.write(' '*format_width)
        ofile.write('\n')
    
    ofile.close()


if __name__ == '__main__':
    check_top_neighbor_across_year('CN',2001,2023,'0101',10)

        



