from collections import Counter

def solution(str1, str2):
    def get_multiset(s):
        multiset = []
        for i in range(len(s) - 1):
            if s[i:i+2].isalpha():
                multiset.append(s[i:i+2].upper())
        return multiset

    multiset1 = get_multiset(str1)
    multiset2 = get_multiset(str2)
    
    if not multiset1 and not multiset2:
        return 65536
    
    counter1 = Counter(multiset1)
    counter2 = Counter(multiset2)
    
    intersection = 0
    union = 0
    
    for item in counter1:
        if item in counter2:
            intersection += min(counter1[item], counter2[item])
    
    union_keys = list(set(counter1.keys()) | set(counter2.keys()))
    for item in union_keys:
        union += max(counter1[item], counter2.get(item, 0))
    
    if union == 0:
        return 65536

    return int((intersection / union) * 65536)