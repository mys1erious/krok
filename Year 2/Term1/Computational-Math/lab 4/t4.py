
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative


def to_show(arr):
    for i in range(len(arr)):
        arr[i] = round(arr[i], 2)
    arr = '\n'.join(map(str, arr))
    return arr


def f(x):
    #return 2*x**3-2*x-5
    return x**5 - 4*x**3 + (1.5*x) / (1+x**2)


def bisection(a, b, e=1e-8):
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError('f(a) and f(b) must have different signs')
    lst_e = []
    f_a = f(a)
    for i in range(1, 1000):
        lst_e.append(abs(b-a))
        x = a + (b - a)/2
        f_x = f(x)
        print(f'i: {i}    a: {a:.8f}    b: {b:.8f}    |b-a|: {abs(b-a):.8f}    f(x): {f_x:.8f}')
        if np.sign(f_a) == np.sign(f_x):
            a = x
        else:
            b = x
        if abs(b-a) > e:
            continue
        else:
            x = a + (b-a)/2
            print(f'x: {x:.8f}')
            return x, lst_e


def chord(a, b, e=1e-8):
    lst_e = []
    f_a = f(a)
    f_b = f(b)
    x = a
    for i in range(1, 1000):
        lst_e.append(abs(b - a))
        x_prev = x
        x = a - f(a)*((b-a) / (f(b) - f(a)))
        f_x = f(x)
        print(f'i: {i}    a: {a:.8f}    b: {b:.8f}    |b-a|: {abs(b - a):.8f}    f(x): {f_x:.8f}'
              f'    |x_prev - x|: {abs(x_prev - x)}')
        if np.sign(f_a) == np.sign(f_x):
            a = x
            f_a = f_x
        else:
            b = x
            f_b = f_x
        if not abs(x_prev-x) < e:
            continue
        else:
            print(f'x: {x:.8f}')
            return x, lst_e


# Lab 3 code
x = np.arange(-3, 3.1, 0.4)
y = [f(i) for i in x]
F1 = [derivative(f, i) for i in x]
F2 = [derivative(f, i, n=2) for i in x]

fig, (graph, info) = plt.subplots(1, 2)
fig.suptitle('f(x) = x**5 - 4*x**3 + (1.5*x) / (1+x**2)')
graph.plot(x, y)
graph.axis([-3, 3, -5, 10])

info.axis([0, 1.3, 0, 1])
info.tick_params(labelbottom=False, labelleft=False)
info.text(0.1, 0.2, f'x\n{to_show(x)}')
info.text(0.4, 0.2, f'F\n{to_show(y)}')
info.text(0.7, 0.2, f'F`\n{to_show(F1)}')
info.text(1, 0.2, f'F``\n{to_show(F2)}')

plt.show()


# Lab 4 code
a = 1
b = 3
e = 1e-4
bis = bisection(a, b, e)
_chord = chord(a, b, e)
print(f'Bisection method x: {bis[0]}\nChord method x: {_chord[0]}')

# Lg graph
fig2, (lgbis, lgchord) = plt.subplots(1, 2)
lgbis.plot(bis[1])
lgbis.set_title('Bisection lg')
lgbis.set_yscale('log')

lgchord.plot(_chord[1])
lgchord.set_title('Chord lg')
lgchord.set_yscale('log')

plt.show()