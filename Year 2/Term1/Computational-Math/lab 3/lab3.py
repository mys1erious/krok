import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative


def to_show(arr):
    for i in range(len(arr)):
        arr[i] = round(arr[i], 2)
    arr = '\n'.join(map(str, arr))
    return arr


def f(x):
    return x**5 - 4*x**3 + (1.5*x) / (1+x**2)


x = np.arange(-3, 3.1, 0.4)
y = [f(i) for i in x]
F1 = [derivative(f, i) for i in x]
F2 = [derivative(f, i, n=2) for i in x]

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('f(x) = x**5 - 4*x**3 + (1.5*x) / (1+x**2)')
ax1.plot(x, y)
ax1.axis([-3, 3, -5, 10])

ax2.axis([0, 1.3, 0, 1])
ax2.tick_params(labelbottom=False, labelleft=False)
ax2.text(0.1, 0.2, f'x\n{to_show(x)}')
ax2.text(0.4, 0.2, f'F\n{to_show(y)}')
ax2.text(0.7, 0.2, f'F`\n{to_show(F1)}')
ax2.text(1, 0.2, f'F``\n{to_show(F2)}')

plt.show()