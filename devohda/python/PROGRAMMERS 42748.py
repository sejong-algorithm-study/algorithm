def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_arr = array[i - 1:j]
        new_arr.sort()
        answer.append(new_arr[k - 1])

    return answer

# 해당 코드로 풀었지만 ramda 를 사용한 코드를 보고 고쳐볼 예정
