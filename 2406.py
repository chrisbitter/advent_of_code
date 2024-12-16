import numpy as np
import re
from tqdm import tqdm

obstacles = []
start_position = None

max_bounds = np.zeros(2, dtype=int)

with open("2406_input") as file:
    for xx, line in enumerate(file.readlines()):
        max_bounds[0] = xx
        max_bounds[1] = len(line) - 1

        for match in re.finditer(r"#", line):
            obstacles.append((xx, match.start()))

        if "^" in line:
            start_position = (xx, line.index("^"))

print(obstacles)
print(start_position)

start_velocity = (-1, 0)

### Part 1

position = start_position
velocity = start_velocity
visited_positions = set()

while True:
    visited_positions.add(position)

    next_position = (position[0] + velocity[0], position[1] + velocity[1])

    if next_position in obstacles:
        velocity = (velocity[1], -velocity[0])
        continue

    if any(np.array(next_position) < 0) or any(np.array(next_position) > max_bounds):
        # out of bounds
        break

    position = next_position

print("Solution 1")
print(len(visited_positions))

### Part 2

loops = 0

visited_positions.discard(start_position)

for xx, yy in tqdm(visited_positions):
    if (xx, yy) in obstacles or (xx, yy) == start_position:
        # cant place an obstacle here
        continue

    pose = start_position + start_velocity
    visited_poses = set()

    while True:
        if pose in visited_poses:
            loops += 1
            break

        visited_poses.add(pose)

        position, velocity = pose[:2], pose[2:]
        next_position = (position[0] + velocity[0], position[1] + velocity[1])

        if any(np.array(next_position) < 0) or any(
            np.array(next_position) > max_bounds
        ):
            # out of bounds
            break

        if next_position in obstacles or next_position == (xx, yy):
            pose = position + (velocity[1], -velocity[0])
        else:
            pose = next_position + velocity

print("Solution 2")
print(loops)
