



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



if __name__ == '__main__':
    get_top_N_AS(2004)