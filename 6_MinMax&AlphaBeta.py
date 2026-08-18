#Define the game tree
#Leaf nodes are terminal states with utility
game_tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[5,3], #Leaf values
    'E':[8,2],
    'F':[7,4],
    'G':[9,1]
}

#MinMax without pruning
def minmax(node,is_maximizing):
    #If leaf node, return the value directly
    if isinstance(node,int):
        return node
    if is_maximizing:
        best=-999999
        for child in game_tree[node]:
            value=minmax(child,not is_maximizing)   # FIX: alternate levels
            best=max(best,value)
        return best
    else:
        best=999999
        for child in game_tree[node]:
            value=minmax(child,not is_maximizing)   # FIX: alternate levels
            best=min(best,value)
        return best

#MinMax with Alpha-Beta Pruning
def alpha_beta(node,is_maximizing,alpha,beta):
    #If leaf node, return the value directly
    if isinstance(node,int):
        return node
    if is_maximizing:
        best=-999999
        for child in game_tree[node]:
            value=alpha_beta(child,False,alpha,beta)  # FIX: alternate + correct args
            best=max(best,value)                        # FIX: was min()
            alpha=max(alpha,best)                        # FIX: was beta=min(beta,best)
            if beta<=alpha:
                break #Prune
        return best                                      # FIX: was returning beta
    else:                                                 # FIX: missing branch entirely
        best=999999
        for child in game_tree[node]:
            value=alpha_beta(child,True,alpha,beta)
            best=min(best,value)
            beta=min(beta,best)
            if beta<=alpha:
                break #Prune
        return best

#Display the game tree
print("-" * 50)
print("GAME TREE")
print("-" * 50)
print()
print("                    MAX")
print("                   /   \\")
print("                  /     \\")
print("                 /       \\")
print("               MIN       MIN")
print("              /   \\     /   \\")
print("            MAX   MAX  MAX   MAX")
print("           /  \\  /  \\ /  \\  /  \\")
print("          5   3 8   2 7   4 9   1")
print()

#Run Minmax without pruning
print("-" * 50)
print("MINMAX WITHOUT PRUNING")
print("-" * 50)
root_value = minmax('A', True)
print()
print("Root Value (Best for MAX):", root_value)
print()
print("Explanation:")
print("  - D = max(5,3) = 5")
print("  - E = max(8,2) = 8")
print("  - F = max(7,4) = 7")
print("  - G = max(9,1) = 9")
print("  - B = min(5,8) = 5")
print("  - C = min(7,9) = 7")
print("  - A = max(5,7) = 7")

#Run MinMax with Alpha-Beta Pruning
print()
print("-" * 50)
print("MINMAX WITH ALPHA-BETA PRUNING")
print("-" * 50)
root_value_pruned = alpha_beta('A', True, -999999, 999999)
print()
print("Root Value (Best for MAX):", root_value_pruned)
print()
print("Alpha-Beta pruned branches that cannot affect the final decision.")
print("Result is the same as minimax but faster.")

#Compare Results
print()
print("-" * 50)
print("COMPARISON")
print("-" * 50)
print()
print("Both algorithms found the same root value:", root_value)
print("Alpha-Beta pruning is more efficient.") 