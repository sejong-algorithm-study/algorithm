dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def search_blocks(board):
    blocks = []
    for x in range(len(board) - 1):
        for y in range(len(board[x]) - 1):

            flag = True
            cmp = board[x][y]
            for k in range(4):
                if not y + dy[k] < len(board[x + dx[k]]):
                    flag = False
                    break
                if cmp != board[x + dx[k]][y + dy[k]]:
                    flag = False
                    break

            if flag:
                blocks.append((x, y))

    return blocks


def pop_board(blocks, board):
    cnt = 0

    for x, y in blocks:
        for i in range(4):
            if board[x + dx[i]][y + dy[i]] != '@':
                board[x + dx[i]][y + dy[i]] = '@'
                cnt += 1

    for i in range(len(board)):
        board[i] = [k for k in board[i] if k != '@']

    return cnt, board


def solution(m, n, board):
    # 가로 세로 바꾸기고 뒤집기
    board2 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board2[i].append(board[j][i])
        board2[i].reverse()

    answer = 0

    while True:
        blocks = search_blocks(board2)
        cnt, board2 = pop_board(blocks, board2)

        if cnt == 0:
            return answer

        answer += cnt


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
