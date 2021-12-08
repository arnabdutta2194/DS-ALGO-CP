import numpy as np
def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1

        for i in range(first,last):
            #Store Top
            top = matrix[layer][i]
            # Rotate Left
            matrix[layer][i] = matrix[-i-1][layer]
            #Rotate Bottom
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            #Rotate Right
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            #Store Top
            matrix[i][-layer-1] = top
    return matrix


matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(rotateMatrix(matrix))