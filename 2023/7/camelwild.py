import sys
# J's are wild
cards = 'J23456789TQKA'
handTypes = ['High card', 'One pair', 'Two pair', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind']

def getHandType(hand:str)->str:
    cardsInHand = { c: 0 for c in cards }
    for card in hand:
        cardsInHand[card] += 1
    wildCount = cardsInHand['J']
    del cardsInHand['J']
    mostRepCard = list(cardsInHand.keys())[list(cardsInHand.values()).index(max(cardsInHand.values()))]
    cardsInHand[mostRepCard]+=wildCount
    if 5 in cardsInHand.values(): return 'Five of a kind'
    if 4 in cardsInHand.values(): return 'Four of a kind'
    if 3 in cardsInHand.values():
        if 2 in cardsInHand.values():return 'Full house'
        return 'Three of a kind'
    if 2 in cardsInHand.values():
        pairs = [ c for c in cardsInHand if cardsInHand[c]==2 ]
        if len(pairs)==2: return 'Two pair'
        return 'One pair'
    return 'High card'

def secOrder(hand1, hand2):
    for card1, card2 in zip(hand1,hand2):
        card1 = cards.index(card1)
        card2 = cards.index(card2)
        if card1 < card2: return True
        if card1 > card2: return False
    return True

def fullOrder(hand1: str, hand2: str)-> bool:
    type1 = handTypes.index(getHandType(hand1))
    type2 = handTypes.index(getHandType(hand2))
    if type1 != type2: return type1 < type2
    return secOrder(hand1, hand2)

def getScore( orderedHands ):
    score = 0
    for i, hand in enumerate(orderedHands):
        score += (i+1)*hand[1]
    return score

def getHandIdx(newHand, orderedHands, low_idx=0, high_idx=None,leq=fullOrder):
    if len(orderedHands)==0: return 0
    if high_idx is None:
        high_idx= len(orderedHands)-1
    if leq(orderedHands[high_idx][0],newHand): return high_idx + 1
    if leq(newHand, orderedHands[low_idx][0]): return low_idx
    mid_idx = (high_idx+low_idx)//2
    if mid_idx==low_idx: return high_idx
    if leq(newHand, orderedHands[mid_idx][0]): return getHandIdx(newHand, orderedHands, low_idx, mid_idx)
    return getHandIdx(newHand, orderedHands, mid_idx, high_idx)
    
if __name__ == '__main__':
    if len(sys.argv)>1:
        camelFile = sys.argv[1]
    else:
        camelFile = 'sample.txt'

    camelInfo = open(camelFile, 'r')
    camelHands = camelInfo.readlines()
    
    orderedHands = [] 
    for camelHand in camelHands:
        [hand, bid] = camelHand.strip().split(' ')
        idx = getHandIdx(hand,orderedHands)
        orderedHands.insert(idx, (hand,int(bid)))
    score = getScore(orderedHands)
    print(score)

    camelInfo.close()


