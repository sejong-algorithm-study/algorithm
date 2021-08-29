#  프로그래머스 스택/큐 - 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 주어진 truck_weights 배열의 앞에서부터 순서대로 트럭이 다리에 올라감.
    # 다리에 있는 트럭과 주어진 트럭을 queue 를 사용하여 만듦

    # 다리에 올라갈 수 있는 무게 한계가 있으며, 다리의 길이보다 많은 트럭이 올라갈 수 없음
    # 즉, 다음 트럭이 올라가기 위해 무게, 길이 조건 2개를 모두 만족시켜야 함.

    # 다리에 있는 트럭은 다리 길이만큼의 시간이 지나면 다리를 모두 건너게 됨
    # 즉, 시간이 지남을 확인해서 큐에서 pop 시켜야 함.
    cnt = 0
    bridge_weight = 0
    trucks = deque(truck_weights)
    bridge = deque([])

    while True:
        cnt += 1

        # 맨 앞에 있는 트럭이 다 건넜는지 확인 후 큐에서 pop
        if len(bridge) != 0:
            if bridge_length + bridge[0]['cnt'] == cnt:
                bridge_weight -= bridge[0]['truck']
                bridge.popleft()

        # 올라간 트럭 개수가 다리의 전체 길이보다 작고, 다음 대기하는 트럭이 올라갔을 때도 다리가 하중을 견딜 수 있으면(길이, 무게 조건)
        # 주어진 트럭 큐에서 pop 해서 다리를 건너게 함.
        if len(trucks) != 0:
            if bridge_weight + trucks[0] <= weight and len(bridge) < bridge_length:
                bridge_weight += trucks[0]
                truck = trucks.popleft()
                bridge.append({'truck': truck, 'cnt': cnt})

        # 모든 트럭이 다리를 건넜으면 시간 count 종료
        if len(bridge) == 0:
            break

    return cnt

