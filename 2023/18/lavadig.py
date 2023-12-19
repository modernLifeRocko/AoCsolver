import sys
directions = {
    'R': (0,1),
    'L': (0,-1),
    'U': (-1,0),
    'D': (1,0)
}
def main(file):
    plan = getInstructions(file)
    map = digContour(plan)
    for line in map:
        print(''.join(line))
    fullsize = len(map)*len(map[0])
    frame = { (i,k) for i in range(len(map)) for k in range(len(map[0])) if i*k*(len(map)-i-1)*(len(map[0])-1-k)==0 }
    outside = set()
    for sq in frame:
        if map[sq[0]][sq[1]]=='.':
            blowup(map,sq[0],sq[1],outside)
    print(fullsize - len(outside))

def blowup(map, y, x ,blown = set()):
    if (y,x) in blown: return
    ymin = max(y-1,0)
    ymax = min(y+1,len(map)-1)+1
    xmin = max(x-1,0)
    xmax = min(x+1, len(map[0])-1)+1
    ally = [j for j in range(ymin,ymax)]
    allx = [i for i in range(xmin,xmax)]
    for i in ally:
        for j in allx:
            if map[i][j]=='.':
                blown.add((i,j))
                blowup(map,i,j,blown)

def getInstructions(file):
    with open(file,'r') as  f:
        plan = f.read().splitlines()
        return plan

def getLength(instruction):
    num = ''
    for char in instruction[2:]:
        if char==' ': break
        num += char
    return int(num)

def getColorHex(instruction):
   return instruction[-8:-1]

def digContour(plan):
    map, curr_x, curr_y = initializeMap(plan)
    for instruction in plan:
        map[curr_y][curr_x] = '#'
        num = getLength(instruction)
        dy, dx= getDirection(instruction)
        for i in range(num):
            curr_x+=dx
            curr_y+=dy
            map[curr_y][curr_x]='#'
    return map

def initializeMap(plan):
    maxH, minH = 0, 0
    maxV, minV = 0, 0
    currH = 0
    currV = 0
    for inst in plan:
        num = getLength(inst)
        dir = getDirection(inst)
        currH += num*dir[1]
        currV += num*dir[0]
        if currH > maxH:
            maxH = currH
        elif currH< minH:
            minH = currH
        if currV > maxV:
            maxV = currV
        elif currV < minV:
            minV = currV
    width = maxH-minH+1
    height = maxV-minV+1
    map = [['.' for i in range(width)]for j in range(height)]
    startH = -minH
    startV = -minV
    return map, startH, startV


def getDirection(instruction):
    dir = instruction[0]
    return directions[dir]

if __name__ == "__main__":
    if len(sys.argv)>1:
        file = sys.argv[1]
    else:
        file = 'sample.txt'

    main(file)
