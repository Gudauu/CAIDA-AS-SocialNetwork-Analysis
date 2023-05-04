

def calc_delta(iofile_name:str) -> None:
    iofile = open(iofile_name,'r+')
    list_new = []
    list_gone = []
    for line in iofile:
        if list_new == []:
            list_new = line[:-1].split(',')
        elif list_gone == []:
            list_gone = line[:-1].split(',')
    list_delta = []
    for i in range(len(list_new)):
        list_delta.append(str(int(list_new[i]) - int(list_gone[i])))
    iofile.write(",".join(list_delta))
    iofile.write("\n")


if __name__ == '__main__':
    calc_delta("playEgOnData/results/2000-2023/node_fluc")
    # calc_delta("playEgOnData/results/2000-2023/edge_fluc")
