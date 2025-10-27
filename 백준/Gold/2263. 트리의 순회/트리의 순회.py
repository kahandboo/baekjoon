import sys

sys.setrecursionlimit(10**6) 

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

preorder = []
idx_map = {val: i for i, val in enumerate(inorder)}

def getPreorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    preorder.append(root)

    root_idx_inorder = idx_map[root] 
    left_subtree_size = root_idx_inorder - in_start
    
    getPreorder(
        in_start, 
        root_idx_inorder - 1, 
        post_start, 
        post_start + left_subtree_size - 1
    )

    getPreorder(
        root_idx_inorder + 1, 
        in_end, 
        post_start + left_subtree_size, 
        post_end - 1
    )

getPreorder(0, n - 1, 0, n - 1)
print(*(preorder))