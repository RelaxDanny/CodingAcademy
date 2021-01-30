"""
다음수업때 아래 링크 참고
youtube.com/watch?v=hettiSrJjM4
[너비 우선 탐색]
Breadth First Search:
    1. is a graph traversal algorithm
    2. finds every vertex that is reachable from the source, and finds its distance
    from the source
    3. Works on Directed and undriected Graphs
    4. Runs is O(V + E) time (vertex + Edge)

BFS Vertex Attributes:
    1. Discovery Status  : color
    2. Distance from source : d

BFS is related to QUEUE!!
"""

tree = {
    'S': ['A', 'B'],
    'A': ['S'],
    'B': ['S','C','D'],
    'C': ['B', 'E', 'F'],
    'D': ['B','G'],
    'E': ['C'],
    'F': ['C']
}

def BFS(array):
    global tree
    index = 0
    nodes_layers = [['S']]

solution, nodes_visited = BFS(['S'])
print()