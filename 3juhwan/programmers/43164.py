def solution(tickets):
    answer = []

    road = {}
    for i, ticket in enumerate(tickets):
        if ticket[0] in road:
            road[ticket[0]].append((ticket[1], i))
        else:
            road[ticket[0]] = [(ticket[1], i)]

    visited = [0] * len(tickets)

    def dfs(ways):
        nonlocal answer

        if len(ways) == len(tickets) + 1 and 0 not in visited:
            if not answer:
                answer = ways

        end = ways[-1]
        if end in road:
            for way, i in sorted(road[end]):
                if not visited[i]:
                    visited[i] = 1
                    dfs(ways + [way])
                    visited[i] = 0

    dfs(['ICN'])

    return answer