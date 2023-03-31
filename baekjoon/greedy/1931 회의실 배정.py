from operator import itemgetter

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=itemgetter(1, 0))

reserved = -1
count = 0

for start, end in meetings:
    if start >= reserved:
        reserved = end
        count += 1

print(count)

# n = 11
# meetings = [(1, 4),(3, 5),(0, 6),(5, 7),(3, 8),(5, 9),(6, 10),(8, 11),(8, 12),(2, 13),(12, 14)]
