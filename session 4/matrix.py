import numpy as np
import time
def input_matrix():
    """take a matrix from user"""
    rows = int(input("please enter number of rows: "))
    cols =int(input("please enter number of cols: "))
    mat = []
    sq = False
    if rows == cols:
        sq = True
    for i in range(0, rows):
        mat.append([])
        for j in range(0, cols):
            element = input("Enter the element: "+str(i)+str(j)+"\n")
            mat[i].append(element)
    mat=np.matrix(mat,dtype='float')
    print("your matrix"+str(mat))
    return mat,sq
def calculation():
    """ask user about what he/she wants to calculate"""
    matrix, sq_status = input_matrix()
    print("What do you need to do?\n1-Transpose\n2-Inverse\n3-diagonals\n4-determinant\n5-Exit")
    respond = input()
    if respond == '1':
        print("your matrix: " + str(matrix))
        print("Transpose: " + str(matrix.T))
        time.sleep(5)
    elif respond == '2':
        if sq_status == False:
            print("your matrix is not square"+str(matrix))
            time.sleep(1)
        elif np.linalg.det(matrix)==0:
            print("your matrix is not invertable")
        else:
            print("your matrix: " + str(matrix))
            print("Inverse: " + str(matrix.I))
            time.sleep(5)
    elif respond=="3":
        print("your matrix: " + str(matrix))
        print("main diagonal: "+str(matrix.diagonal()))
        print("second diagonal: " + str(np.diag(np.fliplr(matrix))))
        time.sleep(5)
    elif respond=="4":
        print("your matrix: " + str(matrix))
        print("determinant: "+str(np.linalg.det(matrix)))
        time.sleep(5)
    elif respond=="5":
        exit()
    else:
        print("please enter the correct number")
        time.sleep(2)
        calculation()

while True:
    calculation()
