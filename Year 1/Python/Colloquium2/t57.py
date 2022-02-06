import numpy as np


def nearest(lst, target):
  return min(lst, key=lambda x: abs(x-target))


surname = np.array(['surn1', 'surn2', 'surn3', 'surn4', 'surn5'])
salary = np.array([  132,     204,     362,     310,     564])
salarySort = sorted(salary)

mean = np.mean(salary)
closest = min(salary, key=lambda x: abs(x-mean))
Min = min(salary)
minSalInd = np.where(salary == Min)[0]
salary = np.delete(salary, minSalInd)
surname = np.delete(surname, minSalInd)

print('Closest salary to average of all salaries: ', closest)
print('2 highest salaries: ', salarySort[-1], salarySort[-2])
print(f'Lists without surn with the least salary:\n{surname}\n{salary}')