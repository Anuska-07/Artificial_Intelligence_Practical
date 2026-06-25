graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['G','H'],
    'E':['I'],
    'F':[],
    'G':[],
    'H':[],
    'I':[]
}
graph
visited=[] #List for visited nodes
queue=[] #Initialize a stack
def BFS(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m, end=' ')
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited,queue
print("-" * 50)
print("BREADTH-FIRST SEARCH TRAVERSAL")
print("-" * 50)
print("BFS Order: ", end='')

visited, stack = BFS(visited, graph, 'A')

print()  # Adds a new line right after the DFS traversal characters print out
print()  # Adds an extra blank line for visual spacing
print("Visited Nodes: ", visited)
print("Stack: ", stack)
print()
print("-" * 50)
print("Program by: Anuska Pradhan")
print("Roll No: 7")

