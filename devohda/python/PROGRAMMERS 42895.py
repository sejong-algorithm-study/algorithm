from collections import deque


def solution(N, number):
    dic = {}
    N_arr = []
    for i in range(1, 9):
        if number == int(str(N) * i):
            return i
        N_str = int(str(N) * i)
        dic[N_str] = i
        N_arr.append(N_str)

    arr = deque([N])
    repeat = N

    while arr:
        n = arr.popleft()
        cnt = dic[n] + 1

        if n == repeat and cnt < 8:
            repeat = repeat * 10 + N
            arr.append(repeat)

        for p in N_arr:
            add_N = n + p
            sub1_N = n - p
            sub2_N = p - n
            mul_N = n * p
            div1_N = n // p
            div2_N = 0
            if n != 0:
                div2_N = p // n

            for k in [add_N, sub1_N, sub2_N, mul_N, div1_N, div2_N]:
                if k == number:
                    return cnt

                if k not in dic:
                    dic[k] = cnt
                    if cnt < 8:
                        arr.append(k)

print(solution(1, 1122))
