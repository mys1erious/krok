import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x - y - 4*x*y**2 * np.sqrt(x**2 + y**2)


def df(x, y):
    return (np.sqrt(x**2 + y**2) - 8*y**2*x**2 - 4*y**4) / np.sqrt(x**2 + y**2)


def ddf(x, y):
    return -((8*y**2*x**3 + 12*y**4*x) / (x**2 + y**2)**1.5)


def bisection(a, b, y0=0, e=1e-4):
    y = y0
    xs = []
    ys = []
    if np.sign(f(a, y)) == np.sign(f(b, y)):
        raise ValueError('f(a) and f(b) must have different signs')
    f_a = f(a, y)
    for i in range(1, 1000):
        y += abs(b-a)
        x = a + (b - a)/2
        f_x = f(x, y)
        xs.append(x)
        ys.append(y)
        if np.sign(f_a) == np.sign(f_x):
            a = x
        else:
            b = x
        if abs(b-a) > e:
            continue
        else:
            x = a + (b-a)/2
            return x, xs, ys


bis, xs, ys = bisection(0, 5)

x = np.arange(0, 5, 0.1)
X, Y = np.meshgrid(x, x)
F = Y**X
G = X**Y
plt.contour(X, Y, (F - G), [0])
plt.show()

_df = [df(xs[i], ys[i]) for i in range(len(ys))]
_ddf = [ddf(xs[i], ys[i]) for i in range(len(ys))]

for i in range(len(ys)):
    print(f'f: {ys[i]:.4f}  f`: {_df[i]:.4f}  f``: {_ddf[i]:.4f}')