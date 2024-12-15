import sys
import numpy as np
import re


def main(file_name: str):
    layout, pos, moves = get_input(file_name)
    pos, layout = boxaform(layout, pos, moves)
    print('Part 1: ', gps(layout))


def boxaform(layout, pos, moves):
    mod_layout = np.copy(layout)
    for move in moves:
        npos = pos + move
        if mod_layout[*npos] == '.':
            pos = npos
        elif mod_layout[*npos] == 'O':
            box_ahead = movable_boxes_ahead(npos, move, mod_layout)
            for box in box_ahead:
                mod_layout[*box] = '.'
            for box in box_ahead:
                mod_layout[*(box+move)] = 'O'
            if len(box_ahead):
                pos = npos
            # print(box_ahead)
            # if len(box_ahead):
            #     mod_layout[*box_ahead] = '.'
            #     mod_layout[*(box_ahead + move)] = 'O'
    return pos, mod_layout


def movable_boxes_ahead(pos, move, layout):
    npos = np.copy(pos)
    boxes = np.empty((0, 2), dtype=int)
    while layout[*npos] == 'O':
        ahead = npos + move
        if layout[*ahead] == '#':
            boxes = np.empty((0, 2), dtype=int)
            npos = ahead
        else:
            boxes = np.vstack((boxes, npos))
            npos = ahead
    return boxes


def gps(layout: np.array) -> int:
    boxes = np.argwhere(layout == 'O')
    x = boxes[:, 1]
    y = boxes[:, 0]
    return sum(x+100*y)


def get_input(file_name: str) -> tuple[np.array, np.array, np.array]:
    dir_dict = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }
    with open(file_name) as f:
        file = f.read()
        sub_map, moves = file.split('\n\n')
        sub_map = np.array(
            [list(line) for line in sub_map.strip().split('\n')]
        )
        pos = np.argwhere(sub_map == '@')[0]
        sub_map[*pos] = '.'
        moves = re.findall(r'[v><^]', moves)
        moves = np.array([dir_dict[move] for move in moves], dtype=int)
    return sub_map, pos, moves


if __name__ == "__main__":
    if len((sys.argv)) <= 1:
        main('minisample.txt')
    else:
        main('input.txt')
