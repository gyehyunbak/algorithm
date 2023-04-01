n = int(input())
p = list(map(int, input().split()))

p.sort()

current = 0
total = 0
for i in p:
    current += i
    total += current

print(total)