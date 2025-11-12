import heapq

# Function to calculate Manhattan Distance
def manhattan_distance(start, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(start.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Function to get possible moves of blank space (0)
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    x, y = divmod(index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = state[:]
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(new_state)
    return neighbors

# A* Search Algorithm
def solve_8_puzzle(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start, goal), 0, start, []))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                heapq.heappush(open_list, (g + 1 + manhattan_distance(neighbor, goal), g + 1, neighbor, path + [current]))

    return None

# Example usage
start_state = [1, 2, 3,
               4, 0, 6,
               7, 5, 8]

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

solution = solve_8_puzzle(start_state, goal_state)

if solution:
    print("\nSolution found in", len(solution) - 1, "moves:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found!")
