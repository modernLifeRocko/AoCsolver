import sys
import numpy as np


def main(file_name: str):
    maze = get_input(file_name)
    # score = maze_solve(maze)
    score = dijkstra(maze)
    print("Part 1: ", score)
    pass


def maze_solve(maze: np.array) -> int:
    pos = np.argwhere(maze == 'S')[0]
    dir = np.array([0, 1])
    next_steps = np.empty((0, 3, 2), dtype=int)
    score = np.array([0, 0], dtype=int)
    while maze[*pos] != 'E':
        next_states = get_next_states(pos, dir, score, maze)
        next_steps = insert_to_queue(next_states, next_steps)
        pos, dir, score = next_steps[0]
        next_steps = next_steps[1:]
        # wait = input()
        print(pos, len(next_steps))
    return score[0]


def dijkstra(maze):
    dir_vect = [
        np.array([0, 1]),
        np.array([1, 0]),
        np.array([0, -1]),
        np.array([-1, 0])
    ]
    coords = np.argwhere(maze != '#')
    unv = np.array([
        np.append(coord, (i, np.inf)) for i in range(4) for coord in coords
    ])
    curr = np.argwhere(maze == 'S')[0]
    unv[(unv[:, :-1] == [*curr, 0]).all(1)] = [*curr, 0, 0]
    final = np.copy(unv)
    idx = np.argsort(unv[:, -1])
    unv = unv[idx]
    while unv[0, -1] != np.inf:
        curr_coord = unv[0, :2].astype(int)
        curr_dir = int(unv[0, 2])
        curr_score = unv[0, -1]
        ahead = curr_coord + dir_vect[curr_dir]
        in_unv = (unv[:, :-1] == [*ahead, curr_dir]).all(1).any()  
        if maze[*ahead] != '#' and in_unv:
            nscore = min(curr_score + 1,
                         unv[(unv[:, :-1] == [*ahead, curr_dir]).all(1)][0, -1])
            unv[(unv[:, :-1] == [*ahead, curr_dir]).all(1)] = [*ahead, curr_dir, nscore]
        rdir = (curr_dir + 1) % 4
        right = curr_coord + dir_vect[rdir]
        in_unv = (unv[:, :-1] == [*right, rdir]).all(1).any()
        if maze[*right] != '#' and in_unv:
            nscore = min(curr_score + 1001,
                         unv[(unv[:, :-1] == [*right, rdir]).all(1)][0, -1])
            unv[(unv[:, :-1] == [*right, rdir]).all(1)] = [*right, rdir, nscore]
        ldir = (curr_dir - 1) % 4
        left = curr_coord + dir_vect[ldir]
        in_unv = (unv[:, :-1] == [*left, ldir]).all(1).any()
        if maze[*left] != '#' and in_unv:
            nscore = min(curr_score + 1001,
                         unv[(unv[:, :-1] == [*left, ldir]).all(1)][0, -1])
            unv[(unv[:, :-1] == [*left, ldir]).all(1)] = [*left, ldir, nscore]
        final[(final[:, :-1] == unv[0, :-1]).all(1)] = unv[0]
        unv = unv[1:]
        unv = unv[np.argsort(unv[:, -1])]
        if len(unv) == 0:
            break
    end_coord = np.argwhere(maze=='E')[0]
    mscore = final[(final[:, :2] == end_coord).all(1)][:, -1]
    print(mscore)
    return min(mscore)


def get_next_states(pos, dir, score, maze):
    ahead = pos + dir
    right_dir = dir @ np.array([[0, 1], [-1, 0]])
    right = pos + right_dir
    left_dir = dir @ np.array([[0, -1], [1, 0]])
    left = pos + left_dir
    ns = np.empty((0, 3, 2), dtype=int)
    if maze[*right] != '#':
        ns = np.vstack((ns, [[right, right_dir, score+[1001, 0]]]))
    if maze[*left] != '#':
        ns = np.vstack((ns, [[left, left_dir, score+[1001, 0]]]))
    if maze[*(pos + dir)] != '#':
        ns = np.vstack(([[pos + dir, dir, score + [1, 0]]], ns))
    return ns


def insert_to_queue(vals, queue):
    # assumes both vals and queue come sorted by score
    for val in vals:
        repeated = (queue[:, :-1, :] == val[:-1]).all(1).all(1).any()
        if repeated:
            continue
        idx = np.searchsorted(queue[:, 2, 0], val[2, 0])
        queue = np.insert(queue, idx, val, axis=0)
    return queue


def get_input(file_name: str) -> np.array:
    with open(file_name) as f:
        lines = f.readlines()
        arr = np.array([list(line.strip()) for line in lines])
    return arr


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main(f'sample{sys.argv[1]}.txt')
