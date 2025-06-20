def solution(phone_book):
    answer = True
    hashtable = {}
    
    for n in phone_book:
        hashtable[n] = 1
    
    for number in phone_book:
        s = ""
        for i in number:
            s += i
            if s in hashtable:
                if number != s:
                    answer = False
                    return answer

    
    return answer