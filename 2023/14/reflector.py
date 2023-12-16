import sys

def getPlatform(systemFile):
    with open(systemFile) as f:
        platform = f.read().splitlines()
        return platform

def printPlat(platform):
    for line in platform:
        print(line)

def tiltPlatform(platform: list[str]) -> list[str]:
    tiltedPlatform = [list(line) for line in platform ] 
    for l, line in enumerate(tiltedPlatform):
        if l ==0: continue
        for k, sq in enumerate(line):
            if sq != 'O': continue
            idx = findTiltIndex(tiltedPlatform, (l,k))
            if l == idx: continue
            tiltedPlatform[l][k] = '.' 
            tiltedPlatform[idx][k] = 'O'
    return [''.join(line) for line in tiltedPlatform]

def findTiltIndex(platform: list[list[str]], loc: tuple[int, int])->int:
    y = loc[0]
    x = loc[1]
    colx = [platform[i][x] for i, _ in enumerate(platform) if i<y]
    for i, sq in enumerate(reversed(colx)):
        if sq =='.': continue
        return y-i
    return 0

def calculateLoad(platform):
    load = 0
    for l, line in enumerate(reversed(platform)):
        for k, sq in enumerate(line):
            if sq != 'O': continue
            load += l+1
    return load

def main(systemFile):
    platform = getPlatform(systemFile)
    tiltedPlat = tiltPlatform(platform)
    load = calculateLoad(tiltedPlat)
    print('load:',load)
    
if __name__ == "__main__":
    if len(sys.argv)>1:
        systemFile = sys.argv[1]
    else:
        systemFile = 'sample.txt'
    main(systemFile)
