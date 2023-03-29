meetings = []
reserved = []
count = 0

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    meetings.append((x,y))

# 준비 단계

shortest = meetings[0]
shortest_time = meetings[0][1] - meetings[0][0]

while(meetings):

    # 제일 시간이 짧은 미팅 찾기

    for meeting in meetings:
        if  meeting[1] - meeting[0] < shortest_time:
            shortest = meeting
            shortest_time = meeting[1] - meeting[0]

    # 더 넣을게 있을때


# 제일 시간이 짧은 미팅 count += 1
# 제일 짧은 미팅과 시간이 겹치지 않는 미팅 count += 1
# 더 이상 겹치지 않는 미팅이 없을 때까지