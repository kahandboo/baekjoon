from collections import deque
def solution(begin, target, words):
    def checkTransition(a, b):
        same_char_count = 0
        for idx in range(len(a)):
            if a[idx] == b[idx]:
                same_char_count += 1
        
        return True if same_char_count == len(a) - 1 else False
    
    visited = [False] * len(words)
    queue = deque([(begin, len(words))])
    dist = [0] * (len(words) + 1)    
    
    while queue:
        curr_word, idx = queue.popleft()
        
        for i in range(len(words)):
            if not visited[i] and checkTransition(curr_word, words[i]):
                visited[i] = True
                dist[i] = dist[idx] + 1
                queue.append((words[i], i))
            
    return dist[words.index(target)] if target in words else 0