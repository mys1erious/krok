import time
import os
import psutil


def inf(type, string):
    print(type.__name__+':')


    start_time = time.time()
    ans = type(string)
    print("Execution time:", "%s seconds" % (time.time() - start_time))

    process = psutil.Process(os.getpid())
    print('Memory usage: ', process.memory_info().rss)
    return ans


def iterative_version(string):
    sign = ['+', '-', '*']
    formula = string.split()

    check = True
    for i in range(len(formula)):
        if i % 2 == 0 and formula[i].isdigit():
            pass
        elif i & 1 and formula[i] in sign:
            pass
        else:
            check = False
            print('Incorrect formula')
            return None

    if check:
        ans = ''.join(formula)
        return eval(ans)


def recursive_version(formula, i=0, ans=str()):
    sign = ['+', '-', '*']

    if i == len(formula):
        return eval(ans)
    elif i % 2 == 0 and formula[i].isdigit():
        return recursive_version(formula, i+1, ans+formula[i])
    elif i & 1 and formula[i] in sign:
        return recursive_version(formula, i+1, ans+formula[i])
    else:
        print('Incorrect formula')
        return None


formulaInput = input('Formula example: (num sign num)\n'
                     'Enter formula: ')


print(inf(iterative_version, formulaInput))
print(inf(recursive_version, formulaInput.split()))
