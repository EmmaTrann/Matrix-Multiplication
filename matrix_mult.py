

import numpy as np
def matrixmultiply(a, b, result):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result 
import time
def main():
    print("Please enter same number for ")
    row_a = int(input("Enter the number of rows in matrix A: "))
    col = int(input("Enter the number of columns in matrix A: "))
    col_b = int(input("Enter the number of columns in matrix B: "))

    a = np.random.randint(10, size=(row_a,col))
    b = np.random.randint(10, size=(col,col_b))
    result = np.zeros((row_a, col_b))
    start = time.time()
    result = matrixmultiply(a, b, result)
    end = time.time()
    computeTime= end-start
    
    print("\nThe compute time using non built-in is %.3f seconds." % computeTime)
    
    start = time.time()
    res = np.dot(a,b) 
    end = time.time()
    computeTime= end-start
    print("\nThe compute time using built-in is %.3f seconds." % computeTime)
    if (result==res).all():
        print("\nThe matrix product got from non built-in routine is the same as the result we use numpy to calculate.")

    
main()
