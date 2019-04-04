import matplotlib.pyplot as plt
import numpy as np

N = 10
h = 0.01
t0 = 0
x0 = 273

nyu = 1.4
s = 0.02
l = 0.03
c = 4.18*1000
O = 273+20
m = 0.13 + 0.01


def f(xs, i):
    return -nyu*s*(xs[i] - O)/(l*c*m)


def diff(xs, i):
    return (f(xs, i) - f(xs, i-1)) / h


def resultf(xs, i):
    y = x0;
    for j in range(i, 1, -1):
        y += h*diff(xs, j)
    return y


def showPlot(xs, ys):
    plt.title("Lab 1.1");
    plt.plot(xs, ys);
    plt.show()


xs = []
ys = []

for x in np.arange(0, N, h):
    xs.append(x)

for i in range(0, len(xs)):
    ys.append(resultf(xs, i))

showPlot(xs, ys)