import sys
import re
import numpy as np


def main(file_name: str):
    grid = get_grid(file_name)
    hor = occurrences(grid)
    ver = occurrences(np.transpose(grid))
    diag = occurrences(get_diags(grid))
    anti_diag = occurrences(get_diags(np.flipud(grid)))
    print('Part 1: ', hor + ver + diag + anti_diag)
    xmas_count = xmas_counter(grid)
    print('Part 2: ', xmas_count)


def xmas_counter(grid: np.array) -> int:
    core_A = zip(*np.where(grid == 'A'))
    n, m = grid.shape
    pat = r'(?=MAS|SAM)'
    counter = 0
    for i, j in core_A:
        if i in {0, n-1} or j in {0, m-1}:
            continue
        block = grid[i-1: i+2, j-1: j+2]
        diag = ''.join(block.diagonal())
        adiag = ''.join(np.flipud(block).diagonal())
        if re.match(pat, diag):
            if re.match(pat, adiag):
                counter += 1
    return counter


def occurrences(grid: list[np.array]) -> int:
    pat = r'XMAS'
    tap = r'SAMX'
    occ = 0
    for row in grid:
        row_str = ''.join(row)
        occ += len(re.findall(pat, row_str))
        occ += len(re.findall(tap, row_str))
    return occ


def get_diags(grid: np.array) -> list[np.array]:
    row, col = grid.shape
    new_grid = []
    for i in range(-row, col):
        new_grid.append(grid.diagonal(i))
    return new_grid


def get_grid(file_name: str) -> np.array:
    grid = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    return np.array(grid)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main(sys.argv[1])
