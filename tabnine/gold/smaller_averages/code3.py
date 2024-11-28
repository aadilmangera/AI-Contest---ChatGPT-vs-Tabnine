MOD = 10**9 + 7

def count_ways(N, A, B):
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1

    sum_A = [0] * (N+1)
    sum_B = [0] * (N+1)

    for i in range(1, N+1):
        sum_A[i] = sum_A[i-1] + A[i-1]
        for j in range(1, N+1):
            sum_B[j] = sum_B[j-1] + B[j-1]
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if sum_A[i] <= sum_B[j]:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

    return dp[N][N]

# Read input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Calculate and print the answer
print(count_ways(N, A, B))