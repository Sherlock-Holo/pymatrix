#!/usr/bin/env python3

import numpy
import sys

def gen_matrix():
    matrix = []

    line = int(input('Please tell me how many lines in the matrix: '))

    for n in range(line):
        l = input('The {} line: '.format(n + 1))
        matrix_line = l.split()
        matrix_line = list(map(int, matrix_line))
        matrix.append(matrix_line)

    return matrix

matrix = gen_matrix()
matrix = numpy.mat(matrix)

if int(numpy.linalg.det(matrix)) == 0:
    print("The matrix can't calculate the inv matrix")
    sys.exit(1)

else:
    imatrix = matrix.I

    for n in imatrix:
        print(n)
