#!/usr/bin/env python3

import sys
'''this is for get your content from terminal'''
'''use sys.argv better than argparse'''


def gen_matrix():
    '''this is turn you input content to a matrix'''
    matrix = []

    line = int(input('Please tell me how many lines in the matrix: '))

    for n in range(line):
        l = input('The {} line: '.format(n + 1))
        matrix_line = l.split()
        matrix_line = list(map(int, matrix_line))
        matrix.append(matrix_line)

    return matrix


'''use gen_matrix to return a matrix'''
from numpy import mat as num_mat
'''i think i can use lambda function to make the program simpler'''
from numpy import linalg as num_linalg
matrix = gen_matrix()
matrix = num_mat(matrix)

if int(num_linalg.det(matrix)) == 0:
    print("The matrix can't calculate the inv matrix")
    sys.exit(1)

else:
    imatrix = matrix.I

    for n in imatrix:
        print(n)
