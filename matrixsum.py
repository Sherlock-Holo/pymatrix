# gen all list
from itertools import permutations
from showmatrix import gen_matrix

def element(line):
    gen_all_list = permutations(list(range(1, line + 1)))
    all_list = []

    for x in gen_all_list:
        all_list.append(x)

    print(all_list)

if __name__ == '__main__':
    element(3)
