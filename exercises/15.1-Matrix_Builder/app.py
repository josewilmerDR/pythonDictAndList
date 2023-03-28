#Import random
import random

#Create the function below:
def matrixBuilder(num):
    raws = []
    matrix = []
    for j in range(num):
        raws.append(1) 
        matrix.append(raws)
    return matrix

print(matrixBuilder(3))

