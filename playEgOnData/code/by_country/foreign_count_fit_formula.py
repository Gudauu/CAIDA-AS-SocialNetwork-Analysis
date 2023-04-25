from include import readList
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Define the exponential function
def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# calculate the exponential fit formula of foreign ASR counts during range, and generate plot the pic
# right now I'm only using the "0101" month data and counted domestic foreign for 2001-2023.
# strip: how many should be removed from calc at the last
# note that data points stripped will still appear in the pic, just won't join the calculation
def calc_exponential_draw_pic(country:str,year_start:int=2001, year_end:int=2023,strip:int = 0):
    ifile_name = f'playEgOnData/results/by_country/{country}/count_domestic_extern_across_{year_start}_{year_end}'
    with open(ifile_name,'r') as ifile:
        ilines = ifile.readlines()
        foreign_data = (ilines[1][:-1].split(','))
    foreign_data = [int(x) for x in foreign_data]
    data = np.array(foreign_data)
    # Define the x-axis values
    x_values = np.arange(len(data)-strip)  # strip the last ones
    # year_values is what's gonna show on pic
    year_values = np.arange(year_start,year_start + len(data))

    if strip <= 0:  # won't strip
        outfile_name = f'playEgOnData/results/by_country/{country}/exponential_fit_foreign_ASR_count_{year_start}_{year_end}.png'
        strip = -1*(year_end - year_start + 1)
    else:  # strip some nodes
        outfile_name = f'playEgOnData/results/by_country/{country}/exponential_fit_foreign_ASR_count_{year_start}_{year_end}_strip_{strip}.png'

    # Fit the exponential function to the data
    popt, pcov = curve_fit(exponential_func, x_values, data[:-1*strip])
    y_pred = exponential_func(x_values, *popt)


    # Print the fitted parameters
    # print(popt)

    # Plot the data and the fitted function
    plt.plot(year_values, data, 'bo', label='data')
    plt.plot(year_values[:-1*strip], y_pred, 'r-', label='fit')

    # Annotate the equation on the plot
    equation = f'y = {popt[0]:.2f} * exp({-1*popt[1]:.2f} * x) + ({popt[2]:.2f})'
    # Calculate and print the R-squared value
    r2 = r2_score(data[:-1*strip], y_pred)
    # print(f"R-squared: {r2:.4f}")
    annotation_R_square = f'R-square: {r2}'
    plt.annotate(equation, xy=(0.05, 0.7), xycoords='axes fraction',fontsize=11)
    plt.annotate(annotation_R_square, xy=(0.05, 0.6), xycoords='axes fraction',fontsize=10)

    # Add legend and axis labels
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('foreign ASR count')

    # Save the figure
    plt.savefig(outfile_name)
    plt.clf()

    # Show the plot
    # plt.show()

if __name__ == '__main__':
    list_country = readList('dataCAIDA/ASN_lookup/filterd_3_neighbor_country_list') 
    # check_top_neighbor_not_self_across_year(list_country,2001,2023)
    # calc_ratio_top_second_across_year(list_country,2001,2023)
    failed_cc = []
    for cc in list_country:
        try:
            calc_exponential_draw_pic(cc,strip = 0)
        except RuntimeError:
            print(f"Failed to fit curve for country: {cc}")
            failed_cc.append(cc)
    print("Failed countries: ", failed_cc) # ['BG', 'BR', 'ZA', 'UA', 'PL', 'ZZ', 'FI', 'CA', 'JP']


    
######## old code
# Load your data
# data = np.array([37, 64, 63, 76, 95, 107, 150, 199, 214, 190, 233, 253, 309, 350, 435, 693, 754]) #, 1341, 1594, 1679, 1748, 1568
# data = np.array([127, 191, 209, 119, 158, 213, 382, 629, 401, 679, 1352, 1730, 1850, 2242, 2661, 4145, 6253, 6480, 7339, 9330, 10077, 12084, 15767]) 
# data = np.array([3281, 4658, 5632, 6396, 8038, 9312, 10570, 12886, 14131, 15543, 15736, 18639, 20761, 24427, 25825, 32398, 34557, 37617, 42797, 51961, 52327, 58053, 62884]) 
# data = np.array([282, 358, 433, 393, 541, 653, 675, 781, 974, 1020, 1246, 1524, 1663, 2009, 2089, 2581, 2640, 2688, 3323]) # , 1853, 2067, 2318, 2974 
# data = np.array([252, 349, 831, 1382, 2264, 2915, 3282, 4472, 5308, 5428, 4945, 7476, 8904, 10265, 11634, 13235, 14743, 15774, 23378, 25218, 28359, 31507]) 
# data = np.array([]) 


