# astar_grid.py
import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    open_set = []
    heapq.heappush(open_set, (heuristic(start,goal), 0, start, None))
    came_from = {}
    gscore = {start:0}
    while open_set:
        f, g, current, parent = heapq.heappop(open_set)
        if current in came_from: 
            continue
        came_from[current] = parent
        if current == goal:
            # reconstruct path
            path=[]
            cur=goal
            while cur:
                path.append(cur)
                cur=came_from[cur]
            return list(reversed(path))
        for d in dirs:
            nb=(current[0]+d[0], current[1]+d[1])
            if 0<=nb[0]<rows and 0<=nb[1]<cols and grid[nb[0]][nb[1]]==0:
                tentative = g + 1
                if tentative < gscore.get(nb, float('inf')):
                    gscore[nb]=tentative
                    heapq.heappush(open_set,(tentative+heuristic(nb,goal), tentative, nb, current))
    return None

if __name__=="__main__":
    grid = [
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
    ]
    start=(0,0); goal=(4,4)
    path = astar(grid,start,goal)
    print("Path:", path)
