import sys
import re
import numpy as np


def main(file_name: str):
    layout, guard = get_input(file_name)
    start = guard.pos
    dir = guard.dir
    valid = True
    while valid:
        guard.step_forward(layout)
        valid = guard.goes_out(layout)
    unique = np.unique(guard.route, axis=0)
    print("Part 1: ", len(unique))
    loop_layouts = 0
    for cell in unique:
        new_layout = add_obst(layout, cell)
        new_guard = Guard(start, dir)
        valid = True
        while valid:
            new_guard.step_forward(new_layout)
            dirs = new_guard.rout_dirs[:-1][
                np.equal(new_guard.route[:-1], new_guard.pos).all(1)
            ]
            valid = new_guard.goes_out(new_layout)
            if new_guard.dir in dirs.tolist():
                print(cell)
                loop_layouts += 1
                valid = False
    print("Part 2: ", loop_layouts)


def add_obst(layout, cell):
    new_layout = np.copy(layout)
    new_layout[*cell] = '#'
    return new_layout


def get_input(file_name: str) -> np.array:
    with open(file_name) as file:
        file_str = file.readlines()
        layout = np.empty((0, len(file_str[0].strip())), dtype='<U1')
        for i, line in enumerate(file_str):
            line = line.strip()
            a = re.search(r'\^', line)
            if a:
                pos = np.array((i, a.start()))
                dir = a.group()
                line = re.sub(r'\^', '.', line)
            layout = np.append(layout, [[c for c in line]], 0)
        guard = Guard(pos, dir)
    return layout, guard


class Guard():
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        self.route = np.array([pos])
        self.rout_dirs = np.array([dir])

    dir_vect = {
        '^': np.array((-1, 0)),
        '>': np.array((0, 1)),
        'v': np.array((1, 0)),
        '<': np.array((0, -1))
    }

    def turn_right(self):
        dir_ord = ['^', '>', 'v', '<']
        idx = dir_ord.index(self.dir)
        rot_idx = (idx + 1) % 4
        self.dir = dir_ord[rot_idx]
        self.route = np.append(self.route, [self.pos], 0)
        self.rout_dirs = np.append(self.rout_dirs, self.dir)

    def step_forward(self, layout):
        vect = self.dir_vect[self.dir]
        new_pos = self.pos + vect
        n, m = layout.shape
        if self.can_move(layout):
            self.route = np.append(self.route, [new_pos], 0)
            self.rout_dirs = np.append(self.rout_dirs, self.dir)
            self.pos = new_pos
        elif layout[*new_pos] != '.':
            self.turn_right()

    def can_move(self, layout):
        new_pos = self.pos + self.dir_vect[self.dir]
        n, m = layout.shape
        in_range_y = new_pos[0] >= 0 and new_pos[0] < n
        in_range_x = new_pos[1] >= 0 and new_pos[1] < m
        in_range = in_range_x and in_range_y
        if in_range:
            if layout[*new_pos] == '.':
                return True
        return False

    def goes_out(self, layout):
        new_pos = self.pos + self.dir_vect[self.dir]
        n, m = layout.shape
        in_range_y = new_pos[0] >= 0 and new_pos[0] < n
        in_range_x = new_pos[1] >= 0 and new_pos[1] < m
        in_range = in_range_x and in_range_y
        return in_range


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main(sys.argv[1])
