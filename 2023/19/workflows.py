import sys

ruleType={
    '<': lambda x,y: x<y,
    '>': lambda x,y: x>y,
}

def main(file):
    wf, parts = parseFile(file)
    wfRulesDict = getRulesDict(wf)
    wfRulesDict['A'] = ['A']
    wfRulesDict['R'] = ['R']
    partList = getPartDict(parts)
    totalRating = 0
    startFlow = 'in'
    for part in partList:
        if followRule(wfRulesDict[startFlow],part,wfRulesDict):
            totalRating += sum(part.values())
    print(totalRating)
    passableComb =0
    for x in range(1,4001):
        for m in range(1,4001):
            for a in range(1,4001):
                for s in range(1,4001):
                    if followRule(wfRulesDict[startFlow],{'x':x,'m':m,'a':a,'s':s},wfRulesDict):
                        passableComb +=1
    print(passableComb)

def getPartDict(parts):
    partDict = []
    for part in parts:
        partDict.append(parsePart(part))
    return partDict

def getRulesDict(wfList):
    wfDict ={}
    for wf in wfList:
        wfDict.update(parseWorkflow(wf))
    return wfDict

def parseFile(file):
    with open(file,'r') as f:
        lines = f.read().splitlines()
        idx = lines.index('')
        workflows = lines[:idx]
        parts = lines[idx+1:]
        return workflows, parts

def parseWorkflow(wfline):
    idx = wfline.index('{')
    name = wfline[:idx]
    rules = wfline[idx+1:-1].split(',')
    return {name: rules}

def parsePart(part):
    specs = part[1:-1].split(',')
    partDict = {}
    for spec in specs:
        cat = spec[0]
        rating = int(spec[2:])
        partDict[cat] = rating
    return partDict

def followRule(rules,part,wfDict):
    for rule in rules:
        if rule == 'A': return True
        if rule == 'R': return False
        if ':' not in rule: return followRule(wfDict[rule],part,wfDict)
        idx = rule.index(':')
        cat = rule[0]
        ruleRating = int(rule[2:idx])
        ord = rule[1]
        isRuleMet = ruleType[ord](part[cat],ruleRating)
        if isRuleMet:
            return followRule(wfDict[rule[idx+1:]],part,wfDict)
    

if __name__ == "__main__":
    if len(sys.argv)>1:
        file = sys.argv[1]
    else:
        file = 'sample.txt'
    main(file)
