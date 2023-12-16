import sys
import re

def main(initFile):
    initSequence = getSequence(initFile)
    verification = 0
    box = [ {} for i in range(256) ]
    for step in initSequence:
        hash = getHash(step)
        verification += hash
        if '-' in step:
            word = step[:-1]
            boxNum = getHash(word)
            if word in box[boxNum]:
                slot = box[boxNum][word][1]
                del box[boxNum][word]
                box[boxNum].update({lense: [ spec[0],spec[1]-1 ] for lense, spec in box[boxNum].items() if spec[1]>slot })
        else:
            word = step[:-2]
            focal = int(step[-1])
            boxNum = getHash(word)
            if word in box[boxNum]:
                box[boxNum][word][0] = focal
            else:
                box[boxNum][word] = [focal, len(box[boxNum])+1]
                                
    print(box)
    print(focusPower(box))
    print(verification)

def focusPower(boxes):
    focal = 0
    for i, box in enumerate(boxes):
        for lense, specs in box.items():
            focal += (i+1)*specs[0]*specs[1]
    return focal

def findSlot(box, lense):
    regex = '^'+lense
    for i, slot in enumerate(box):
        if lense in slot.keys():
            return i
    return
def getSequence(initFile: str) -> list[str]:
    with open(initFile,'r') as f:
        return f.read().strip().split(',')

def getHash(word: str) -> int:
    hash = 0
    for char in word:
        ascii = ord(char)
        hash += ascii
        hash *= 17
        hash %= 256
    return hash

if __name__ == "__main__":
    if len(sys.argv)>1:
        initFile = sys.argv[1]
    else:
        initFile = 'sample.txt'
    main(initFile)
