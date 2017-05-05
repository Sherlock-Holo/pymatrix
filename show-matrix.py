import re

matrix = []

line = int(input('Please tell me how many lines in the matrix: '))

for n in range(line):
    l = input('The {} line: '.format(n + 1))
    matrix_line = re.split(r'[,\s ]\s*', l)
    matrix_line = list(map(int, matrix_line))
    matrix.append(matrix_line)

for n in matrix:
    print(n)
