import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

hashtable = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if (len(word) >= M):
        if word not in hashtable:
            hashtable[word] = [0, len(word)]
        else:
            hashtable[word][0] += 1
    

sorted_keys = sorted(
    hashtable.keys(),
    key = lambda k: (-hashtable[k][0], -hashtable[k][1], k)
)

sys.stdout.write('\n'.join(sorted_keys) + '\n')