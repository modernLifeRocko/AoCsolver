import sys

def getConn(i,j,char):
    if char=='.': return []
    if char=='|': return [(i-1,j),(i+1,j)]
    if char=='-': return [(i,j-1),(i,j+1)]
    if char=='L': return [(i-1,j),(i,j+1)]
    if char=='J': return [(i-1,j),(i,j-1)]
    if char=='7': return [(i+1,j),(i,j-1)]
    if char=='F': return [(i+1,j),(i,j+1)]
    if char=='S': return

def getSConn(i,j,maze):
    possibleNeighbors = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    sConn = []
    for pair in possibleNeighbors:
        if pair[0] in range(len(maze)) and pair[1] in range(len(maze[i])):
            conn = getConn(pair[0],pair[1],maze[pair[0]][pair[1]])
            if (i,j) in conn:
                sConn.append(pair)
    return sConn

def getStart(maze):
    for i, line in enumerate(maze):
        if 'S' in line:
            return (i, line.index('S'))

# unnecessary for input, but should be done in general
def getLoopStart(start, maze):
    sConn = getSConn(*start, maze)
    if len(sConn)==2: return sConn
    
def getNext(curr, prev, maze):
    conn = getConn(*curr, maze[curr[0]][curr[1]])
    return conn[0] if conn[0]!=prev else conn[1] 


if __name__=='__main__':
    if len(sys.argv)>1:
        mazeFile = sys.argv[1]
    else:
        mazeFile = 'sample.txt'

    f = open(mazeFile,'r')
    maze = f.readlines()
    maze = [ line.strip() for line in maze ] 
    startTile = getStart(maze)
    [start, end] = getLoopStart(startTile, maze)


    prev = startTile
    prevE = startTile
    dist = 1
    while start != end:
        if getNext(start, prev, maze)==end:
            print(dist)
            break
        start, prev = getNext(start,prev, maze), start
        end, prevE = getNext(end, prevE, maze), end
        dist += 1 
    print(dist)

