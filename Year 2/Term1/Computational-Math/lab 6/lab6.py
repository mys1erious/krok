from scipy.misc import derivative


def f(x):
    return x**5 - 4*x**3 + (1.5*x) / (1+x**2)


def newton_raphson(x_0, e):
    x = x_0
    for i in range(1, 1000):
        f_x = f(x)
        f_der_x = derivative(f, x)
        d = -f_x/f_der_x
        x = x+d
        print(f'i: {i}    x: {x:.8f}    d: {d:.8f}')
        if not abs(d) < e:
            continue
        else:
            print(x)
            return x


def secant(x_0, x_1, e):
    f_x = f(x_0)
    d = x_1 - x_0
    x = x_1
    for i in range(1, 1000):
        f_prev = f_x
        f_x = f(x)
        d = (f_x / (f_prev-f_x))*d
        x += d
        print(f'i: {i}    x: {x:.8f}    d: {d:.8f}')
        if not abs(d) < e:
            continue
        else:
            print(x)
            return x


x_0 = 1
x_1 = 3
e = 1e-4
print('Newton Raphnson method:')
n_r = newton_raphson(x_0, e)
print('\nSecant method:')
sec = secant(x_0, x_1, e)

print('Newton Raphnson result:', n_r)
print('Secant result:', sec)
