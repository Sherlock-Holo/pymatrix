def gen_matrix():
    matrix = []

    line = int(input('Please tell me how many lines in the matrix: '))

    for n in range(line):
        l = input('The {} line: '.format(n + 1))
        matrix_line = l.split()
        matrix_line = list(map(int, matrix_line))
        matrix.append(matrix_line)

    return matrix, line

if __name__ == '__main__':
    matrix, line = gen_matrix()
