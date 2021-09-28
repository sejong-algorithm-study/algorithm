def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    start = 1
    end = distance

    while start<=end:
        mid = (start+end)//2
        destroy_rock = 0 #부신 돌의 개수
        prev_rock =0
        for i in rocks:
            if i-prev_rock<mid:
                destroy_rock+=1
            else:
                prev_rock = i

        #부셔진 돌이 n개일 경우 start거리(바위 간 거리)를 늘려서 한 번 더 시도해봄
        #한 번 더 시도했지만 부셔진 돌이 n보다 크면 마지막 end값이 최대값이 됨
        if destroy_rock > n:
            end  = mid-1
        else:
            start = mid+1
    return end
