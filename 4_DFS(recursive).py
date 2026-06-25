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
def DFS_recursive(visited,graph,node):
    if node not in visited:
        visited.append(node)
        print(node,end=" ")
        for neighbour in graph[node]:
            DFS_recursive(visited,graph,neighbour)          
print("-" * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL")
print("-" * 50)
print("DFS Order: ", end='')

visited = DFS_recursive(visited, graph, 'A')

print()  # Adds a new line right after the DFS traversal characters print out
print()  # Adds an extra blank line for visual spacing
print("Visited Nodes: ", visited)
print()
print("-" * 50)
print("Program by: Anuska Pradhan")
print("Roll No: 7")