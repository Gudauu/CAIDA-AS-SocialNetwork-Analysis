



def get_top_N_AS(year:int,version = '0101',top = 10):
    ifile = open(f'playEgOnData/results/{year}{version}/degree_top')
    count = 0
    list_AS = []
    for line in ifile:
        line_list = line.split(':')
        list_AS.append(line_list[0])
        count += 1
        if count == top:
            break 
    str_R = ','.join(list_AS)
    print(str_R)

def get_custom_range_N_AS(year:int,version:str = '0101',start:int = 200, end:int = 210):
    ifile = open(f'playEgOnData/results/{year}{version}/degree_top')
    count = 0
    list_AS = []
    for line in ifile:
        if count < start:
            count += 1
            continue 
        if count >= end:
            break
        line_list = line.split(':')
        if line_list[-1] in ["Unknown\n"]:
            continue
        list_AS.append(line_list[0])
        count += 1
        
    str_R = ','.join(list_AS)
    print(str_R)



if __name__ == '__main__':
    # get_top_N_AS(2004)
    get_custom_range_N_AS(2004,start = 5000,end = 5010)
    get_custom_range_N_AS(2010,start = 5000,end = 5010)
    get_custom_range_N_AS(2020,start = 5000,end = 5010)