def dfs(start_city, visited, tickets, answer=[]):
    answer2 = answer[:]
    answer2.append(start_city)

    for i in range(len(tickets)):
        if visited[i]:
            continue

        if start_city == tickets[i][0]:
            visited_copy = visited[:]
            visited_copy[i] = True
            answer3 = dfs(tickets[i][1], visited_copy, tickets, answer2)
            if len(answer3) == len(visited) + 1:
                return answer3

    return answer2


def solution(tickets):
    tickets.sort()
    v = [False] * len(tickets)

    return dfs('ICN', v, tickets)