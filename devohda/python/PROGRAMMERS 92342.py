def solution(n, info):
    answer = []
    score_price = []

    for i in range(11):
        score = 10 - i
        if not info[i]:
            score_price.append((score, info[i] + 1))
        else:
            score_price.append((score * 2, info[i] + 1))

    # 적은 가격, 고효율
    score_price.sort(key=lambda x: (x[1], 10 - x[0]))
    print("n =", n)
    print(score_price)

    return answer