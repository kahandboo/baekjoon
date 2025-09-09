def solution(want, number, discount):
    items = {}
    for i in range(len(want)):
        items[want[i]] = number[i]

    answer = 0
    left, right = 0, 9

    temp = {}
    for j in range(10):
        if discount[j] in items:
            temp[discount[j]] = temp.get(discount[j], 0) + 1


    while right < len(discount):
        if temp == items:
            answer += 1

        if discount[left] in temp:
            temp[discount[left]] -= 1
            if temp[discount[left]] == 0:
                del temp[discount[left]]
        left += 1
        right += 1
        if right < len(discount) and discount[right] in items:
            temp[discount[right]] = temp.get(discount[right], 0) + 1

    return answer
