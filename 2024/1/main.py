import sys
import re
import numpy as np


def main(file: str):
    col1, col2 = get_cols(file)
    col1 = np.sort(col1)
    col2 = np.sort(col2)
    diffs = abs(col1 - col2)

    print("Part 1:", sum(diffs))
    similarity = 0
    n, count = np.unique(col2, return_counts=True)
    rep_score = dict(zip(n, count))
    for num in col1:
        in_col2 = rep_score.get(num, 0)
        similarity += num*in_col2
    print("Part 2:", similarity)
    return sum(diffs)


def get_cols(file: str):
    col1 = np.array([])
    col2 = np.array([])
    with open(file) as file_str:
        lines = file_str.readlines()
        for line in lines:
            nums = re.findall(r'\d+', line)
            if len(nums) != 2:
                continue
            col1 = np.append(col1, int(nums[0]))
            col2 = np.append(col2, int(nums[1]))
    return col1, col2


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main("test_input.txt")
    else:
        main('input.txt')
