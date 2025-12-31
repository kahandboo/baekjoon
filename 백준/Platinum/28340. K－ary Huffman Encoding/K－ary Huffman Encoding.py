import sys, heapq
input = sys.stdin.readline

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.children = None

    def __lt__(self, other):
        return self.freq < other.freq

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    C = list(map(int, input().split()))
    tree = []

    for c in C:
        node = Node(c)
        tree.append(node)

    heapq.heapify(tree)

    while (len(tree) - 1) % (k-1) != 0:
        heapq.heappush(tree, Node(0))

    while len(tree) > 1:
        children = []
        sum_freq = 0

        for _ in range(k):
            if tree:
                child = heapq.heappop(tree)
                children.append(child)
                sum_freq += child.freq

        parent = Node(sum_freq)
        parent.children = children

        heapq.heappush(tree, parent)
    
    node = heapq.heappop(tree)
    def traverse(node, path):
        if not node.children:
            return node.freq * path
        
        total = 0
        for child in node.children:
            total += traverse(child, path + 1)
        return total

    result = traverse(node, 0)
    sys.stdout.write(str(result) +'\n')