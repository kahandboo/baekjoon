N = int(input())
ans = ''
if N < 4:
    ans = 'a' * N
else:
    if (N % 2 == 0):
        ans = 'a' * (N//4) * 4
    else:
        ans = 'a' * (N//4) * 4
        
        for i in range(2):
            q, r = divmod(N, 2)

            if (r != 0):
                if (i == 0):
                    ans += 'a'
                else:
                    ans += 'a' * 2
            
            N = q

    
            
print(ans)