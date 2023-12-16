import sys
import re

def getSingleRec(lineRecord):
    [schema, blocks] = lineRecord.split()
    blocks = [int(num) for num in blocks.split(',') ]
    return [schema, blocks]

def findRecMatch(schema, blocks):
    idx = getUnknownSprings(schema)
    possibleSchemes = [bin(num)[2:].zfill(len(idx)) for num in range(2**len(idx))]
    possibleSchemes = [re.sub('1','#',schema) for schema in possibleSchemes]
    possibleSchemes = [re.sub('0','.',schema) for schema in possibleSchemes]
    print(possibleSchemes)
    
    fittingSchemes =[]
    for sch in possibleSchemes:
        tempSchema = getTrialSchema(schema, sch)
        isMatch = [len(block) for block in re.findall('\#+',tempSchema)]==blocks  
        if isMatch:
            fittingSchemes.append(tempSchema)
    return fittingSchemes

def getUnknownSprings(schema):
    unknownSprings = []
    lstschema = list(schema)
    for i, spring in enumerate(lstschema):
        if spring!='?': continue
        unknownSprings.append(i)
    return unknownSprings

def getTrialSchema(schema, sch):
    tmpschem = list(schema)
    idx = getUnknownSprings(schema)
    for i, id in enumerate(idx):
        tmpschem[id] = sch[i]
    return ''.join(tmpschem)

def unfoldSchema(schema, folds=5):
    return '?'.join([schema for _ in range(folds)])

def unfoldBlocks(blocks, folds=5):
    unfoldedBlocks =[]
    for _ in range(folds):
        unfoldedBlocks = [*unfoldedBlocks, *blocks]
    return unfoldedBlocks

if __name__ == '__main__':
    if len(sys.argv)>1:
        springRecord = sys.argv[1]
    else:
        springRecord = 'sample.txt'

    with open(springRecord,'r') as f:
        records = f.read().splitlines()
        matchTotalWays =  0
        for record in records:
            [schema, blocks] = getSingleRec(record)
            # only for part2
            schema = unfoldSchema(schema)
            blocks = unfoldBlocks(blocks)
            matchTotalWays += len(findRecMatch(schema,blocks))
        print(matchTotalWays)
