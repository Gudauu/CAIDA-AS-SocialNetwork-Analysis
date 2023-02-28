import re

ifile = open('dataCAIDA/ASN_lookup/ASN_lookup.html','r')
ofile = open('dataCAIDA/ASN_lookup/ASN_lookup','w')

#<a href="/cgi-bin/as-report?as=AS0&view=2.0">AS0    </a> -Reserved AS-, ZZ
pattern = r'AS(\d+)\s*</a>\s+(.*)$'
dict_ASN_info = {}

for line in ifile:
    if line.startswith("<a href="):
        try:
            # Use re.search() to find the match
            match = re.search(pattern, line)

            # Extract the ASN and name from the match object
            asn = match.group(1)
            name = match.group(2)
            dict_ASN_info[asn] = name
        except Exception as e:
            print(e)


for asn, info in dict_ASN_info.items():
    ofile.write(f'{asn}:{info}\n')