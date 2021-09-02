from itertools import permutations

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    # for i in range(len(numbers)):
    #     # print(numbers[i]*3)
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    # print(numbers)
    
    
    answer = str(int("".join(i for i in numbers)))
    # print(answer)
    
#     result = list(permutations(numbers, len(numbers)))
#     result = [''.join(map(str, i)) for i in result] 
    
#     answer = max(result)
    
    # 시간 초과
    # tmp = []
    # for i in numbers:
    #     tmp.append(str(i))
    # result = list(permutations(tmp, len(tmp)))
    # test = []
    # for i in range(len(result)):
    #     test.append([])
    #     string = ""
    #     for j in result[i]:
    #         string += j
    #     test[i].append(string)
    # test.sort(reverse=True)
    # answer = ",".join(test[0])
    
    return answer