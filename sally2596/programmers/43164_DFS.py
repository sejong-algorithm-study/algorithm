from operator import itemgetter
answer = []

def solution(tickets):
    used = [0 for i in range(len(tickets))]
    tickets.sort(key=itemgetter(0, 1))

    listofICN = list(filter(lambda x:tickets[x][0] =="ICN",range(len(tickets))))
    for i in listofICN:
        used[i] = 1
        answer.append(tickets[i][0])
        answer.append(tickets[i][1])
        num = dfs(tickets, used)
        if num == 0:
            used[i] = 0
            answer.pop()
            answer.pop()
        elif num == 1:
            return answer

def dfs(tickets,used):
    if 0 not in used:
        return 1
    for i in range(len(tickets)):
        if used[i]==0 and answer[-1]==tickets[i][0]:
            used[i]=1
            answer.append(tickets[i][1])
            num= dfs(tickets,used)
            if num ==0:
                used[i]=0
                answer.pop()
            elif num==1:
                return 1
    return 0
