import matplotlib.pyplot as mat_plt
import csv

import numpy as np


def get_data(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        data_virginica = list()
        data_versicolor = list()
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
    x = np.arange(0, 30.0, 0.1)
    mat_plt.plot(x, ((m * x) + b), 'black')
    return

def plot_scatter(x, y, color):
    mat_plt.scatter(x, y, color=color)

def pass_data_to_plotter():
    data_versicolor, data_virginica = get_data('..\data\irisdata.csv')
    x1, y1 = split_data(data_versicolor)
    x2, y2 = split_data(data_virginica)
    plot_for_part_one(x1, y1, x2, y2)

    print("the first versicolor plant is over the line = " + str(classifier(x1[0],y1[0])))
    print("the 10th virginica plant is over the line = " + str(classifier(x2[9],y2[9])))

def plot_for_part_one(x1, y1, x2, y2):
    mat_plt.title("petal length v width for versicolor and virginica")
    plot_line(-.35, 14)
    mat_plt.xlabel("Petal Length")
    mat_plt.ylabel("Petal Width")
    plot_scatter(x1 + x2, y1 + y2, "white")
    plot_scatter(x1, y1, "green")
    plot_scatter(x2, y2, "orange")

def classifier(x, y):
    over = False
    if float(x) *-0.285714286+3.25 <= float(y):
        over = True
    return over


if __name__ == "__main__":
    pass_data_to_plotter()
    mat_plt.show()