import sys
import re

def getInstructions( node: list[str] ) -> str:
    return node[0].strip()

def getMap(node)->list:
    nodes = {}
    for  line in node[2:]:
        node_key = re.search('^\w+',line).group()
        (node_L, node_R) = re.search('\((\w+),\s(\w+)\)',line).groups()
        nodes[node_key] = {'L': node_L, 'R': node_R}
    return nodes

if __name__=='__main__':
    if len(sys.argv)>1:
        nodeFile = sys.argv[1]
    else:
        nodeFile = 'sample.txt'

    f = open(nodeFile, 'r')
    nodes = f.readlines()
    instructions = getInstructions(nodes)
    node_map = getMap(nodes)

    endFound = False
    currentNode = node_map['AAA']
    steps = 0

    while not endFound:
        for inst in instructions:
            nextNodeKey =  currentNode[inst]
            steps += 1
            endFound = nextNodeKey == 'ZZZ'
            if endFound: break
            currentNode = node_map[nextNodeKey]
    print(steps)
    f.close()
