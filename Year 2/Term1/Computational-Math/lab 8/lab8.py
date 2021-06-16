import math
import matplotlib.pyplot as plt


def f(x):
    return x**5 - 4*x**3 + (1.5*x) / (1+x**2)


def golden_section(a, b, e=10e-4):
    f_a = f(a)
    f_b = f(b)
    r = (math.sqrt(5) - 1) / 2
    c = a + (1-r) * (b-a)
    f_c = f(c)
    d = b - (1-r) * (b-a)
    f_d = f(d)
    i = 0
    lst_e = []
    while True:
        lst_e.append(abs(b - a))
        i+=1
        if f_a == f_c == f_d or f_c == f_d == f_b:
            break
        elif f_c > f_d:
            a = c
            f_a = f_c
            c = d
            f_c = f_d
            d = b - (1-r) * (b-a)
            f_d = f(d)
        else:
            b = d
            f_b = f(d)
            d = c
            f_d = f(c)
            c = a + (1-r) * (b-a)
            f_c = f(c)
        print(f'i: {i}\n    a: {a:.8f}    c: {c:.8f}    d: {d:.8f}    b: {b:.8f}    |b-a|: {abs(b - a):.8f}    '
              f'f(a): {f_a:.8f}    f(c): {f_c:.8f}    f(d): {f_d:.8f}    f(b): {f_b:.8f}')
        if not abs(b-a) < e:
            continue
        else:
            x = c
            print(f'x: {x}')
            return x, lst_e


test = golden_section(0.5, 2)
plt.plot(test[1])
plt.yscale('log')
plt.show()