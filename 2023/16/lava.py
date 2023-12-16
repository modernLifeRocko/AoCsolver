import sys

split ={
    '|': {'heap': 'v', 'next':'^'},
    '-':{'heap': '>', 'next': '<'}
}
mirror = {
    '\\': {
        '>': 'v',
        'v': '>',
        '<': '^',
        '^': '<'
    },
    '/': {
        '>': '^',
        '<': 'v',
        'v': '<',
        '^': '>'
    }
}
beam_dir = {
    '>': (0,1),
    '<': (0,-1),
    'v': (1,0),
    '^': (-1,0)
}

def main(file):
    contraption = getContraption(file)
    heap = [('>', (0,0))]
    energized = {(0,0):['>']}
    while heap:
        #print('heap',heap)
        curr_beam, cur_loc = heap.pop()
        inBound = cur_loc[0] in range(len(contraption)) and cur_loc[1] in range(len(contraption[0]))
        if not inBound: continue
        
        while curr_beam:
            # wait = input('enter to continue')
            curr_cont = contraption[cur_loc[0]][cur_loc[1]]
            if cur_loc in energized:
                energized[cur_loc].append(curr_beam)
            else:
                energized[cur_loc] = [curr_beam]
            # print('visited',energized)
            # set next beams/ heap beams
            if curr_cont in split:
                if curr_beam not in split[curr_cont]:
                    heap_beam = split[curr_cont]['heap'] 
                    heap_loc = tuple(x+d for x,d in zip(cur_loc,beam_dir[heap_beam])) 
                    heap.append((heap_beam,heap_loc))
                    
                    curr_beam = split[curr_cont]['next']
                    cur_loc = tuple(x+d for x,d in zip(cur_loc,beam_dir[curr_beam])) 
                else:
                    cur_loc = tuple(x+d for x,d in zip(cur_loc,beam_dir[curr_beam])) 
            elif curr_cont in mirror:
                curr_beam = mirror[curr_cont][curr_beam]
                cur_loc = tuple(x+d for x,d in zip(cur_loc,beam_dir[curr_beam])) 
            else:
                cur_loc = tuple(x+d for x,d in zip(cur_loc,beam_dir[curr_beam]))
            # validate new beam
            dejavu = cur_loc in energized and curr_beam in energized[cur_loc]
            inBound = cur_loc[0] in range(len(contraption)) and cur_loc[1] in range(len(contraption[0]))
            if not inBound or dejavu:
                curr_beam = None
            
    print(len(energized))        

def getContraption(file):
    with open(file,'r') as f:
        contraption = f.read().splitlines()
        return contraption


if __name__ == "__main__":
    if len(sys.argv) >1:
        file = sys.argv[1]
    else:
        file = 'sample.txt'
    
    main(file)
