import heapq

nodes = []

visited = []

class Node:
    def __init__(self, position):
        self.position = position
        self.neighbors = []
        self.previous = None
        self.heuristic = 0

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __repr__(self):
        return f"{self.position} | {self.cost} | {self.neighbors}"

    def __str__(self):
        return f"{self.position}"

with open("2416_input") as file:
    grid = [list(line.strip()) for line in file.readlines()]
    
    print(grid)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, end, grid):
    start_node = Node(start)
    end_node = Node(end)
    
    open_set = []
    heapq.heappush(open_set, (0, start_node))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current.position == end:
            path = []
            while current.position in came_from:
                path.append(current.position)
                current = came_from[current.position]
            path.append(start)
            return path[::-1]
        
        for neighbor in current.neighbors:
            tentative_g_score = g_score[current.position] + 1
            
            if neighbor.position not in g_score or tentative_g_score < g_score[neighbor.position]:
                came_from[neighbor.position] = current
                g_score[neighbor.position] = tentative_g_score
                f_score[neighbor.position] = tentative_g_score + heuristic(neighbor.position, end)
                heapq.heappush(open_set, (f_score[neighbor.position], neighbor))
    
    return None

start = None
end = None

for y, row in enumerate(grid):
    for x, value in enumerate(row):
        node = Node((x, y))
        
        if value != '#':
            nodes.append(node)
            
            if value == 'S':
                start = node
            elif value == 'E':
                end = node

for node in nodes:
    x, y = node.position
    
    neighbour_positions = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    
    node.neigh
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        
        for node in nodes
        
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != '#':
            neighbor = next((n for n in nodes if n.position == (nx, ny)), None)
            if neighbor:
                node.add_neighbor(neighbor)




# heapq.heappush(open_set, (0, start_node))
    