from include import *



if __name__ == '__main__':
    limit = 3
    list_country = readList('dataCAIDA/ASN_lookup/country_list') 
    filtered_country = list_country.copy()
    for year in range(2001,2023+1):
        new_filtered_country = filtered_country.copy()
        for country in filtered_country:
            ifile = open(f'playEgOnData/results/{year}0101/by_country/{country}/neighbors_count_by_country','r')
            count = 0
            for line in ifile:
                count += 1
            if count < limit:
                new_filtered_country.remove(country) 
        filtered_country = new_filtered_country
    ofile = open(f'dataCAIDA/ASN_lookup/filterd_{limit}_neighbor_country_list','w')
    for cc in filtered_country:
        ofile.write(cc+'\n')



