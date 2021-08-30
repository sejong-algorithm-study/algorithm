# 가격이 떨어지지 않은 것으로 본다 => 떨어지는 순간까지 1초로 계산하겠다.
# 그 다음에 오르는 건 관게 없다!

def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        flag = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break

        answer.append(cnt)

    return answer
