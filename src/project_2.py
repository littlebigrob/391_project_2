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
def plot_line(m, b, color='black', label=None):
    x = np.arange(3, 7.0, 0.1)
    mat_plt.plot(x, ((m * x) + b), color=color, label=label)
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
def mean_square_error(data_1, data_2, boundary):
    petal_length_versicolor, petal_width_versicolor = split_data(data_1)
    petal_length_virginica, petal_width_virginica = split_data(data_2)
    number_of_points = 0
    sum_error = 0
    for (x, y) in zip(petal_length_versicolor, petal_width_versicolor):
        number_of_points = number_of_points + 1
        difference = ((float(boundary[0]) * float(x)) + float(boundary[1])) - float(y)
        sum_error = sum_error + np.math.pow(difference, 2)
    for (x, y) in zip(petal_length_virginica, petal_width_virginica):
        number_of_points = number_of_points + 1
        difference = ((float(boundary[0]) * float(x)) + float(boundary[1])) - float(y)
        sum_error = sum_error + np.math.pow(difference, 2)
    total_error = sum_error / number_of_points
    return total_error

# this takes the data and the boundary line and finds the new gradient for it
def gradient(data_1, data_2, boundary):
    points = 0
    gradient_m = 0
    gradient_b = 0
    petal_length_versicolor, petal_width_versicolor = split_data(data_1)
    petal_length_virginica, petal_width_virginica = split_data(data_2)
    for (x, y) in zip(petal_length_versicolor, petal_width_versicolor):
        points = points + 1
        gradient_b += (float(boundary[0]) * float(x) + boundary[1] - float(y))
        gradient_m += (float(boundary[0]) * float(x) + boundary[1] - float(y)) * float(x)
    for (x, y) in zip(petal_length_virginica, petal_width_virginica):
        points = points + 1
        gradient_b += (float(boundary[0]) * float(x) + boundary[1] - float(y))
        gradient_m += (float(boundary[0]) * float(x) + boundary[1] - float(y)) * float(x)
    m = boundary[0] - (gradient_m * 2) / points * 0.1 / points
    b = boundary[1] - (gradient_b * 2) / points * 0.1 / points
    return m, b


# starts at a decision boundary line and keeps on moving until minimal change in the gradient
def descent(data_1, data_2, boundary):
    previous_error = np.math.inf
    calculated_error = mean_square_error(data_1, data_2, boundary)
    m = boundary[0]
    b = boundary[1]
    iteration = 1
    line_m = [m]
    line_b = [b]
    while previous_error - calculated_error > 0.00001:
        m, b = gradient(data_1, data_2, (m, b))
        iteration = iteration + 1
        previous_error = calculated_error
        calculated_error = mean_square_error(data_1, data_2, (m, b))
        line_m.append(m)
        line_b.append(b)
    mat_plt.figure(4)
    mat_plt.xlabel("Petal Length")
    mat_plt.ylabel("Petal Width")
    petal_length_versicolor, petal_width_versicolor = split_data(data_1)
    petal_length_virginica, petal_width_virginica = split_data(data_2)
    mat_plt.scatter(petal_length_versicolor, petal_width_versicolor, color="green")
    mat_plt.scatter(petal_length_virginica, petal_width_virginica, color="orange")
    mat_plt.title("change in gradient")
    plot_line(boundary[0], boundary[1], "red", "first line, MSE = " +
              str(mean_square_error(data_1, data_2, (boundary[0], boundary[1]))))
    plot_line(line_m[int((iteration-1) / 2)], line_b[int((iteration-1) / 2)], "purple", "mid point line, MSE = " +
              str(mean_square_error(data_1, data_2, (line_m[int((iteration-1) / 2)], line_b[int((iteration-1) / 2)]))))
    plot_line(line_m[int(iteration-1)], line_b[int(iteration-1)], "blue",  "final line, MSE = " +
              str(mean_square_error(data_1, data_2, (line_m[int((iteration-1))], line_b[int((iteration-1))]))))
    mat_plt.legend()

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
    decision_boundary_1 = dict()
    decision_boundary_1[0] = -.41
    decision_boundary_1[1] = 3.75
    decision_boundary_1[2] = "first boundary"
    decision_boundary_2 = dict()
    decision_boundary_2[0] = -.1
    decision_boundary_2[1] = 2.0
    decision_boundary_2[2] = "second boundary"
    decision_boundary_3 = dict()
    decision_boundary_3[0] = -.5*np.random.random()
    decision_boundary_3[1] = 2.0+3.0*np.random.random()
    print("MSE for boundary 1: " + str(mean_square_error(data_versicolor, data_virginica, decision_boundary_1)))
    print("MSE for boundary 2: " + str(mean_square_error(data_versicolor, data_virginica, decision_boundary_2)))
    plot_points_and_decision_boundary(x1, y1, x2, y2, decision_boundary_1, 2)
    plot_points_and_decision_boundary(x1, y1, x2, y2, decision_boundary_2, 3)
    descent(data_versicolor, data_virginica, decision_boundary_3)


if __name__ == "__main__":
    data_versicolor, data_virginica = get_data('..\data\irisdata.csv')
    exercise_1(data_versicolor, data_virginica)
    exercise_2(data_versicolor, data_virginica)

    mat_plt.show()
