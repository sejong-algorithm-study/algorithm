N = int(input())
water = list(map(int, input().split()))
water.sort()

value = 2000000001
start_idx = 0
end_idx = N - 1
answer = [water[start_idx], water[end_idx]]

while start_idx < end_idx:
    add_value = water[start_idx] + water[end_idx]
    abs_value = abs(add_value - 0)

    if add_value == 0:
        answer = [water[start_idx], water[end_idx]]
        break

    if abs_value < value:
        answer = [water[start_idx], water[end_idx]]
        value = abs_value

    if 0 < add_value:
        end_idx -= 1
    else:
        start_idx += 1

print(answer[0], answer[1])
