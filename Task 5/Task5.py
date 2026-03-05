#DFS
'''tree={
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
start_node= "A"
goal_node= "G"
visited= []

def dfs(tree, start_node, goal_node, visited):
    visited.append(start_node)
    print(visited)

    for i in tree[start_node]:
        if goal_node in visited:
            break
        dfs(tree, i,goal_node,visited)
    return visited

dfs(tree, start_node, goal_node,visited)'''

graph={
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
} 

def dfs(graph, start):
    stack = []
    visited = []

    stack.append(start)

    while stack:
        node =stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for neighbour in reversed(graph[node]):
                stack.append(neighbour)

dfs(graph, "A")

