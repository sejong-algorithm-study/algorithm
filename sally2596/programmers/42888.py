def solution(record):
    answer = []
    id_order = []
    ids = {}
    for i in record:
        arr = list(map(str,i.split(" ")))
        if arr[0]=="Enter":
            answer.append("님이 들어왔습니다.")
            ids[arr[1]] = arr[2]
        elif arr[0]=="Leave":
            answer.append("님이 나갔습니다.")
        else:
            ids[arr[1]] = arr[2]
        if arr[0] !="Change":
            id_order.append(arr[1])
    for i in range(len(id_order)):
        answer[i]=ids[id_order[i]]+answer[i]
    return answer