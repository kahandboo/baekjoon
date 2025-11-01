import sys
sys.setrecursionlimit(10**6)

tree = list(map(int, sys.stdin.read().split()))
answer = []

def getPostOrder(nodes):
    if len(nodes) == 0:
        return
    
    root = nodes[0]
    left_nodes = []
    right_nodes = []

    for x in nodes[1:]:
        if x < root:
            left_nodes.append(x)
        else:
            right_nodes.append(x)
    
    getPostOrder(left_nodes)
    getPostOrder(right_nodes)
    answer.append(root)



getPostOrder(tree)
print(*answer, sep='\n')