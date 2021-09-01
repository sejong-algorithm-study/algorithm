def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for item in puddles:
        x, y = item
        dp[y - 1][x - 1] = 'X'
    for i in range(n):
        for j in range(m):
            if i - 1 >= 0 and dp[i][j] != 'X' and dp[i - 1][j] != 'X':
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0 and dp[i][j] != 'X' and dp[i][j - 1] != 'X':
                dp[i][j] += dp[i][j - 1]
            if dp[i][j]!='X':
                dp[i][j] %= 1000000007 
            # for a in range(n):
            #     for b in range(m):
            #         print(dp[a][b], end=" ")
            #     print()
            # print()
            # print()

    answer = dp[n-1][m-1]
    return answer