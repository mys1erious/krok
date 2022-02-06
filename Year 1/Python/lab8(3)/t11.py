import numpy as np

def matrix_creator(string, column):
    arr = np.zeros((string, column))
    for i in range(string):
        for j in range(column):
            arr[i, j] = int(input(f"elem[{i},{j}]: "))
    return arr

# № 1. Rotate array 90 deg
'''
string = int(input("String: "))
column = int(input("Column: "))
if string == column:
    arr1 = matrix_creator(string, column)
    rotated = np.rot90(arr1,k=3)
    print('Rotated matrix: \n', rotated)
else:
    print('Array isnt square')
'''

# № 2. Move array elems on (2) to the left
'''
k = int(input('Move left: '))
arr1 = np.arange(10)
arr2 = arr1[k:]
print(arr2)
'''

# № 3. Multiply 2 matrix
'''
string1 = int(input("String mat1: "))
column1 = int(input("Column mat1: "))
arr1 = matrix_creator(string1, column1)
print(arr1)

string2 = int(input("String mat2: "))
column2 = int(input("Column mat2: "))
arr2 = matrix_creator(string2, column2)
print(arr2)

if column1 == string2 and column2 == string1:
    arrProduct = np.dot(arr1, arr2)
    print("Product of matrices: \n", arrProduct)
else:
    print("Matrix isnt square")
'''

# № 4. Det of matrix
'''
string = int(input("String: "))
column = int(input("Column: "))

if string == column:
    arr1 = np.zeros((string, column))
    
    for i in range(string):
        for j in range(column):
            arr1[i,j] = int(input(f"elem[{i},{j}]: "))
            
    det = np.linalg.det(arr1)
    print(int(det))
else:
    print("Entered matrix isnt square, det can be found only in square matrix")
'''