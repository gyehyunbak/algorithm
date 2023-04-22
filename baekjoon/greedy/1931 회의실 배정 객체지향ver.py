from operator import itemgetter

class MeetingScheduler:
    def __init__(self, n, meetings):
        self.n = n
        self.meetings = meetings
        self.reserved = -1
        self.count = 0

    def schedule_meetings(self):
        self.meetings.sort(key=itemgetter(1, 0))

        for start, end in self.meetings:
            if start >= self.reserved:
                self.reserved = end
                self.count += 1

        return self.count

def main():
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]

    meeting_scheduler = MeetingScheduler(n, meetings)
    count = meeting_scheduler.schedule_meetings()

    print(count)

if __name__ == "__main__":
    main()