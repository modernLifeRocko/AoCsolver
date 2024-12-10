import sys
import numpy as np


def main(file_name: str):
    topo_map = get_input(file_name)
    starts = np.argwhere(topo_map == 0)
    score = 0
    rating = 0
    for start in starts:
        if is_trailhead(start, topo_map):
            score += trail_score(start, topo_map)
            rating += trail_rating(start, topo_map)
    print("Part 1: ", score)
    print("Part 2: ", rating)


def is_trailhead(start: np.array, map: np.array) -> bool:
    height = 0
    stack = get_neighbors(start, map)

    while len(stack):
        next_val, stack = stack[-1], stack[:-1]
        if map[*next_val] == 9:
            return True
        else:
            neigh = get_neighbors(next_val, map)
            stack = np.vstack((stack, neigh))

    return False


def get_neighbors(pos: np.array, map: np.array) -> np.array:
    n, m = map.shape
    up = pos + (-1, 0)
    down = pos + (1, 0)
    left = pos + (0, -1)
    right = pos + (0, 1)
    neigh = np.empty((0, 2), dtype=int)
    height = map[*pos]
    for coord in (up, down):
        in_range = coord[0] < n and coord[0] >= 0
        if in_range:
            if map[*coord] == height + 1:
                neigh = np.vstack((neigh, coord))
    for coord in (left, right):
        in_range = coord[1] < m and coord[1] >= 0
        if in_range:
            if map[*coord] == height + 1:
                neigh = np.vstack((neigh, coord))
    return neigh


def trail_score(start: np.array, map: np.array) -> int:
    aux_map = np.copy(map)
    stack = get_neighbors(start, map)
    score = 0

    while len(stack):
        next_val, stack = stack[-1], stack[:-1]
        if aux_map[*next_val] == 9:
            score += 1
            aux_map[*next_val] = -1
        else:
            neigh = get_neighbors(next_val, aux_map)
            stack = np.vstack((stack, neigh))

    return score


def trail_rating(start: np.array, map: np.array) -> int:
    stack = get_neighbors(start, map)
    rating = 0

    while len(stack):
        next_val, stack = stack[-1], stack[:-1]
        if map[*next_val] == 9:
            rating += 1
        else:
            neigh = get_neighbors(next_val, map)
            stack = np.vstack((stack, neigh))

    return rating


def get_input(file_name: str) -> np.array:
    with open(file_name) as f:
        lines = f.readlines()
        arr = np.array([
            [int(num) for num in list(line.strip())] for line in lines
        ])
    return arr


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main('sample.txt')
