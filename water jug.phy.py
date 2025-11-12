from collections import deque

def water_jug_problem(jug1, jug2, target):
    visited = set()
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(f"({x}, {y})")

        if x == target or y == target:
            print("Goal reached!")
            return

        # Possible states
        q.extend([
            (jug1, y),  # Fill Jug1
            (x, jug2),  # Fill Jug2
            (0, y),     # Empty Jug1
            (x, 0),     # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 -> Jug1
        ])

water_jug_problem(4, 3, 2)
