from itertools import permutations

def travelling_salesman(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    best_path = None

    for perm in permutations(vertices):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]

        if current_cost < min_path:
            min_path = current_cost
            best_path = perm

    print("Shortest Path:", (start,) + best_path + (start,))
    print("Minimum Cost:", min_path)

graph = {
    'A': {'A':0,'B':10,'C':15,'D':20},
    'B': {'A':10,'B':0,'C':35,'D':25},
    'C': {'A':15,'B':35,'C':0,'D':30},
    'D': {'A':20,'B':25,'C':30,'D':0}
}

travelling_salesman(graph, 'A')
