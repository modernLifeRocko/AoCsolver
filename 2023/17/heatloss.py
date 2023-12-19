import sys

def main(file):
    cityMap = getMap(file)
    path = minHeatPath(cityMap)
    heat = getHeatLoss(path,cityMap)

def getMap(file):
    with open(file,'r') as f:
        map = f.read().splitlines()
        return map

def getGraph(map):
    pass

def minHeatPath(cityMap: list[str]):
    graph = getGraph(cityMap)
    pass


if __name__ == "__main__":
    if len(sys.argv)>1:
        file = sys.argv[1]
    else:
        file = 'sample.txt'
    # main(file)
