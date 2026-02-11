import sys
input = sys.stdin.readline

S = input()
answer = ""
i = 0
S = S[:-1]

while i < len(S):
    s = S[i]

    if s == "<":
        while s != ">":
            answer += s
            i += 1
            s = S[i]
        
        answer += ">"
        i += 1
    else:
        stack = ""
        while s != " " and s != "<":
            stack += s
            i += 1
            if i < len(S):
                s = S[i]
            else:
                break

        reversed_stack = stack[::-1]
        answer += reversed_stack
        if s != "<":
            answer += " "
            i += 1
        

print(answer)
