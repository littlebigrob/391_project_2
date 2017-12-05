import matplotlib.pyplot as mat_plt
import csv

import numpy as np


def get_data(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        data_versicolor = []
        data_virginica = []
        for row in reader:
            if row[4] == 'versicolor':
                data_versicolor.append((row[2], row[3]))
            elif row[4] == 'virginica':
                data_virginica.append((row[2], row[3]))
    return data_versicolor, data_virginica


def split_data(data):
    petal_length = list()
    petal_width = list()
    for row in data:
        petal_length.append(row[0])
        petal_width.append(row[1])
    return petal_length, petal_width


def plot_line(m, b):
    x = np.arange(3.0, 7.0, 0.1)
    mat_plt.plot(x, ((m * x) + b), 'black')
    return


def plot_for_part_one():
    mat_plt.title("petal length v width for versicolor and virginica")
    data_versicolor, data_virginica = get_data('..\data\irisdata.csv')
    x1, y1 = split_data(data_versicolor)
    x2, y2 = split_data(data_virginica)
    #plot_line(1, 2)
    mat_plt.scatter(x2, y2)
    mat_plt.scatter(x1, y1)
    mat_plt.show()

mat_plt.title("petal length v width for versicolor and virginica")
data_versicolor, data_virginica = get_data('..\data\irisdata.csv')
x1, y1 = split_data(data_versicolor)
x2, y2 = split_data(data_virginica)
#plot_line(1, 2)
mat_plt.scatter(x2, y2)
mat_plt.scatter(x1, y1)
mat_plt.show()
