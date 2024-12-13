import sys
import re
import numpy as np


def main(file_name: str):
    confs_coefs = get_input(file_name)
    tot_tokens = 0
    tot_tokens2 = 0
    for a_coef, b_coef, pos in confs_coefs:
        A = np.array([a_coef, b_coef], dtype=int)
        A = np.transpose(A)
        x = np.linalg.solve(A, pos)
        x = np.round(x).astype(int)
        prod = np.matmul(A, x, dtype=int)
        pos2 = pos + np.array([10000000000000, 10000000000000])
        x2 = np.linalg.solve(A, pos2)
        x2 = np.round(x2).astype(int)
        prod2 = np.matmul(A, x2, dtype=int)
        if prod[0] == pos[0] and prod[1] == pos[1]:
            tot_tokens += x @ [3, 1]
        if prod2[0] == pos2[0] and prod2[1] == pos2[1]:
            tot_tokens2 += x2 @ [3, 1]
    print("part 1: ", tot_tokens)
    print("part 2: ", tot_tokens2)


def get_input(file_name: str):
    coefs = np.empty((0, 3, 2), dtype=int)
    with open(file_name) as f:
        file_str = f.read().strip()
        confs = file_str.split('\n\n')
        for conf in confs:
            a_coeff = np.array(
                re.search(r'Button A: X\+(\d+), Y\+(\d+)', conf).groups()
            ).astype(int)
            b_coeff = np.array(
                re.search(r'Button B: X\+(\d+), Y\+(\d+)', conf).groups()
            ).astype(int)
            pos = np.array(
                re.search(r'Prize: X=(\d+), Y=(\d+)', conf).groups()
            ).astype(int)
            new_coefs = np.array([a_coeff, b_coeff, pos], dtype=int)
            coefs = np.vstack((coefs, [new_coefs]))
    return coefs


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('sample.txt')
    else:
        main('input.txt')
