from itertools import product

def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    result = [0, 0]
    discount = list(product(sale, repeat=len(emoticons)))
    for d in discount:  
        total_join = 0  
        total_income = 0  

        for user in users:
            r, p = user
            cost = 0
            for i in range(len(emoticons)):
                if d[i] >= r:
                    cost += emoticons[i] * (100 - d[i]) / 100

            if cost >= p:
                total_join += 1
            else:
                total_income += cost


        if total_join > result[0] or (total_join == result[0] and total_income > result[1]):
            result = [total_join, total_income]

    return result