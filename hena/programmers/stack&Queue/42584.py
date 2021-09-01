from collections import deque
def solution(prices):
    # print(prices)
    prices = deque(prices[:])
    # print(prices)
    
    answer = []
    while prices:
        val = prices.popleft()
        cnt = 0
        for item in prices:
            cnt += 1
            if val > item:
                break 
        answer.append(cnt)
#     length = len(prices)
#     for i in range(length):
#         cnt = 0
#         for j in range(i + 1, length):
#             cnt += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(cnt)
#             # print(answer)
    
    return answer