import numpy as np

def transpose(matrix):
    matrix = np.array(matrix)
    return (matrix.transpose()).tolist()

a = transpose([[1,2,3],[4,5,6],[7,8,9]])
print(a)