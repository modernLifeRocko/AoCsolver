import sys
import re

if len(sys.argv)>1:
    race_info = sys.argv[1]
else:
    race_info = 'sample.txt'

race_file = open(race_info,'r')
lines= race_file.readlines()
times_str = re.findall('\d+',lines[0])
real_time = int(''.join(times_str))
times = [int(time) for time in times_str]
record_str= re.findall('\d+',lines[1])
real_record = int(''.join(record_str))
distances = [int(dist) for dist in record_str]

total_ways = 1
for time, dist in zip(times,distances):
    race_ways=0
    for button_down in range(time):
        travel_dist = button_down*(time - button_down)
        if travel_dist <= dist: continue
        race_ways+=1
    print(race_ways)
    total_ways *= race_ways
print(total_ways)
print('part 2 ans')
race_ways=0
for button_down in range(real_time):
    travel_dist = button_down*(real_time - button_down)
    if travel_dist <= real_record: continue
    race_ways+=1
print(race_ways)
