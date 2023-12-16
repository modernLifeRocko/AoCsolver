import sys
import re

def getStarmap(file: str)->list[str]:
    with open(file,'r') as f:
        starmap = f.read().splitlines()
        return starmap

def getGalaxies(starmap):
    galaxies = []
    for i, line in enumerate(starmap):
        for j, char in enumerate(line):
            if char=='#':
                galaxies.append((i,j))
    return galaxies

def cosmicInflate(starmap):
    infChart = starmap[:]
    infChart = inflateH(infChart)
    infChart = inflateV(infChart)
    return infChart

def inflateH(starmap):
    i = 0
    while i in range(len(starmap)):
        if re.search('\#', starmap[i]):
            i+=1
            continue
        starmap.insert(i,starmap[i])
        i+=2
    return starmap

def inflateV(starmap):
    i = 0
    while i in range(len(starmap[0])):
        col = [ starmap[l][i] for l in range(len(starmap))  ]
        col_str = ''.join(col)
        if re.search('\#',col_str):
            i+=1
            continue
        for l in range(len(starmap)):
            starmap[l] = starmap[l][:i]+'.'+starmap[l][i:]
        i += 2
    return starmap

def getTotalDist(galaxies):
    dist = 0
    for i, galaxy in enumerate(galaxies):
        for galaxy2 in galaxies[i:]:
            dist += getDist(galaxy, galaxy2)
    return dist

def getDist(gal1, gal2):
    x_diff = gal1[1]-gal2[1]
    y_diff = gal1[0]-gal2[0]
    x_dist = x_diff if x_diff>0 else -x_diff
    y_dist = y_diff if y_diff>0 else -y_diff
    return x_dist + y_dist

def getEmptyLines(starmap):
    emptyList = []
    for i, line in enumerate(starmap):
        if re.search('\#',line): continue
        emptyList.append(i)
    return emptyList

def getEmptyCols(starmap):
    emptyList = []
    for i in range(len(starmap[0])):
        line = ''.join([starmap[l][i] for l in range(len(starmap))])
        if re.search('\#',line): continue
        emptyList.append(i)
    return emptyList

def getTotalInfDist(starmap):
    galaxies = getGalaxies(starmap)
    infLines = getEmptyLines(starmap)
    infCols = getEmptyCols(starmap)

    dist = 0
    for i, galaxy in enumerate(galaxies):
        for galaxy2 in galaxies[i:]:
            dist += getInfDist(galaxy, galaxy2, infLines, infCols)
    return dist
            
def getInfDist(gal1, gal2, infLines, infCols):
    min_x = min(gal1[1],gal2[1])
    max_x = max(gal1[1],gal2[1])
    min_y = min(gal1[0],gal2[0])
    max_y = max(gal1[0],gal2[0])

    doubleLines = [ line for line in infLines if line in range(min_y,max_y)]
    doubleCols = [ line for line in infCols if line in range(min_x,max_x)]
    
    return max_x-min_x +len(doubleCols)*(10**6-1) +max_y-min_y + len(doubleLines)*(10**6-1)
    

if __name__ == "__main__":
    if len(sys.argv)>1:
        starFile = sys.argv[1]
    else:
        starFile = 'sample.txt'
    
    starmap = getStarmap(starFile)
    inflatedStarmap = cosmicInflate(starmap)
    galaxies = getGalaxies(inflatedStarmap)
    print(getTotalDist(galaxies))
    print(getTotalInfDist(starmap))
