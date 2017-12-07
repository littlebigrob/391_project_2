import matplotlib.pyplot as mat_plt
import csv
import numpy as np


# returns two sets of data one which contains teh petal length and width for versicolor and one for virginica
def get_data(file):
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        data_virginica = list()
        data_versicolor = list()
        for row in reader:
            if row[4] == 'versicolor':
                data_versicolor.append((float(row[2]), float(row[3])))
            elif row[4] == 'virginica':
                data_virginica.append((float(row[2]), float(row[3])))
    return data_versicolor, data_virginica


# this takes the data and splits it into petal length and petal width
def split_data(data):
    petal_length = list()
    petal_width = list()
    for row in data:
        petal_length.append(row[0])
        petal_width.append(row[1])
    return petal_length, petal_width


# this takes a m and a b and plots it over the scatter plot
def plot_line(m, b):
    x = np.arange(3, 7.0, 0.1)
    mat_plt.plot(x, ((m * x) + b), 'black')
    return


# this plots all of the points with a boundary line
def plot_points_and_decision_boundary(x1, y1, x2, y2, boundary, figure_number):
    mat_plt.figure(figure_number)
    mat_plt.title("petal length v width for versicolor and virginica with " + boundary[2])
    plot_line(boundary[0], boundary[1])
    mat_plt.xlabel("Petal Length")
    mat_plt.ylabel("Petal Width")
    mat_plt.scatter(x1, y1, color="green")
    mat_plt.scatter(x2, y2, color="orange")


# this classifies whether or not a flower is above or below the line
def classifier(x, y, boundary_x, boundary_y):
    over = True
    line_y = float(x) * boundary_x + boundary_y
    if line_y > float(y):
        over = False
    return over


# returns the amount of flowers in the correct quadrant
def mean_square_error(data, boundary, pattern):
    petal_length, petal_width = split_data(data)
    number_of_points = 0
    sum_error = 0
    for (x, y) in zip(petal_length, petal_width):
        number_of_points = number_of_points + 1
        if pattern != classifier(x, y, boundary[0], boundary[1]):
            sum_error += 1
    total_error = sum_error / number_of_points
    return total_error


# this runs exercise 1
def exercise_1(data_versicolor, data_virginica):
    x1, y1 = split_data(data_versicolor)
    x2, y2 = split_data(data_virginica)
    decision_boundary_1 = dict()
    decision_boundary_1[0] = -.4
    decision_boundary_1[1] = 3.75
    decision_boundary_1[2] = "hand drawn line"
    plot_points_and_decision_boundary(x1, y1, x2, y2, decision_boundary_1, 1)
    print("the second versicolor plant is over the line = " +
          str(classifier(x1[3], y1[3], decision_boundary_1[0], decision_boundary_1[1])))
    print("the first virginica plant is over the line = " +
          str(classifier(x2[0], y2[0], decision_boundary_1[0], decision_boundary_1[1])))


# runs exercise 2
def exercise_2(data_versicolor, data_virginica):
    x1, y1 = split_data(data_versicolor)
    x2, y2 = split_data(data_virginica)
    decision_boundary_1_x = -.41
    decision_boundary_1_y = 3.75
    decision_boundary_1 = dict()
    decision_boundary_1[0] = decision_boundary_1_x
    decision_boundary_1[1] = decision_boundary_1_y
    decision_boundary_1[2] = "first boundary"
    decision_boundary_2_x = -.1
    decision_boundary_2_y = 1.0
    decision_boundary_2 = dict()
    decision_boundary_2[0] = decision_boundary_2_x
    decision_boundary_2[1] = decision_boundary_2_y
    decision_boundary_2[2] = "second boundary"
    print("MSE for boundary 1: " +
          str((mean_square_error(data_versicolor, decision_boundary_1, False) +
               mean_square_error(data_virginica, decision_boundary_1, True)) / 2))
    print("MSE for boundary 2: " +
          str((mean_square_error(data_versicolor, decision_boundary_2, False) +
               mean_square_error(data_virginica, decision_boundary_2, True)) / 2))
    plot_points_and_decision_boundary(x1, y1, x2, y2, decision_boundary_1, 2)
    plot_points_and_decision_boundary(x1, y1, x2, y2, decision_boundary_2, 3)


if __name__ == "__main__":
    data_versicolor, data_virginica = get_data('..\data\irisdata.csv')
    exercise_1(data_versicolor, data_virginica)
    exercise_2(data_versicolor, data_virginica)

    mat_plt.show()
