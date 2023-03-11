from include import *


# find all the nodes that were / are in top 10 degree size in CN and track their growth across 2000-2023

def find_top(year_start:int,year_end:int,limit:int=10) -> None:
    month = "0101"
    set_top = set()
    for year in range(year_start,year_end+1):
        version = str(year) + month
        # add top limit from degree
        ifile_degree = open("playEgOnData/results/" + version + "/degree_top",'r')
        count = 0
        for line in ifile_degree:
            list_line = line.split(':')
            if ', CN' in list_line[-1]:
                set_top.add(str(list_line[0]))
                count += 1
                if count >= limit:
                    break
    # read degree again, tracking ASes inside set_top
    # output file format: 
    # ASN:company, country
    # year2000 degree | rank;   year2001 degree| rank; ...  year2023 degree| rank 

    # initialize
    dict_ASN_trace = {}
    for asn in set_top:
        dict_ASN_trace[asn] = {}  # year: degree | rank
        for year in range(year_start,year_end+1):
            dict_ASN_trace[asn][year] = 'None' # ini to None

    # go over all the degree files and record each asn in set_top
    for year in range(year_start,year_end+1):
        version = str(year) + month
        # add top limit from degree
        ifile_name = "playEgOnData/results/" + version + "/degree_top"
        dict_degree = readDict(ifile_name)
        dict_rank = readRank(ifile_name)
        for asn in set_top:
            if str(asn) in dict_rank: # chances are that some asn haven't appeared
                dict_ASN_trace[asn][year] = f'{dict_rank[str(asn)]}({dict_degree[str(asn)]})'
    
    # write the result
    ofile = open("playEgOnData/results/2000-2023/track_degree_top_CN_"+str(limit),'w')
    dict_asn_info = readDict("dataCAIDA/ASN_lookup/ASN_lookup")
    for asn in dict_ASN_trace:
        ofile.write(f'{asn} : {dict_asn_info[asn]}\n')
        for year in range(year_start,year_end+1):
            ofile.write(f'{year:<18};')
        ofile.write('\n')

        for year in range(year_start,year_end+1):
            ofile.write(f'{dict_ASN_trace[asn][year]:<18};')
        ofile.write('\n\n')
    ofile.close()







if __name__ == '__main__':
    find_top(2000,2023)




