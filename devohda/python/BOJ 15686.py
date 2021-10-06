from itertools import combinations

n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

arr = list(combinations(chicken, m))
dist = [0] * len(arr)

for i in home:
    for j in range(len(arr)):
        a = 100
        for k in arr[j]:
            temp = abs(i[1] - k[1]) + abs(i[0] - k[0])
            a = min(a, temp)
        dist[j] += a

print(min(dist))
