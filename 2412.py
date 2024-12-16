import numpy as np
from itertools import product

with open("2412_input") as file:
    grid = np.array([list(line.strip()) for line in file.readlines()])

# grid = np.array([["a", "a"], ["a", "c"]])
# grid = np.array([["a", "a", "a"], ["a", "b", "c"], ["a", "a", "a"]])

# perimeter_grid = np.zeros_like(grid, dtype=int)

padded_grid = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2), dtype=str)
padded_grid[1:-1, 1:-1] = grid

perimeter_grid = np.zeros_like(grid, dtype=int)

print(grid)

fence_up = padded_grid[:-2, 1:-1] != grid
fence_down = padded_grid[2:, 1:-1] != grid
fence_left = padded_grid[1:-1, :-2] != grid
fence_right = padded_grid[1:-1, 2:] != grid

neighbour_up = grid == padded_grid[:-2, 1:-1]
neighbour_left = grid == padded_grid[1:-1, :-2]

neighbour_left_with_fence_up = np.zeros_like(grid, dtype=int)
neighbour_left_with_fence_up[:, 1:] = (neighbour_left[:, 1:] * fence_up[:,:-1])
perimeter_grid += fence_up * (1 - neighbour_left_with_fence_up)

neighbour_left_with_fence_down = np.zeros_like(grid, dtype=int)
neighbour_left_with_fence_down[:, 1:] = (neighbour_left[:, 1:] * fence_down[:,:-1])
perimeter_grid += fence_down * (1 - neighbour_left_with_fence_down)


neighbour_up_with_fence_left = np.zeros_like(grid, dtype=int)
neighbour_up_with_fence_left[1:, :] = (neighbour_up[1:, :] * fence_left[:-1,:])
perimeter_grid += fence_left * (1 - neighbour_up_with_fence_left)

neighbour_up_with_fence_right = np.zeros_like(grid, dtype=int)
neighbour_up_with_fence_right[1:, :] = (neighbour_up[1:, :] * fence_right[:-1,:])
perimeter_grid += fence_right * (1 - neighbour_up_with_fence_right)


# perimeter_grid[:-1, :] += (padded_grid[:-2, 1:-1] != padded_grid[2:, 1:-1])
# perimeter_grid[1:, :] += (padded_grid[2:, 1:-1] != padded_grid[:-2, 1:-1])
# perimeter_grid[:, :-1] += (padded_grid[1:-1, :-2] != padded_grid[1:-1, 2:])
# perimeter_grid[:, 1:] += (padded_grid[1:-1, 2:] != padded_grid[1:-1, :-2])

plots = set(product(range(grid.shape[0]), range(grid.shape[1])))

print(plots)

total_price = 0

while plots:
    new_plots = set()
    new_plots.add(plots.pop())
    
    area = 0
    perimeter = 0
    
    while new_plots:
        plot = new_plots.pop()
        plots.discard(plot)
        
        area += 1
        perimeter += perimeter_grid[plot]
        
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour = tuple(np.array(plot) + np.array(direction))
            if neighbour in plots:
                if grid[neighbour] == grid[plot]:
                    plots.discard(neighbour)
                    new_plots.add(neighbour)
                    
    price = area * perimeter
    total_price += price
    
print(total_price)