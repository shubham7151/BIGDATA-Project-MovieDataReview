import matplotlib.pyplot as plt
from numpy import save

def createStemPlot(xplot,yplot,xlabel,ylabel,title,savePath):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.stem(xplot,yplot)
    plt.savefig(savePath)
    plt.show()

def createScatterPlot(xplot,yplot,xlabel,ylabel,title,savePath):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(xplot,yplot)
    plt.savefig(savePath)
    plt.show()

def createaxis(key,data):
    temp_data = data[key]
    xplot=[]
    yplot=[]
    for value in temp_data:
        if not (value[0]is None):
            xplot.append(value[0])
            yplot.append(value[1])
    return (xplot,yplot)