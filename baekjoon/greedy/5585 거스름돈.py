n = 1000 - int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += n // coin      # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 화폐의 종류 K만큼 반복 수행 -> O(K)
# 시간복잡도는 거슬러 줘야하는 금액의 크기(n)과는 무관