from collections import deque
from pathlib import PosixPath


def tree_style(depth):
    for _ in range(0, depth):
        print("--", end="")

def bfs(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    
    while queue:
        node, depth = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            
            tree_style(depth)
            print(node)
            
            try:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, depth + 1))
            except KeyError:
                pass
