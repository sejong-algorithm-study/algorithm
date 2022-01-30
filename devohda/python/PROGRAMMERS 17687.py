def change_to_string(num, n):
    dic = 'ABCDEF'
    str_num = ""
    while num >= n:
        tmp = num % n
        if tmp < 10:
            str_num += str(tmp)
        else:
            str_num += dic[tmp - 10]
        num = num // n

    if num < 10:
        str_num += str(num)
    else:
        str_num += dic[num - 10]

    return str_num[::-1]


def solution(n, t, m, p):
    length = 0
    cnt = 0
    s = ""

    while length < m * (t - 1) + p:
        tmp = change_to_string(cnt, n)
        s += tmp
        cnt += 1
        length += len(tmp)

    # 정답 만들기
    answer = ''
    for i in range(t):
        answer += str(s[m * i + p - 1])

    return answer


print(solution(16, 16, 2, 1))
