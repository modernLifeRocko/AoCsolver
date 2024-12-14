import sys
import matplotlib.pyplot as plt
import numpy as np
import re


def main(file_name: str, width, height):
    robots = get_input(file_name)
    t = 100
    robots_per_quadrant = np.zeros(4, dtype=int)
    for x, v in robots:
        fpos = x + t*v
        quad = get_quadrant(fpos, width, height)
        if quad:
            robots_per_quadrant[quad-1] += 1
    print(robots_per_quadrant)
    print("Part 1: ", np.prod(robots_per_quadrant))
    sscore = 0
    for i in range(width*height):
        nscore = safety_score(robots, i, width, height)
        if nscore < 1e8:
            robot_pos = np.mod(robots[:, 0] + i*robots[:, 1], [height, width])
            plt.figure()
            plt.scatter(robot_pos[:, 0], robot_pos[:, 1])
            plt.savefig(f"out/{i}.jpg")
            print(i)
        sscore = nscore


def draw(robot_pos, width, height):
    area = np.zeros((height, width))
    for x, y in robot_pos:
        area[y % height, x % width] += 1
    return area


def safety_score(robots, t, width, height):
    robots_per_quadrant = np.zeros(4, dtype=int)
    for x, v in robots:
        fpos = x + t*v
        quad = get_quadrant(fpos, width, height)
        if quad:
            robots_per_quadrant[quad-1] += 1
    return np.prod(robots_per_quadrant)


def get_quadrant(pos: np.array, width: int, height: int) -> int:
    # assume odd dims
    y_axis = width//2
    x_axis = height//2
    x, y = pos
    x %= width
    y %= height
    if x < y_axis:
        if y < x_axis:
            return 1
        if y > x_axis:
            return 2
    if x > y_axis:
        if y < x_axis:
            return 3
        if y > x_axis:
            return 4
    return 0


def get_input(file_name: str) -> np.array:
    with open(file_name) as f:
        fstr = f.read()
        robots = np.array(
            re.findall(r'[pv]=(-?\d+),(-?\d+)', fstr)
        ).astype(int)
        robots = np.reshape(robots, (len(robots)//2, 2, 2))
    return robots


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('sample.txt', 11, 7)
    else:
        main('input.txt', 101, 103)
