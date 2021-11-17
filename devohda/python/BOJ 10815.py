N = int(input())
check = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
check.sort()


def is_in_card(n, start_idx, end_idx):
    if start_idx > end_idx:
        return 0
    mid = (start_idx + end_idx) // 2
    if n == check[mid]:
        return 1
    elif n > check[mid]:
        return is_in_card(n, mid + 1, end_idx)
    else:
        return is_in_card(n, start_idx, mid - 1)


for num in nums:
    print(is_in_card(num, 0, N - 1), end=" ")
