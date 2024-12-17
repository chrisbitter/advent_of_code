import numpy as np
from itertools import chain
from tqdm import tqdm

raw_grid = []
instructions = []

with open("2415_input") as file:

    for line in file.readlines():
        line = list(line.strip())

        if not line:
            continue
        elif "#" in line:
            raw_grid.append(line)
        else:
            instructions.append(line)

grid = np.array(raw_grid)

robot = np.argwhere(grid == "@")[0]
grid[tuple(robot)] = "."

for instruction in chain.from_iterable(instructions):
    match instruction:
        case "<":
            direction = np.array([0, -1])
        case ">":
            direction = np.array([0, 1])
        case "^":
            direction = np.array([-1, 0])
        case "v":
            direction = np.array([1, 0])

    step = 1

    while True:
        match grid[tuple(robot + step * direction)]:
            case ".":
                if step > 1:
                    # move the box(es)
                    grid[tuple(robot + step * direction)] = "O"
                    grid[tuple(robot + direction)] = "."

                # move the robot
                robot += direction
                break
            case "#":
                break
            case "O":
                pass

        step += 1

    # grid[tuple(robot)] = "@"
    # print(grid)
    # grid[tuple(robot)] = "."

boxes = np.argwhere(grid == "O")

print(np.sum(boxes * np.array([100, 1])))

grid = []

for row in raw_grid:
    new_row = []

    for cell in row:
        match cell:
            case "#":
                new_row += ["#", "#"]
            case "O":
                new_row += ["[", "]"]
            case ".":
                new_row += [".", "."]
            case "@":
                new_row += ["@", "."]

    grid.append(new_row)

grid = np.array(grid)

print(grid)

robot = np.argwhere(grid == "@")[0]
grid[tuple(robot)] = "."

for instruction in tqdm(chain.from_iterable(instructions)):
    match instruction:
        case "<":
            direction = np.array([0, -1])
        case ">":
            direction = np.array([0, 1])
        case "^":
            direction = np.array([-1, 0])
        case "v":
            direction = np.array([1, 0])

    unmoved_objects = {tuple(robot)}
    moved_objects = set()
    
    hit_wall = False
    while unmoved_objects and not hit_wall:
        for obj in unmoved_objects.copy():
        
            new_pos = np.array(obj) + direction
            
            match grid[tuple(new_pos)]:
                case ".":
                    unmoved_objects.discard(obj)
                    moved_objects.add(obj)
                case "#":
                    hit_wall = True
                    break
                case "[":
                    unmoved_objects.add(tuple(new_pos))
                    unmoved_objects.add(tuple(new_pos + np.array([0, 1])))
                    
                    unmoved_objects.discard(obj)
                    moved_objects.add(obj)
                case "]":
                    unmoved_objects.add(tuple(new_pos))
                    unmoved_objects.add(tuple(new_pos + np.array([0, -1])))

                    unmoved_objects.discard(obj)
                    moved_objects.add(obj)
    
    if not unmoved_objects:
        
        objects = [(obj, grid[tuple(obj)]) for obj in moved_objects]
        
        for obj in moved_objects:
            grid[tuple(obj)] = "."
            
        for obj, obj_type in objects:
            new_pos = np.array(obj) + direction
            grid[tuple(new_pos)] = obj_type
            
        robot += direction
        
    # grid[tuple(robot)] = "@"
    # print(grid)
    # grid[tuple(robot)] = "."
    
boxes = np.argwhere(grid == "[")

print(np.sum(boxes * np.array([100, 1])))