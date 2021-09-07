def DFS(ticket, tickets, visited, answer):
    print(visited)
    if visited == [True] * len(tickets):
        answer.append(ticket[1])
        # print("마지막",answer)
        return answer, True
    for index, port in enumerate(tickets):
        if not visited[index] and port[0] == ticket[1]:
            visited[index] = True
            answer.append(port[0])
            # print("in",answer)
            return_val = DFS(port, tickets, visited, answer)
            if return_val[1] == True:
                return return_val
            else:
                answer.pop()
                visited[index] = False
    # print("여기")
    return 0, False
def solution(tickets):
    array = []
    for index, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            array.append(ticket)
    print(array)
    for i in range(len(array)):
        del tickets[tickets.index(array[i])]
    array.sort(key=lambda x: x[1], reverse =True)
    tickets.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(array)):
        tickets.insert(0, array[i])
    # print(tickets)
    # print(tickets)
    for index, ticket in enumerate(tickets):
        # if ticket[0] == 'ICN':
        answer = []
        visited = [False] * len(tickets)
        visited[index] = True
        answer.append(ticket[0])
        # print(answer)
        answer, return_value = DFS(ticket, tickets, visited,answer)
        visited[index] = False

        if return_value == 1:
            return answer