import re
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

games_file = 'input.txt'

with open(games_file, 'r') as g:
    games = g.readlines()
    total_possible:int = 0
    total_power:int = 0
    for game in games:
        game_number = re.findall('Game\s(\d+):',game)[0]
        blues = re.findall('(\d+)\sblue',game)
        reds = re.findall('(\d+)\sred',game)
        greens = re.findall('(\d+)\sgreen',game)

        max_blues = max([int(blue) for blue in blues])
        max_reds = max([int(red) for red in reds])
        max_greens = max([int(green) for green in greens])
        
        power = max_blues*max_reds*max_greens
        total_power += power

        RED_UNEXCEEDED = max_reds <= bag["red"]
        GREEN_UNEXCEEDED = max_greens <= bag["green"]
        BLUE_UNEXCEEDED = max_blues <= bag["blue"]
        GAME_POSSIBLE = RED_UNEXCEEDED and GREEN_UNEXCEEDED and BLUE_UNEXCEEDED
        if GAME_POSSIBLE:
            total_possible += int(game_number)
    print('Possible total:',total_possible)
    print('Total power:', total_power)
