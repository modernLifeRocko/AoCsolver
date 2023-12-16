import re
def main():
    cali_docu='input.txt'
    with open(cali_docu, 'r') as c:
        lines = c.readlines()
        cali_numbers = []
        for line in lines:
            first_digit=getFirstDigit(line)
            last_digit=getLastDigit(line)
            cali_numbers = [*cali_numbers, first_digit*10+last_digit]
        print(sum(cali_numbers))
def getFirstDigit(line:str)->int:
    number=re.search('one|two|three|four|five|six|seven|eight|nine|\d',line).group()
    return int(number) if number.isnumeric() else parseDigit(number)

def getLastDigit(line:str)->int:
    backwardsDigits='eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d'
    backwardsLine=line[::-1]
    backwardsMatch=re.search(backwardsDigits,backwardsLine).group()
    number = backwardsMatch[::-1]
    return int(number) if number.isnumeric() else parseDigit(number)

def parseDigit(digit_str:str)->int:
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return digits.index(digit_str)


if __name__ =='__main__':
    main()
