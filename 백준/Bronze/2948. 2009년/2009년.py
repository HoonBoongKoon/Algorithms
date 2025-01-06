date = ["Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday"]
day = [0, 31, 28, 31,30,31,30, 31, 31, 30, 31, 30, 31]
D,M = map(int, input().split())
All = 0
for i in range(0,M):
    All += day[i]
All += D
#1월 1일이 목요일
All = All % 7 -1
print(date[All])