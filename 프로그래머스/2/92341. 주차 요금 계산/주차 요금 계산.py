import math
def solution(fees, records):
    def calculateTimeDiff(a, b):
        a_hour, a_min = map(int, a.split(':'))
        b_hour, b_min = map(int, b.split(':'))
        
        a_time = a_hour * 60 + a_min
        b_time = b_hour * 60 + b_min
        
        return b_time - a_time
        
    answer = {}
    history = {}
    result = []
    
    for record in records:
        time, number, act = record.split()
        number = int(number)
        
        if act == 'IN':
            history[number] = time
        else:
            inTime = history[number]
            del history[number]
            
            diff = calculateTimeDiff(inTime, time)
            answer[number] = answer.get(number, 0) + diff
        
    for number in history:
        inTime = history[number]

        diff = calculateTimeDiff(inTime, "23:59")
        answer[number] = answer.get(number, 0) + diff
        
    sorted_answer = dict(sorted(answer.items()))
    
    for time in sorted_answer.values():
        if time <= fees[0]:
            result.append(fees[1])
        else:
            total = fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3]
            result.append(total)
    
    return result