def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 주어진 다리 길이만큼 생성
    bridge = [0] * bridge_length
    # print(bridge)

    # 다리가 없어질 때 까지 반복
    while bridge != []:
        # 매번 1초 증가
        answer += 1

        # 첫 번째 값을 제외
        bridge.pop(0)

        # 트럭이 남아있다면?
        if truck_weights != []:
            # 첫 번째 값을 빼오기
            val = truck_weights[0]

            # 다리에 있는 트럭들의 값과 지금 막 들어가려는 트럭의 무게가 다리 중량보다 크다면 다리에 0인 트럭을 채운다
            if sum(bridge) + val > weight:
                bridge.append(0)
            # 반대의 경우 트럭을 다리에 올린다
            else:
                bridge.append(val)
                truck_weights.pop(0)
        # print(bridge)
    
    return answer