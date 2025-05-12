from collections import deque

math = input()
dq = deque()
number = 0
i = 0
result = 0

while i < len(math) and math[i].isalnum():
    number = number*10 + int(math[i])
    i += 1
dq.append(number)

while i < len(math):
    if math[i] == '+':
        i += 1
        number2 = 0
        while i < len(math) and math[i].isalnum():
            number2 = number2*10 + int(math[i])
            i += 1
        number = dq.pop()
        dq.append(number + number2)
    else:
        i += 1
        number2 = 0
        number = 0
        while i < len(math) and math[i].isalnum() :
            number = number*10 + int(math[i])
            i += 1
        if i < len(math) and math[i] == '+':
            i += 1
            while i < len(math) and math[i].isalnum() :
                number2 = number2*10 + int(math[i])
                i += 1
            dq.append(number + number2)
        else:
            dq.append(number)


result = dq.popleft()

while dq:
    result -= dq.popleft()

print(result)

