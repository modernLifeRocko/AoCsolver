import sys
import re

def main(scratchies):
    with open(scratchies,'r') as f:
        cards = f.readlines()
        card_mult = { cn: 1 for cn in range(len(cards)) } 
        total_points = 0
        for i, card in enumerate(cards):
            [winning_numbers, my_numbers]=re.search(':([0-9\s]*)\|([0-9\s]*)',card).groups()
            winning_numbers=winning_numbers.strip().split(' ')
            my_numbers=[num for num in my_numbers.strip().split(' ') if num!='']
            my_winning_numbers = set(my_numbers).intersection(set(winning_numbers))
            n = len(my_winning_numbers)
            card_points = 2**(n-1) if n>0 else 0
            total_points += card_points
            repeat_cards_start = i+1
            repeat_cards_end = min(i+n+1,len(cards))
            for c in range(i+1,i+n+1):
                card_mult[c]+=card_mult[i]
        print(total_points)
        print('total cards',sum(card_mult.values()))

if __name__=="__main__":
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        main('input.txt')
