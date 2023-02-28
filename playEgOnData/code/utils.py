

def create_directories():
    import os

    # Define the start and end years
    start_year = 2000
    end_year = 2022

    # Loop over the years and create directories
    for year in range(start_year, end_year+1):
        dirname = "playEgOnData/results/"+str(year) + "0101"
        os.makedirs(dirname)


if __name__ == '__main__':
    create_directories()