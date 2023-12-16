import wasteland as wl 
import sys
import re

if len(sys.argv)>1:
    nodeFile = sys.argv[1]
else:
    nodeFile = 'ghost_sample.txt'

f = open(nodeFile, 'r')
nodes = f.readlines()
instructions = wl.getInstructions(nodes)
nodesMap = wl.getMap(nodes)

ghostNodeKeys = [c for c in nodesMap.keys() if re.search('A$', c)]
ghostNodes = [nodesMap[ghost] for ghost in ghostNodeKeys]
endFound =  False
steps = 0

while not endFound:
    for inst in instructions:
        nextKeys = [ghost[inst] for ghost in ghostNodes]
        steps +=1
        endFound = all([True if re.search('Z$',key) else False for key in nextKeys])
        if endFound: break
        ghostNodes = [nodesMap[ghost] for ghost in nextKeys]
print(steps)
