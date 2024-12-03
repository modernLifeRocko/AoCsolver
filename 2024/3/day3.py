import numpy as np
import re
import sys


def main(file: str):
    vec1, vec2 = parse_corrupted(file)
    dot_res = np.dot(vec1, vec2)
    print('Part 1: ', dot_res)
    vec1, vec2 = parse_corrupted(file, ignore_conds=False)
    dotted = np.dot(vec1, vec2)
    print('Part 2: ', dotted)


def parse_corrupted(file: str,
                    ignore_conds: bool = True) -> tuple[np.array, np.array]:
    if ignore_conds:
        pat = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    else:
        # pat = re.compile(
        #   r'(?<=do\(\)).*(?<!don\'t\(\))mul\((\d{1,3}),(\d{1,3})\)'
        # )
        pat = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))')
        # startpat = re.compile(r'\A.*?(?=don\'t\(\))')

    with open(file) as openfile:
        file_str = openfile.read()
        if ignore_conds:
            num_pairs = re.findall(pat, file_str)
            nums1, nums2 = zip(*num_pairs)
            nums1 = np.array([int(num) for num in nums1])
            nums2 = np.array([int(num) for num in nums2])
        else:
            groups = re.findall(pat, file_str)
            nums1 = np.array([])
            nums2 = np.array([])
            enabled = True
            for t in groups:
                if enabled:
                    if t[0] != '':
                        nums1 = np.append(nums1, int(t[0]))
                        nums2 = np.append(nums2, int(t[1]))
                    if t[3] != '':
                        enabled = False
                elif t[2] != '':
                    enabled = True
            # attempt with a single look behind regex
            # beg_str = re.findall(startpat, file_str)[0]
            # pat = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
            # startnums = re.findall(pat, beg_str)
            # print(startnums)
            # st_nums1, st_nums2 = zip(*startnums)
            # st_nums1 = [int(num) for num in st_nums1]
            # st_nums2 = [int(num) for num in st_nums2]
            # nums1 = np.append(st_nums1, nums1)
            # nums2 = np.append(st_nums2, nums2)
    return nums1, nums2


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('sample2.txt')
    else:
        main('input.txt')
