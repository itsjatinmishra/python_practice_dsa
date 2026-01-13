from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7],
    5: [],
    6: [],
    7: []
}

bfs(graph, 1)