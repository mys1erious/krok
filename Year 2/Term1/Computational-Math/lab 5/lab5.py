import math


def f(x):
    return x**5 - 4*x**3 + (1.5*x) / (1+x**2)


def g(x):
    return (4*x**3 - (1.5*x) / (1+x**2)) ** (1/5)


def simple_iteration(x_0, e):
    x = x_0
    for i in range(1, 1000):
        x_prev = x
        x=g(x)
        d=x-x_prev
        print(f'i: {i}    x: {x:.8f}    d: {d:.8f}')
        if not abs(d) < e:
            continue
        else:
            print(x)
            return x


x_0 = 1
e = 1e-4

s_i = simple_iteration(x_0, e)
print('Simple iteration result:', s_i)