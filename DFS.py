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
visited=[]
stack=[]
def DFS(visited,graph,node):
    stack.append(node)
    visited.append(node)
    while stack:
        m=stack.pop()
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
    return visited,stack
print("-" * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL")
print("-" * 50)
print("DFS Order: ", end='')

visited, stack = DFS(visited, graph, 'A')

print()  # Adds a new line right after the DFS traversal characters print out
print()  # Adds an extra blank line for visual spacing
print("Visited Nodes: ", visited)
print("Stack: ", stack)
print()
print("-" * 50)
print("Program by: Anuska Pradhan")
print("Roll No: 7")