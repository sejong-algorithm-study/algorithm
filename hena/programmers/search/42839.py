from itertools import permutations

def solution(numbers):
    number_list = set()
    answer = 0
    strlist = list(numbers)
    for i in range(1, len(strlist) + 1):
        for item in permutations(strlist, i):
            tmp = ""
            for index in item:
                tmp += "".join(index)
            number_list.add(int(tmp))
    number_list.discard(0)
    number_list.discard(1)
    for value in number_list:
        cnt = 0
        for i in range(2, value + 1):
            if i * i > value:
                break
            if value % i == 0:
                cnt += 1
        if cnt == 0:
            answer +=1
    
    
    return answer