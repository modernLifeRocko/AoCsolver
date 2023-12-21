import sys
directions = {
    'N': (-1,0),
    'S': (1,0),
    'E': (0,1),
    'W': (0,-1)
}
day_steps = 64

def main(mapFile):
    map = getMap(mapFile)
    endSteps = dayStepsFull(map)
    print(len(endSteps))

def getMap(mapFile):
    with open(mapFile,'r') as f:
        map = f.read().splitlines()
        return map

def dayStepsFull(map, steps=day_steps):
    positions = {findStart(map)}
    for i in range(steps):
        positions = evolveStep(map, positions)
    return positions

def findStart(map):
    for i, line in enumerate(map):
        if 'S' in line:
            return (i, line.index('S'))


def evolveStep(map, positionList):
    new_pos = set()
    for y,x in positionList:
        new_pos = new_pos.union(stepSingle(map,(y,x)))
    return new_pos

def stepSingle(map, pos):
    new_pos = set()
    y,x = pos
    for dir in directions.values():
        newx = x+dir[1]
        newy = y+dir[0]
        if newy not in range(len(map)): continue
        if newx not in range(len(map[newy])): continue
        if map[newy][newx]=='#': continue
        new_pos.add((newy,newx))
    return new_pos

            



if __name__ == "__main__":
    mapFile = sys.argv[1] if len(sys.argv)>1 else 'sample.txt'
    main(mapFile)
