'''

@author ysbecca Rebecca Stone

Functions which display graphs using matplotlib.pyplot (http://matplotlib.org/api/pyplot_api.html)

'''

import matplotlib.pyplot as plt



def plot_with_legend(x_range, y_data, legend_labels, x_label, y_label):
    ''' Displays a single plot with multiple datasets and matching legends.
        x_range should be one single array of indices for the x axis, and y_data can 
    '''
    if(len(y_data) != len(legend_labels)):
        print("Error: the number of data sets does not match the number of labels provided.")
        return
    all_plots = []
    for i, data in enumerate(y_data):
        temp, = plt.plot(x_range, data, label=legend_labels[i])
        all_plots.append(temp)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(handles=all_plots)
    plt.show()