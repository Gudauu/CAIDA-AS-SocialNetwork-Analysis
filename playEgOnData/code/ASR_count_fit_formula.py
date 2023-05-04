from include import readList
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Define the exponential function
def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

def calc_exponential_draw_pic(version:"0101"):
    list_edge_size = []

    for year in range(2000,2023+1):
        ifile_name = f'playEgOnData/results/{year}0101/basic'
        with open(ifile_name,'r') as ifile:
            ilines = ifile.readlines()
            node_size = int(ilines[0][:-1].split(': ')[1])
            edge_size = int(ilines[1][:-1].split(': ')[1])
            list_edge_size.append(edge_size)
    data = np.array(list_edge_size)
    # Define the x-axis values
    x_values = np.arange(len(data))
    # year_values is what's gonna show on pic
    year_values = np.arange(2000,2000 + len(data))

    outfile_name = f'playEgOnData/results/2000-2023/exponential_fit_ASR_count.png'
    ofile_fit_data = open('report/R/basic/ASR_exponential_pred','w')

    # Fit the exponential function to the data
    popt, pcov = curve_fit(exponential_func, x_values[:-3], data[:-3])
    y_pred = exponential_func(x_values, *popt)

    ofile_fit_data.write(",".join([str(int(y)) for y in list(y_pred)]))
    ofile_fit_data.close()


    # Print the fitted parameters
    # print(popt)

    # Plot the data and the fitted function
    plt.plot(year_values, data, 'bo', label='data')
    plt.plot(year_values, y_pred, 'r-', label='fit')

    # Annotate the equation on the plot
    equation = f'y = {popt[0]:.2f} * exp({-1*popt[1]:.2f} * x) + ({popt[2]:.2f})'
    # Calculate and print the R-squared value
    r2 = r2_score(data, y_pred)
    # print(f"R-squared: {r2:.4f}")
    annotation_R_square = f'R-square: {r2}'
    plt.annotate(equation, xy=(0.05, 0.7), xycoords='axes fraction',fontsize=11)
    plt.annotate(annotation_R_square, xy=(0.05, 0.6), xycoords='axes fraction',fontsize=10)

    # Add legend and axis labels
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('ASR count')

    # Save the figure
    plt.savefig(outfile_name)
    plt.clf()

    # Show the plot
    # plt.show()

if __name__ == '__main__':
    calc_exponential_draw_pic(version = "0101")



