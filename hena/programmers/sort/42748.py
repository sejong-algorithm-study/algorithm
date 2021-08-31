def solution(array, commands):
    answer = []
    for item in commands:
        i, j, k = item
        # print(i,j,k)
        split_array = array[i - 1:j]
        # print(split_array)
        split_array.sort()
        answer.append(split_array[k - 1])
    
    return answer