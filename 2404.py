import numpy as np
import re

with open("2404_input") as file:
    grid = np.array([list(line.strip()) for line in file.readlines()])

# print(grid.shape)
# print(grid)

result_1 = 0
result_2 = 0

def find_words(raw_line):
    line = "".join(raw_line)
    # print(list(re.finditer("XMAS", line)))
    # print(list(re.finditer("SAMX", line)))
    return len(list(re.finditer("XMAS", line))) + len(list(re.finditer("SAMX", line)))

# rows - forward
for raw_line in grid:
    result_1 += find_words(raw_line)

for raw_line in grid.T:
    result_1 += find_words(raw_line)

for offset in range(-grid.shape[0] + 1, grid.shape[1]):
    result_1 += find_words(grid.diagonal(offset))
    result_1 += find_words(np.rot90(grid).diagonal(offset))
    
    
print("Solution 1")
print(result_1)


from itertools import product

for ii, jj in product(range(1, grid.shape[0] - 1), range(1, grid.shape[1] - 1)):
    if grid[ii, jj] != "A": continue
        
    if "".join([grid[ii-1, jj-1], "A", grid[ii+1, jj+1]]) in ["MAS", "SAM"] and "".join([grid[ii-1, jj+1], "A", grid[ii+1, jj-1]]) in ["MAS", "SAM"]:
        result_2 += 1
    

print("Solution 2")
print(result_2)