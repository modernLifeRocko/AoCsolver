import sys
import re
import numpy as np


def main(file_name: str):
    layout, start, end = get_input(file_name)
    n, m = layout.shape
    # this is overkill now as the road is unique
    d_from_start = solve_maze(layout, start)
    walls = np.argwhere(layout == 1)
    good_cheats = 0
    for wall in walls:
        y, x = wall
        neighy, neighx = np.array([[y-1, y+1, y, y], [x, x, x-1, x+1]])
        mask = [y-1 >= 0, y+1 < n, x-1 >= 0, x+1 < m]
        neighy = neighy[mask]
        neighx = neighx[mask]
        minent = np.min(d_from_start[neighy, neighx])
        if minent == np.inf:
            continue
        for ny, nx in zip(neighy, neighx):
            # dte = d_to_end[ny, nx]
            nd = d_from_start[ny, nx]
            if nd < np.inf and nd - minent - 2 >= 100:
                good_cheats += 1
    print("part 1: ", good_cheats)


def get_input(file_name: str):
    with open(file_name) as f:
        file = f.read()
        st = re.search('S', file).span()[0]
        end = re.search('E', file).span()[0]
        file = re.sub('S|E', '.', file)
        file = re.sub('#', '1', file)
        file = re.sub('\\.', '0', file)
        maz = np.array(
            [list(line) for line in file.strip().split('\n')]
        ).astype(int)
        n, m = maz.shape
        st_coord = (st//(m+1), st % (m+1))
        end_coord = (end//(m+1), end % (m+1))
    return maz, st_coord, end_coord


def solve_maze(maze, start):
    m, n = maze.shape
    vals = np.ones((m, n))*np.inf
    y_st, x_st = start
    vals[y_st, x_st] = 0
    isUnv = maze == 0
    mazeUnsolved = True
    while mazeUnsolved:
        curr = np.min(vals[isUnv])
        my, mx = np.argwhere((vals == curr) & isUnv)[0]
        if my >= 1 and isUnv[my-1, mx]:
            vals[my-1, mx] = min(vals[my-1, mx], curr + 1)
        if my < m-1 and isUnv[my+1, mx]:
            vals[my+1, mx] = min(vals[my+1, mx], curr + 1)
        if mx < n-1 and isUnv[my, mx+1]:
            vals[my, mx+1] = min(vals[my, mx+1], curr + 1)
        if mx >= 1 and isUnv[my, mx-1]:
            vals[my, mx-1] = min(vals[my, mx-1], curr + 1)
        isUnv[my, mx] = False
        mazeUnsolved = np.sum(isUnv) > 0 and np.min(vals[isUnv]) < np.inf
    return vals


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main('sample.txt')
