import sys
import numpy as np


def main(file_name: str):
    grid = get_input(file_name)
    freqs = np.unique(grid)
    freqs = freqs[freqs != '.']
    tot_anods = np.empty((0, 2), dtype=int)
    for f in freqs:
        antenas = np.argwhere(grid == f)
        n = len(antenas)
        for i in range(n):
            for j in range(i + 1, n):
                tot_anods = np.vstack((
                    tot_anods,
                    antinodes(antenas[i], antenas[j], grid)
                ))
    anods_count = len(np.unique(tot_anods, axis=0))
    print("Part 1: ", anods_count)
    res_anodes = np.empty((0, 2), dtype=int)
    for f in freqs:
        antenas = np.argwhere(grid == f)
        n = len(antenas)
        for i in range(n):
            for j in range(i + 1, n):
                res_anodes = np.vstack((
                    res_anodes,
                    res_antinodes(antenas[i], antenas[j], grid)
                ))
    ranods_count = len(np.unique(res_anodes, axis=0))
    print("Part 2: ", ranods_count)


def res_antinodes(ni, nj, grid):
    vect = nj - ni
    anodes = np.array([ni])
    node = nj
    while in_range(node, grid):
        anodes = np.vstack((anodes, node))
        node = node + vect

    node = ni - vect
    while in_range(node, grid):
        anodes = np.vstack((anodes, node))
        node = node - vect
    return anodes


def in_range(node, grid):
    n, m = grid.shape
    in_range_x = node[1] >= 0 and node[1] < m
    in_range_y = node[0] >= 0 and node[0] < n
    in_range = in_range_y and in_range_x
    return in_range


def antinodes(ni, nj, grid):
    vect = nj - ni
    anode1 = ni - vect
    anode2 = vect + nj
    n, m = grid.shape
    tot = np.empty((0, 2), dtype=int)
    for node in (anode1, anode2):
        in_range_x = node[1] >= 0 and node[1] < m
        in_range_y = node[0] >= 0 and node[0] < n
        in_range = in_range_x and in_range_y
        if in_range:
            tot = np.vstack((tot, node))
    return tot


def get_input(file_name: str) -> np.array:
    with open(file_name) as f:
        lines = f.readlines()
        lines = [list(line.strip()) for line in lines]
    return np.array(lines)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main(sys.argv[1])
