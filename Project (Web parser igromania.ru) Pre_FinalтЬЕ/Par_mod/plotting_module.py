import matplotlib.pyplot as plt


# plotting plot with format (line, box, histogram, area, pie, bar)
# data_ser - data series for plotting
# path - path for saving plot
def plotting_plot(data_ser, path, kind='line', title=None, x_lab=None, y_lab=None):
    try:
        data_ser.plot(kind=kind)
        plt.xlabel(x_lab)
        plt.ylabel(y_lab)
        plt.suptitle(title)
        plt.savefig(path)
    except Exception:
        print('Choose another kind of plot')

