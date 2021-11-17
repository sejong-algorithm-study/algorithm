def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid+1
        elif arr[mid] > target:
            high = mid-1
    return 0

n = int(input())
_card = list(map(int, input().split()))
m = int(input())
_data = list(map(int, input().split()))

_card.sort()
_output = []
for x in _data:
    _output.append(binary_search(_card, x))
print(*_output)