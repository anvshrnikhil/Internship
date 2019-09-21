


import math
import matplotlib.pyplot as plt

def bargraph(x, y):

    plt.bar(x, y, width = 0.5 , color ='c')
    plt.show()


def ploting(x, y):
    plt.plot(x, y)
    plt.show()



x_axis = [x for x in range(-300, 300, 1)]
x_axis = list(map(lambda x : x / 100, x_axis))
y_axis = list(map(lambda x : math.cos(x), x_axis))
ploting(x_axis, y_axis)