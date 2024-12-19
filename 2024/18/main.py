import sys
import numpy as np
import re


def main(file_name: str, grid_size: int, b: int):
    bt_coords = get_input(file_name)
    sim_mem = simulate(grid_size, bt_coords, b)
    min_paths = solve(sim_mem)
    print("Part 1: ", min_paths[grid_size-1, grid_size-1])
    for i in range(b, len(bt_coords)):
        simulmem = simulate(grid_size, bt_coords, i)
        djk = solve(simulmem)
        nexits = djk[grid_size-1, grid_size-1] == np.inf
        if nexits:
            print("Part 2: ", bt_coords[i-1])
            break


def simulate(grid_size, bt_coords, b=None):
    mem = np.zeros((grid_size, grid_size), dtype=int)
    for coord in bt_coords[:b]:
        y, x = coord
        mem[x, y] = 1
    return mem


def solve(maze):
    n, m = maze.shape
    start = np.array([0, 0])
    unv = np.argwhere(maze == 0)
    vals = np.ones(maze.shape)*np.inf
    vals[start[0], start[1]] = 0
    inloop = True
    while inloop:
        x, y = np.transpose(unv)
        curr = np.min(vals[x, y])
        coords = np.argwhere(vals == curr)
        for coord in coords:
            if (unv == coord).all(1).any():
                curr_coord = coord
        neigh = []
        if curr_coord[0]-1 >= 0 and (unv == curr_coord + (-1,0)).all(1).any():
            neigh.append(curr_coord + (-1, 0))
        if curr_coord[0]+1 < n and (unv == curr_coord+(1,0)).all(1).any():
            neigh.append(curr_coord + (1, 0))
        if curr_coord[1]+1 < m and (unv == curr_coord+(0,1)).all(1).any():
            neigh.append(curr_coord + (0, 1))
        if curr_coord[1]-1 >= 0 and (unv == curr_coord+(0,-1)).all(1).any():
            neigh.append(curr_coord + (0, -1))
        for i, j in neigh:
            if vals[i, j] > curr + 1:
                vals[i, j] = curr + 1
        unv = unv[~(unv == curr_coord).all(1)]
        if (vals[*np.transpose(unv)] == np.inf).all():
            inloop = False
    return vals


def get_input(file_name: str):
    with open(file_name) as f:
        file = f.read()
        bt_coords = np.array(re.findall(r'\d+', file)).astype(int)
        bt_coords = np.reshape(bt_coords, (-1, 2))
    return bt_coords


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt', 71, 1024)
    else:
        main('sample.txt', 7, 12)
