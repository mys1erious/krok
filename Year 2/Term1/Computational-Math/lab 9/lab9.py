import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return x**5 - 4*x**3 + (1.5*x) / (1+x**2)


def piecewise_lin_interp(a, b, n=6):
    h = (b-a) / n
    x = []
    y = []
    p = []
    for i in range(n+1):
        x.append(a + h * i)
        y.append(func(x[i]))
    for i in range(1, n+1):
        p.append(y[i-1]*(1-x[i])+y[i]*x[i])
    x.pop()
    return x, p


x = np.arange(-2, 2, 0.1)
y = [func(i) for i in x]

pli_x, pli_p = piecewise_lin_interp(-2, 2)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y)
ax1.set_title('f(x)')
ax1.axis([-3, 3, -5, 8])

ax2.plot(pli_x, pli_p)
ax2.set_title('Piecewise lin int')
ax2.axis([-3, 3, -8, 10])

plt.show()