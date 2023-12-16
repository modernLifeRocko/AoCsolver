import sys

def main(mapFile):
    patterns = getPatternArray(mapFile)
    patternLimits = getLimits(patterns)
    print(patternLimits)

    patternStartIdx = 0
    score = 0
    for i in patternLimits:
        pattern = patterns[patternStartIdx:i]
        vmirror = getVMirror(pattern)
        hmirror = getHMirror(pattern)
        score += vmirror + 100*hmirror
        patternStartIdx = i+1
    print(score)

    
def getLimits(patterns):
    arr = patterns[:]
    idx = arr.index('')
    limits = []
    while idx:
        try:
            limits.append(idx)
            arr = patterns[idx+1:]
            idx = arr.index('') + idx +1
        except:
            idx = None
    limits.append(len(patterns))
    return limits

def isVMirror(idx: int, pattern: list[str])-> bool:
    length = min(idx, len(pattern[0]) - idx)    
     
    for i in range(length):
        col_pre = [ line[idx-1-i] for line in  pattern ]
        col_pos = [ line[idx+i] for line in pattern ]
        if col_pre != col_pos:
            return False
    return True

def isHMirror(idx: int, pattern: list[str])-> bool:
    length = min(idx, len(pattern) - idx) 
    for i in range(length):
        if pattern[idx+i] != pattern[idx-i-1]:
            return False
    return True

def getHMirror(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        if  isHMirror(i, pattern): return i
    return 0

def getVMirror(pattern: list[str]) -> int:
    for i in range(1, len(pattern[0])):
        if isVMirror(i, pattern): return i
    return 0

def getPatternArray(mapFile):
    with open(mapFile,'r') as f:
        patterns = f.read().splitlines()
        return patterns

if __name__ == "__main__":
    if len(sys.argv)>1:
        mapFile = sys.argv[1]
    else:
        mapFile = 'sample.txt'
    main(mapFile)
    

