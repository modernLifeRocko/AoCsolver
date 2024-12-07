import sys
import re
import numpy as np
from functools import reduce


def main(file_name: str):
    vals, eqns = get_input(file_name)
    valid_tests = np.array([])
    concat_valid = np.array([])
    for test, nums in zip(vals, eqns):
        valid_calibration: bool = is_valid(test, nums, allow_concat=False)
        if valid_calibration:
            valid_tests = np.append(valid_tests, test)
        elif is_valid(test, nums, allow_concat=True):
            concat_valid = np.append(concat_valid, test)

    print("Part 1: ", sum(valid_tests))
    print("Part 2: ", sum(valid_tests) + sum(concat_valid))


def is_valid(test: np.array,
             nums: list[np.array],
             allow_concat: bool = False) -> bool:
    n = len(nums)
    if allow_concat:
        base = 3
    else:
        base = 2
    for i in np.arange(base**(n-1)):
        ops = np.array(list(np.base_repr(i, base).zfill(n-1))).astype(np.uint8)
        tot = reduce(
            lambda acc, y: opr(ops[y[0]], acc, y[1]),
            enumerate(nums[1:]),
            nums[0]
        )
        if tot == test:
            return True
    return False


def opr(o: int, a: int, b: int) -> int:
    if o == 1:
        return a * b
    if o == 0:
        return a + b
    if o == 2:
        return int(str(a)+str(b))


def get_input(file_name: str):
    test_vals = np.array([])
    eqns = []
    with open(file_name) as f:
        file_lines = f.readlines()
        for cal_eq in file_lines:
            eq = re.search(r'(?P<cal>\d+): (?P<nums>.+)', cal_eq)
            test = int(eq.group('cal'))
            test_vals = np.append(test_vals, test)
            nums = re.findall(r'\d+', eq.group('nums'))
            nums = np.array([int(num) for num in nums])
            eqns.append(nums)
    return test_vals, eqns


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main(sys.argv[1])
