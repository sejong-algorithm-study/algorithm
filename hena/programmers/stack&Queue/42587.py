def solution(priorities, location):
    array = priorities
    answer = 1
    while array != []:
        value = array[0]
        if value < max(array):
            array.pop(0)
            array.append(value)
            location = (location - 1)%len(array)
            print(location)
        else:
            array.pop(0)
            if location == 0:
                break
            location = (location - 1)%len(array)
            answer += 1
    return answer