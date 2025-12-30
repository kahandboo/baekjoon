import sys
sys.setrecursionlimit(10**6)

def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

input = sys.stdin.readline

G = int(input())
P = int(input())
g_list = []
parent = [i for i in range(G+1)]
answer = 0

for _ in range(P):
    g_list.append(int(input()))

for g in g_list:
    k = find(g)
    if k == 0:
        break
    else:
        parent[k] = k-1
        answer += 1

print(answer)