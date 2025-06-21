def solution(sequence, k):
    
    min_len = float('inf')
    N = len(sequence)    
    
    curr_sum = sequence[0]
    left = 0
    right = 0
    answer = []
    
    while left < N and right < N:
        if curr_sum < k:
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
        elif curr_sum > k:
            curr_sum -= sequence[left]
            left += 1
        else:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                answer = [left, right]
            curr_sum -= sequence[left]
            left += 1
    
    return [] if len(answer) == 0 else answer