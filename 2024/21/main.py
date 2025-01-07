import sys
import re
import numpy as np


dirmove = {
    '^': np.array([-1, 0]),
    '>': np.array([0, 1]),
    'v': np.array([1, 0]),
    '<': np.array([0, -1])
}
dirloc = {
    '^': np.array([0, 1]),
    'A': np.array([0, 2]),
    '<': np.array([1, 0]),
    'v': np.array([1, 1]),
    '>': np.array([1, 2])
}
numloc = {
    '7': np.array([0, 0]),
    '8': np.array([0, 1]),
    '9': np.array([0, 2]),
    '4': np.array([1, 0]),
    '5': np.array([1, 1]),
    '6': np.array([1, 2]),
    '1': np.array([2, 0]),
    '2': np.array([2, 1]),
    '3': np.array([2, 2]),
    '0': np.array([3, 1]),
    'A': np.array([3, 2])
}
dirkb = np.array([['', '^', 'A'], ['<', 'v', '>']])
numkb = np.array([
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', 'A'],
])


def main(file_name: str):
    codes = get_input(file_name)
    tot_comp = 0
    for code in codes:
        print(code)
        numval = int(re.sub('A', '', code))
        fstrobseq = num2dirpad(code)
        sndrobseq = dir2dirpad(fstrobseq)
        # thdrobseq = dir2dirpad(sndrobseq)
        myseq = dir2dirpad(sndrobseq)
        print(len(myseq))
        complexity = len(myseq)*numval
        print(complexity)
        tot_comp += complexity
        print(tot_comp)
    print("part 1:", tot_comp)


def get_input(file_name: str):
    with open(file_name) as f:
        file = f.read()
        codes = re.findall(r'[0-9A]+', file)
    return codes


def num2dirpad(code: str, start: str = 'A') -> str:
    ysgn = {True: 'v', False: '^'}
    xsgn = {True: '>', False: '<'}
    pos = numloc[start]
    seq = ''
    for button in code:
        npos = numloc[button]
        y, x = npos - pos
        moveseq = abs(x)*xsgn[x > 0] + abs(y)*ysgn[y > 0] + 'A'
        seq += moveseq
        pos = npos
    return seq


def dir2dirpad(code: str, start: str = 'A') -> str:
    ysgn = {True: 'v', False: '^'}
    xsgn = {True: '>', False: '<'}
    pos = dirloc[start]
    seq = ''
    for button in code:
        npos = dirloc[button]
        y, x = npos - pos
        # order in d form A >^v<
        moveseq = abs(x)*xsgn[x > 0] + abs(y)*ysgn[y > 0] + 'A'
        seq += moveseq
        pos = npos
    return seq


def simulatepresses(code):
    snd = sim2dir(code)
    fst = sim2dir(snd)
    num = sim2num(fst)
    return num


def sim2dir(code):
    keyseqs = code.split('A')[:-1]
    outcode = ''
    pos = dirloc['A']
    for seq in keyseqs:
        for key in seq:
            pos += dirmove[key]
        outcode += dirkb[pos[0], pos[1]]
    return outcode


def sim2num(code):
    keyseqs = code.split('A')[:-1]
    outcode = ''
    pos = numloc['A']
    for seq in keyseqs:
        for key in seq:
            pos += dirmove[key]
        outcode += numkb[pos[0], pos[1]]
    return outcode


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('input.txt')
    else:
        main('sample.txt')
