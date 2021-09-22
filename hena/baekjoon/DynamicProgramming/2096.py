import sys
input = sys.stdin.readline

T = int(input()) -1
array_max = list(map(int, input().split()))
array_min = array_max[:]

for c in range(T):
    a, b, c = map(int, input().split())
    
    tmp1 = [a, b, c]
    tmp2 = [a, b, c]

    tmp1[0] = tmp1[0] + max(array_max[0], array_max[1])
    tmp1[1] = tmp1[1] + max(array_max[0], array_max[1], array_max[2])
    tmp1[2] = tmp1[2] + max(array_max[1], array_max[2])
    array_max = tmp1[:]
    # print(array_max)
    
    tmp2[0] = tmp2[0] + min(array_min[0], array_min[1])
    tmp2[1] = tmp2[1] + min(array_min[0], array_min[1], array_min[2])
    tmp2[2] = tmp2[2] + min(array_min[1], array_min[2])
    array_min = tmp2[:]
    # print(array_min)
print(max(array_max), min(array_min))