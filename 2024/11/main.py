import sys
import numpy as np


def main(file_name: str):
    stones = get_input(file_name)
    # total_blinks = 25
    # temp_stones = np.copy(stones)
    # for _ in range(total_blinks):
    #     temp_stones = blink(temp_stones)
    # print("Part 1: ", len(temp_stones))
    total_blinks = 75
    stone_counts = dict(zip(*np.unique(stones, return_counts=True)))
    for _ in range(total_blinks):
        stone_counts = blink_counts(stone_counts)
        if _ == 24:
            print("Part 1: ", sum(stone_counts.values()))
    print("Part 2: ", sum(stone_counts.values()))
    print(len([1 for stone in stone_counts if stone_counts[stone] != 0]))


def get_input(file_name: str) -> np.array:
    with open(file_name) as f:
        file_str = f.read().strip()
        arr = [int(num) for num in file_str.split()]
    return np.array(arr)


def blink(stones: np.array) -> np.array:
    new_arr = np.array([], dtype=int)
    for num in stones:
        stone_str = str(num)
        n = len(stone_str)
        if num == 0:
            new_arr = np.append(new_arr, 1)
        elif n % 2 == 1:
            new_arr = np.append(new_arr, num*2024)
        else:
            fst = stone_str[:n//2]
            snd = stone_str[n//2:]
            new_arr = np.append(new_arr, [int(fst), int(snd)])
    return new_arr


def blink_counts(stone_counts: dict[int, int]) -> dict[int, int]:
    new_count = stone_counts.copy()
    for num, count in stone_counts.items():
        stone_str = str(num)
        n = len(stone_str)
        if num == 0:
            new_count[1] = new_count.get(1, 0) + count
        elif len(stone_str) % 2 == 1:
            new_count[2024*num] = new_count.get(2024*num, 0) + count
        else:
            fst = int(stone_str[:n//2])
            snd = int(stone_str[n//2:])
            new_count[fst] = new_count.get(fst, 0) + count
            new_count[snd] = new_count.get(snd, 0) + count
        new_count[num] -= count
    return new_count


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main('sample.txt')
