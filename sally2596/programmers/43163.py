list =[]
def solution(begin, target, words):
    if target not in words:
        return 0
    else:

        visited = [0 for i in range(len(words))]
        for i in range(0, len(words), 1):

            if countDifferChar(begin, words[i]) == 1 and visited[i] == 0:
               dfs(words, i, visited, target, 1)

        return min(list)



def countDifferChar(begin, target):
    num = 0
    for i in range(0, len(begin), 1):
        if begin[i] != target[i]:
            num += 1
    return num


def dfs(words, index, visited, target, cnt):
    if words[index] == target:
        list.append(cnt)
        return

    for i in range(0, len(words), 1):
        if visited[i] == 0 and countDifferChar(words[index], words[i]) == 1:
            visited[i] = 1
            dfs(words, i, visited, target, cnt+1)
            visited[i] = 0


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log","cog"])
