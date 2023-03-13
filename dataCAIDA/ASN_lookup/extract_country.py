

ifile_name = 'dataCAIDA/ASN_lookup/ASN_lookup'

ifile = open(ifile_name,'r')
set_country = set()

for line in ifile:
    code = line[-3:-1]
    set_country.add(code)


print(len(set_country))

ofile = open('dataCAIDA/ASN_lookup/country_list','w')
for code in set_country:
    ofile.write(f'{code}\n')

ofile.close()
