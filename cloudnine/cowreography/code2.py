def min_moves(N, K, first, last):
    dp = [[float('inf')] * N for _ in range(N)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(N):
            if first[i] == last[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                if i >= K and j >= K and first[i] != last[j]:
                    dp[i][j] = min(dp[i][j], dp[i-K][j-K] + 1)

    return dp[N-1][N-1]

N, K = 4, 1
first = '0111'
last = '1110'

min_moves(N, K, first, last)