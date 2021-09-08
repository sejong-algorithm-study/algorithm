def soulution(F, S, G, U, D):
    que = []
    visited = [0] * (F + 1)
    que.append([S,0])
    visited[S] = 1

    if S == G:
        return 0
    else:
        while len(que)!=0:
            current = que.pop(0)
            if current[0]==G:
                return current[1]
            if current[0] + U <= F and visited[current[0] + U] == 0:
                que.append([current[0]+U,current[1]+1])
                visited[current[0]+U] = 1

            if current[0] - D > 0 and visited[current[0] - D] == 0:
                que.append([current[0]-D,current[1]+1])
                visited[current[0]-D] = 1

        return "use the stairs"



F, S, G, U, D = input().split(" ")

print(soulution(int(F), int(S), int(G), int(U), int(D)))
