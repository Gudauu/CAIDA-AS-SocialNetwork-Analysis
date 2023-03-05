from include import *


# find all the nodes that were / are in top 10 degree/ effective size and track their growth across 2000-2023

def find_top(year_start:int,year_end:int,limit:int=10) -> None:
    month = "0101"
    set_top = set()
    for year in range(year_start,year_end+1):
        version = year + month
        # add top limit from degree
        ifile_degree = open("playEgOnData/results/" + version + "/degree_top")
        count = 0
        for line in ifile_degree:
            list_line = line.split(':')
            set_top.add(str(list_line[0]))
            count += 1
            if count > limit:
                break
        # add top limit from effectivesize
        ifile_degree = open("playEgOnData/results/" + version + "/effective_size")
        count = 0
        for line in ifile_degree:
            list_line = line.split(':')
            set_top.add(str(list_line[0]))
            count += 1
            if count > limit:
                break




if __name__ == '__main__':
    ASN_lookup('6339')




