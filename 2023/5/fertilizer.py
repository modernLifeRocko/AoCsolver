import sys
import re

def main(info):
    m=open(info,'r')
    lines=m.readlines()
    
    seed_pairs = re.findall('\d+\s\d+',lines[0])
    seed_pairs = [ [int(num) for num in pair.split(' ')] for pair in seed_pairs ]
    print(seed_pairs)

    seeds = []
    for pair in seed_pairs:
        for num in range(pair[0],pair[0]+pair[1]):
            seeds.append(num)
    print(seeds)
    locations = []
    for seed in seeds:
        seedSoilTable = getTable('seed-to-soil',lines)
        soil = readMap(seedSoilTable,seed)

        soilFertilizerTable = getTable('soil-to-fertilizer',lines)
        fertilizer = readMap(soilFertilizerTable, soil)

        fertilizerWaterTable = getTable('fertilizer-to-water',lines)
        water = readMap(fertilizerWaterTable, fertilizer)

        waterLightTable = getTable('water-to-light',lines)
        light = readMap(waterLightTable, water)
        
        lightTemperatureTable = getTable('light-to-temperature',lines)
        temperature= readMap(lightTemperatureTable, light)

        lightHumidityTable = getTable('temperature-to-humidity',lines)
        humidity= readMap(lightHumidityTable, temperature)
        
        humidityLocationTable = getTable('humidity-to-location',lines)
        location= readMap(humidityLocationTable, humidity)
        locations.append(location)

    print(min(locations))
    m.close()

def getTable(table_name:str, lines):
    inZone = False
    table = []
    for i, line in enumerate(lines):
        if inZone:
            if line=='\n': break
            newLine = [int(num) for num in re.findall('\d+',line)]
            table.append(newLine)
        if table_name in line:
            inZone = True
    return table

def readMap(table,entry:int):
    for line in table:
        if entry in range(line[1],line[1]+line[2]): return entry - line[1]+line[0]
    return entry
    
if __name__=='__main__':
    if len(sys.argv) >1:
        main(sys.argv[1])
    else:
        main('sample.txt')
