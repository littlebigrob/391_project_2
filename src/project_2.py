import matplotlib.pyplot as mat_plt
import csv

import numpy as np


def get_data():
    with open('irisdata.csv') as csvfile:
        reader = csv.reader(csvfile)
        data_versicolor = []
        data_virginica = []
        for row in reader:
            if row[4] == 'versicolor':
                data_versicolor.append(row[2:3])
            elif row[4] == 'virginica':
                data_virginica.append(row[2:3])
    return data_versicolor, data_virginica


def split_data(data):
    petal_length = list()
    petal_width = list()
    for row in data:
        petal_length.append(row[1])
        petal_width.append(row[2])
    return petal_length, petal_width


def plot_line(m, b):
    x = np.arange(3.0, 7.0, 0.1)
    mat_plt.plot(x, ((m * x) + b), 'black')
    return


def plot_for_part_one():
    mat_plt.figure(1)
    mat_plt.title("petal length v width for versicolor and virginica")
    data_versicolor, data_virginica = get_data()
    x1, y1 = split_data(data_versicolor)
    x2, y2 = split_data(data_virginica)
    mat_plt.plot(x1, y1)
    mat_plt.plot(x2, y2, 'y')
    #plot_line(1, 2)
    mat_plt.show()


plot_for_part_one()
