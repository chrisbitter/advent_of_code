from itertools import combinations
import numpy as np

with open("2408_input") as file:
    antennas = []
    
    for xx, line in enumerate(file.readlines()):
        for yy, char in enumerate(line.strip()):
            if char != ".":
                antennas.append((xx, yy, char))
            
print(xx, yy)

antenna_types = set([antenna[2] for antenna in antennas])
antinodes = set()

# print(antenna_types)

for antenna_type in antenna_types:
    antenna_positions = np.array([antenna[:2] for antenna in antennas if antenna[2] == antenna_type])
    
    for antenna_position_1, antenna_position_2 in combinations(antenna_positions, 2):
        delta = antenna_position_2 - antenna_position_1
        
        antinodes.add(tuple(antenna_position_1))
        antinodes.add(tuple(antenna_position_2))
        
        kk = 1
        while True:
            antinode = antenna_position_1 - kk * delta
            
            if not all([0 <= antinode[0] <= xx, 0 <= antinode[1] <= yy]):
                break
            antinodes.add(tuple(antinode))
            kk += 1
        
        kk = 1
        while True:
            antinode = antenna_position_2 + kk * delta
            if not all([0 <= antinode[0] <= xx, 0 <= antinode[1] <= yy]):
                break
            antinodes.add(tuple(antinode))
            kk += 1
            
            
        
        antinode_1 = antenna_position_1 - delta
        antinode_2 = antenna_position_2 + delta
        
        antinodes.add(tuple(antinode_1))
        antinodes.add(tuple(antinode_2))
        
antinodes = [antinode for antinode in antinodes if all([0 <= antinode[0] <= xx, 0 <= antinode[1] <= yy])]
    
print(len(antinodes))