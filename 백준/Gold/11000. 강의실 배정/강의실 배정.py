import sys
import heapq

# 입력 받기
n = int(sys.stdin.readline().strip())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 시작 시간을 기준으로 정렬
arr.sort()

# 최소 힙(우선순위 큐) 생성
heap = []

# 첫 번째 강의의 끝나는 시간을 힙에 추가
heapq.heappush(heap, arr[0][1])

# 강의 배정 시작
for i in range(1, n):
    start, end = arr[i]

    # 가장 빨리 끝나는 강의실이 현재 강의 시작 시간보다 작거나 같다면, 해당 강의실 사용 가능
    if heap[0] <= start:
        heapq.heappop(heap)  # 기존 강의 끝나는 시간 제거

    # 새 강의 끝나는 시간을 힙에 추가
    heapq.heappush(heap, end)

# 최종적으로 남아 있는 힙의 크기가 필요한 강의실 수
print(len(heap))