import re
import numpy as np
from collections import defaultdict
from functools import reduce
import matplotlib.pyplot as plt
from tqdm import tqdm


max_position = np.array([101, 103])
quadrants = defaultdict(int)

with open("2414_input") as file:
    for line in file.readlines():
        print(line)

        # sample line: p=0,4 v=3,-3
        values = re.match(
            r"p=([+-]?\d+),([+-]?\d+) v=([+-]?\d+),([+-]?\d+)", line
        ).groups()
        values = np.array(values, dtype=int)

        position = values[:2]
        velocity = values[2:]

        future_position = position + 100 * velocity
        future_position %= max_position

        quadrant = future_position - (max_position - 1) / 2
        quadrant = tuple(np.sign(quadrant).tolist())

        if all(quadrant):
            quadrants[quadrant] += 1

print(quadrants.values())
print(reduce(lambda x, y: x * y, quadrants.values()))


robots = []

with open("2414_input") as file:
    for line in file.readlines():
        values = re.match(
            r"p=([+-]?\d+),([+-]?\d+) v=([+-]?\d+),([+-]?\d+)", line
        ).groups()
        values = np.array(values, dtype=int)

        position = values[:2]
        velocity = values[2:]

        robots.append((position, velocity))

fig, ax = plt.subplots()

# step_from = 0
# step_to = np.prod(max_position)


step_from = 6000
step_to = 7000

metrics = []

for step in tqdm(range(step_from, step_to)):
    future_positions = [
        (position + step * velocity) % max_position for position, velocity in robots
    ]

    positions_array = np.array(future_positions)
    
    mean_distance = np.mean(np.linalg.norm(positions_array[:, np.newaxis] - positions_array, axis=2))
    metrics.append(mean_distance)

min_index = metrics.index(min(metrics))

print(min_index)
print(metrics[min_index])

# plt.plot(metrics)
# plt.savefig("2414_avg_distance.png")

best_step = min_index + step_from

future_positions = [
        (position + best_step * velocity) % max_position for position, velocity in robots
    ]

grid = np.zeros(max_position)
for position in future_positions:
    grid[tuple(position)] = 1

plt.figure()
plt.title(f"Step {best_step}")
plt.imshow(grid)
plt.savefig("2414_result.png")