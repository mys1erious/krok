import numpy as np


def F(s):
    if s >= 0: return 1
    else: return 0


# Creating russian letters 'Н' and 'Г' as arrays of 0`s and 1`s
rus_letter_n = np.array([[1, 0, 1],
                         [1, 1, 1],
                         [1, 0, 1]])

rus_letter_g = np.array([[1, 1, 1],
                         [1, 0, 0],
                         [1, 0, 0]])


# Changing letters form to a vector and add them to an input variable X
X = np.array([rus_letter_n.flatten(), rus_letter_g.flatten()])


