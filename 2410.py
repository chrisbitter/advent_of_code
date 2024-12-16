import numpy as np

grid = []

with open("2410_input") as file:
    for line in file.readlines():
        grid.append(list(line.strip()))

grid = np.array(grid, dtype=int)


for part in range(2):
    result = 0

    for start in np.argwhere(grid == 0):
        poses = [start]
        
        for level in range(1, 10):
            new_poses = []
            
            for pose in poses:
                for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    new_pose = pose + delta
                    
                    if any(new_pose < np.zeros(2)) or any(np.array(grid.shape) <= new_pose):
                        continue
                    
                    
                    if grid[tuple(new_pose)] == level:
                        new_poses.append(new_pose)
                        
            poses = new_poses
            
            if not poses:
                break
            
            if not part:
                # part 1
                unique_poses = list({tuple(pose) for pose in poses})
                poses = [np.array(pose) for pose in unique_poses]
            
        result += len(poses)
        
    print(result)
            