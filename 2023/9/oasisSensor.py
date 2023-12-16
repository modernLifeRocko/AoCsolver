import sys
import re

def main(oasisFile):
    f = open(oasisFile,'r')
    histories = f.readlines()
    sumP = 0
    sum = 0
    for history in histories:
        hist = [int(value) for value in re.findall('-?\d+',history)]
        diffTable = getDiffs(hist) 
        nextValue = getNext(diffTable)
        prevValue = getPrevious(diffTable)
        sum += nextValue
        sumP += prevValue
    print(sum, sumP)
    return sum

def getDiffs(arr: list[int]):
    diffs = [arr]
    allZeroes = False
    while not allZeroes:
        diffArr = diffArray(diffs[-1])
        allZeroes = all([val==0 for val in diffArr])
        diffs.append(diffArr)
    return diffs 

def diffArray(arr: list[int])-> list[int]:
    diffs = []
    for i, val in enumerate(arr[:-1]):
        diffs.append(arr[i+1]-val)
    return diffs

def getPrevious(triangle: list[list[int]])->int:
    triangle[-1].insert(0,0)
    for i, line in enumerate(reversed(triangle[:-1])):
        cl = len(triangle)-i-2
        if cl == 0: continue
        curr_diff = triangle[cl][0]
        next_val = triangle[cl-1][0]
        triangle[cl-1].insert(0, next_val-curr_diff)
    return triangle[0][0]

def getNext(triangle: list[list[int]])-> int:
    triangle[-1].append(0)
    for i, line in enumerate(reversed(triangle[:-1])):
        cl = len(triangle) -i -2
        if cl == 0: continue
        curr_diff = triangle[cl][-1]
        base_val = triangle[cl-1][-1]
        triangle[cl-1].append(base_val+curr_diff)
    return triangle[0][-1]

if __name__ == "__main__":
    if len(sys.argv)>1:
        oasisFile = sys.argv[1]
    else:
        oasisFile = 'sample.txt'

    main(oasisFile)
