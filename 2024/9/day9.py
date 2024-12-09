import sys
import numpy as np


def main(file_name: str):
    disk_map = get_map(file_name)
    disk = disk_blocks(disk_map)
    ddisk = defragment(disk)
    checksum = get_checksum(ddisk)
    print("Part 1: ", checksum)
    fdisk = file_defragment(disk)
    fcheck = get_checksum(fdisk)
    print("Part 2: ", fcheck)


def file_defragment(disk):
    ddisk = np.copy(disk)
    last_id = ddisk[np.where(ddisk)[0][-1]]
    for i in range(last_id, 0, -1):
        file = np.where(ddisk == i)[0]
        done = False
        req_free = -1*np.ones(len(file))
        free_idx = np.where(ddisk == -1)[0]
        free_idx = free_idx[free_idx < file[0]]
        for idx in free_idx:
            if done:
                break
            if idx + len(file) <= len(ddisk):
                if all(req_free == ddisk[idx:idx+len(file)]):
                    ddisk[file] = req_free
                    ddisk[idx:idx+len(file)] = i*np.ones(len(file))
                    done = True
            else:
                done = True
    return ddisk


def get_map(file_name: str) -> str:
    with open(file_name) as f:
        map = f.read().strip()
    return map


def get_checksum(disk: np.array) -> int:
    mock_disk = np.copy(disk)
    mock_disk[mock_disk < 0] = 0
    pos = np.arange(len(disk))
    return np.dot(pos, mock_disk)


def defragment(disk: np.array) -> np.array:
    ddisk = np.copy(disk)
    free = np.where(ddisk < 0)[0]
    files = np.where(ddisk >= 0)[0]
    while free[0] < files[-1]:
        ddisk[[free[0], files[-1]]] = ddisk[[files[-1], free[0]]]
        free = np.where(ddisk < 0)[0]
        files = np.where(ddisk >= 0)[0]
    return ddisk


def disk_blocks(disk_map: str) -> np.array:
    blocks = np.array([], dtype=int)
    for i, dig in enumerate(disk_map):
        if i % 2 == 0:
            block = (i//2)*np.ones(int(dig), dtype=int)
            blocks = np.append(blocks, block)
        else:
            block = (-1)*np.ones(int(dig), dtype=int)
            blocks = np.append(blocks, block)
    return blocks


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main('sample.txt')
