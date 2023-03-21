coin_type = []
count = 0

n, k = map(int, input().split())

for i in range(n):
    coin_type.append(int(input()))

coin_type.sort(reverse= True)

for coin in coin_type:
    count += k // coin
    k %= coin

print(count)