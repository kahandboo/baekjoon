word = []

for _ in range(int(input())):
    word.append(input())

word = list(set(word))

word.sort(key = lambda x: (len(x),x))

for i in word:
    print(i)