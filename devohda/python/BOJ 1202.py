import heapq

N, K = map(int, input().split())

# 보석 정보
jewel = []
for _ in range(N):
    heapq.heappush(jewel, list(map(int, input().split())))

# 가방 정보
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()


answer = 0
tmp = []
for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jewel:
        break

print(answer)
