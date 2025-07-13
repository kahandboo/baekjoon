import sys

def preorder(node):
    if node == '.':
        return
    preorderList.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    inorderList.append(node)
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    postorderList.append(node)

N = int(sys.stdin.readline())
tree = {}


for _ in range(N):
    root, left, right = sys.stdin.readline().split()

    tree[root] = [left, right]

preorderList = []
inorderList = []
postorderList = []

preorder('A')
inorder('A')
postorder('A')

for pre in preorderList:
    sys.stdout.write(pre)

sys.stdout.write('\n')

for i in inorderList:
    sys.stdout.write(i)

sys.stdout.write('\n')

for po in postorderList:
    sys.stdout.write(po)