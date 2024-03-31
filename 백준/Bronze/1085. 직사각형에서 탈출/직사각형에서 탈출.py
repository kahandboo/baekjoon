x, y, w, h = map(int,input().split())

r = [ y , x , w - x , h - y ]
print(min(r))