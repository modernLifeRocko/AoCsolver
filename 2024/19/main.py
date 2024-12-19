import sys
import re
from functools import cache


def main(file_name: str):
    pats, des = get_input(file_name)
    # pat_regex = '|'.join(pats)
    # comp = re.compile(rf'^({pat_regex})+$')
    pos_des = 0

    @cache
    def pat_match(text):
        if text == '':
            return True
        return any(
            [pat_match(text[len(pat):]) for pat in pats if re.match(pat, text)]
        )

    for d in des:
        if pat_match(d):
            pos_des += 1
    print("Part 1: ", pos_des)


def get_input(file_name: str) -> tuple[list[str], list[str]]:
    with open(file_name) as f:
        file = f.read()
        pats, designs = file.split('\n\n')
        pat_list = re.findall(r'[rgbuw]+', pats)
        des_list = designs.strip().split('\n')
    return pat_list, des_list


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main('sample.txt')
