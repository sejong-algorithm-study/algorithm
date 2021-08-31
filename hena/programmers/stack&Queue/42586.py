import math
def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(progresses)):
        queue.append(math.ceil( (100 - progresses[i])/speeds[i]))
    print(queue)

    
    while queue != []:
        val = queue.pop(0)#값 빼기
        if queue == []:
            answer.append(1)
            break
        cnt = 1
        while queue != []:
            if val >= queue[0]:
                queue.pop(0)
                cnt += 1
                if queue == []:
                    answer.append(cnt)
                    break
                
            else:
                answer.append(cnt)
                break
        print(queue)
        
    return answer