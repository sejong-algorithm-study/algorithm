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

comb = list(combinations(chicken, m))
dist = [0] * len(comb)

for x1, y1 in home:
    for chicken_shop in comb:
        m = 100
        for x2, y2 in chicken_shop:
            d = abs(x1 - x2) + abs(y1 - y2)
            m = min(m, d)
        dist[j] += m

print(min(dist))
