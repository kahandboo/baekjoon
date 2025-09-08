def solution(n, words):
    answer = [0, 0]
    dict = set([words[0]])
    pre = words[0][-1]

    for i in range(1, len(words)):
        if words[i] in dict or words[i][0] != pre:
            return [(i%n) + 1, i//n + 1]
        else:
            dict.add(words[i])
            pre = words[i][-1]

    return answer