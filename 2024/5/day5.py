import sys
import numpy as np
import re


def main(file_name: str):
    rules, updates = get_input(file_name)
    is_ordered = get_ordered_update(rules)
    sort_update = get_sort_update(rules)
    mids = []
    dis_mids = []
    for update in updates:
        if is_ordered(update):
            mids.append(update[len(update)//2])
        else:
            ord_upd = sort_update(update)
            dis_mids.append(ord_upd[len(update)//2])
    print("Part 1: ", sum(mids))
    print("Part 2: ", sum(dis_mids))


def get_input(file_name: str) -> tuple[np.array, np.array]:
    with open(file_name) as file:
        f = file.read()
        rulestr, updatestr = f.split('\n\n')
        rulestr = re.findall(r'(\d+)[|](\d+)', rulestr)
        rules = np.array(rulestr, dtype=int)
        updates = [
            np.array(re.findall(r'\d+', update), dtype=int)
            for update in updatestr.strip().split('\n')
        ]
    return rules, updates


def get_ordered_update(rules):
    order = get_order(rules)

    def is_ordered(update):
        n = len(update)
        for i in range(n-1):
            if not order(update[i], update[i+1]):
                return False
        return True
    return is_ordered


def get_order(rules: np.array):
    def order(a: int, b: int) -> bool:
        if b in rules[:, 0]:
            idx = np.where(rules[:, 0] == b)
            if a in rules[idx, 1]:
                return False
        return True
    return order


def get_sort_update(rules: np.array):
    order = get_order(rules)

    def sort_updates(update: np.array):
        sorted_arr = np.array([update[0]])
        n = len(update)
        for i in range(1, n):
            ins_idx = i
            val = update[i]
            for j in range(i-1, -1, -1):
                if order(val, sorted_arr[j]):
                    ins_idx = j
            sorted_arr = np.insert(sorted_arr, ins_idx, val)
        return sorted_arr
    return sort_updates


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main(sys.argv[1])
