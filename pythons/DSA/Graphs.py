# Graph traversal algorithms 
# breadth-first search explore neighbours level by level. 

from collections import deque
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex,end = '')
            visited.add(vertex)
            queue.extend(graph[vertex])

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
bfs(graph, "A")  # Output: A B C D E F