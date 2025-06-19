import math
def solution(brown, yellow):
    colorsum = brown+yellow
    for height in range(3, math.floor(colorsum**0.5) + 1):
        width = colorsum // height
        if (width-2) * (height-2) == yellow:
            answer = [width, height]
            return answer