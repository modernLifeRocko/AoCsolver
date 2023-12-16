import re
import math
import sys

def main(schematic='sample.txt'):
    with open(schematic, 'r') as f:
        lines = f.readlines()
        star_coords = {(r,c): [] for r in range(len(lines)) for c in range(len(lines[r])) if lines[r][c]=='*' }
        total:int =0
        for i, line in enumerate(lines):
            for num in re.finditer('\d+',line):
                num_str = num.group()
                num_idx = num.start()
                N = getNeighbors(lines, i, num_idx, len(num_str))
                isAdj =not N.issubset('.1234567890')
                if isAdj: 
                    total += int(num_str)
                starAdj = '*' in N
                if starAdj:
                    neighborStars = getStarCoords(lines, i, num_idx, len(num_str))
                    for coord in neighborStars:
                        star_coords[coord].append(int(num_str))
        gears = {p: star_coords[p] for p in star_coords if len(star_coords[p])==2}
        gear_ratios = {p: math.prod(gears[p]) for p in gears}
        print('parts:',total)
        print('gears:',sum(gear_ratios.values()))

def getStarCoords(arr,r,c,l):
    r_start = max(0,r-1)
    r_end = min(len(arr)-1,r+1)
    c_start = max(0,c-1)
    c_end = min(len(arr[r])-1,c+l+1)
    return {(i,j) for i in range(r_start,r_end+1) for j in range(c_start,c_end) if arr[i][j]=='*'}

def getNeighbors(arr, r, c, l):
    n = len(arr)
    m = len(arr[r])-1 #ignore last char CR
    neighbors = set()
    c_start = max(0,c-1)
    c_end = min(m,c+l+1)
    
    if c>=1:
        neighbors.add(arr[r][c-1])
    
    if c+l<m:
        neighbors.add(arr[r][c+l])

    if r>=1:
        neighbors.update(arr[r-1][c_start:c_end])
    if r+1<n:
        neighbors.update(arr[r+1][c_start:c_end])
    return neighbors

if __name__=='__main__':
    if len(sys.argv)>1:
        print(sys.argv[1])
        main(sys.argv[1])
    else:
        main()
