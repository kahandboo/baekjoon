import sys
import random

search_order_a = list(range(1, 10001))
search_order_b = list(range(1, 10001))

random.shuffle(search_order_a)
random.shuffle(search_order_b)

for a in search_order_a:
    # A가 a인지 물어보고 flush를 한다.
    # print에 flush 파라미터를 넣으면 된다.
    print("? A", a, flush=True)

    # 채점기의 답변을 입력받는다.
    resp = int(input())

    if resp == 1:
        # 답변이 "예"이므로 A의 값은 a이다.
        # B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
        for b in search_order_b:
            print("? B", b, flush=True)

            if int(input()) == 1:
                print("!", a + b)
            
                sys.exit()