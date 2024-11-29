# Chatgpt Gold Problems
# Problem 3

# Prompt 1

MOD = 10**9 + 7

def count_valid_splits(N, a, b):
    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: 0 splits

    # Fill DP table
    for k in range(1, N + 1):  # Number of subarrays
        for j in range(1, N + 1):  # Consider splitting at position j
            for i in range(1, j + 1):  # Consider subarray starting from i
                if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                    dp[k][j] = (dp[k][j] + dp[k - 1][i - 1]) % MOD

    # Sum over all ways to split into k subarrays
    result = sum(dp[k][N] for k in range(1, N + 1)) % MOD
    return result

# Input processing
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    b = list(map(int, data[N+1:]))
    print(count_valid_splits(N, a, b))


# Prompt 1 a


MOD = 10**9 + 7

def count_valid_splits(N, a, b):
    # Compute prefix sums for both arrays
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # DP table: dp[j] is the number of ways to split the first j elements
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: no elements to split

    # Iterate over the positions to split
    for j in range(1, N + 1):
        temp = [0] * (N + 1)
        for i in range(1, j + 1):
            # Check validity of the subarray [i, j]
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                temp[j] += dp[i - 1]
                temp[j] %= MOD
        dp = temp

    # Sum all valid splits
    result = sum(dp) % MOD
    return result

# Input handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    # Test Case
    N = 2
    a = [1, 2]
    b = [2, 2]

    print(count_valid_splits(N, a, b))  # Expected Output: 2


# Prompt 2

MOD = 10**9 + 7

def count_valid_splits(N, a, b):
    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):
        dp_j = 0  # Temporary sum for dp[j]
        for i in range(1, j + 1):
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))
    print(count_valid_splits(N, a, b))



# Prompt 2a


MOD = 10**9 + 7

def count_valid_splits(N, a, b):
    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):
        dp_j = 0  # Temporary sum for dp[j]
        for i in range(1, j + 1):
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
# Simulated input for debugging
    data = [
        "2",       # N
        "1 2",     # Array a
        "2 2"      # Array b
    ]

    N = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))

    print(count_valid_splits(N, a, b))



# Test more cases


MOD = 10**9 + 7

def count_valid_splits(N, a, b):
    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):
        dp_j = 0  # Temporary sum for dp[j]
        for i in range(1, j + 1):
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
# Simulated input for debugging
    data = [
        "3",       # N
        "1 3 2",     # Array a
        "2 2 2"      # Array b
    ]

    N = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))

    print(count_valid_splits(N, a, b))


# Prompt 3


MOD = 10**9 + 7

def count_valid_splits(N, a, b):
    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):  # Iterate over possible end points
        dp_j = 0
        for i in range(1, j + 1):  # Iterate over possible start points
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))
    print(count_valid_splits(N, a, b))



# Prompt 3a

def count_valid_splits(N, a, b):
    MOD = 10**9 + 7

    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):  # Iterate over possible end points
        dp_j = 0
        for i in range(1, j + 1):  # Iterate over possible start points
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
    import sys

    try:
        # For testing manually, uncomment this section:
        # Simulated input:
        data = [
            "3",       # N
            "1 3 2",   # Array a
            "2 2 2"    # Array b
        ]

        # Uncomment this for competitive programming environments:
        # input = sys.stdin.read
        # data = input().splitlines()

        print(f"Input data: {data}")  # Debugging input

        N = int(data[0].strip())
        a = list(map(int, data[1].strip().split()))
        b = list(map(int, data[2].strip().split()))

        print(count_valid_splits(N, a, b))
    except IndexError:
        print("Error: Input data is not properly formatted.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Test more cases


def count_valid_splits(N, a, b):
    MOD = 10**9 + 7

    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):  # Iterate over possible end points
        dp_j = 0
        for i in range(1, j + 1):  # Iterate over possible start points
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
    import sys

    try:
        # For testing manually, uncomment this section:
        # Simulated input:
        data = [
            "2",       # N
            "1 2",   # Array a
            "2 2"    # Array b
        ]

        # Uncomment this for competitive programming environments:
        # input = sys.stdin.read
        # data = input().splitlines()

        print(f"Input data: {data}")  # Debugging input

        N = int(data[0].strip())
        a = list(map(int, data[1].strip().split()))
        b = list(map(int, data[2].strip().split()))

        print(count_valid_splits(N, a, b))
    except IndexError:
        print("Error: Input data is not properly formatted.")
    except Exception as e:
        print(f"Unexpected error: {e}")




def count_valid_splits(N, a, b):
    MOD = 10**9 + 7

    # Compute prefix sums
    prefix_a = [0] * (N + 1)
    prefix_b = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_a[i] = prefix_a[i - 1] + a[i - 1]
        prefix_b[i] = prefix_b[i - 1] + b[i - 1]

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to split 0 elements

    # Fill DP table
    for j in range(1, N + 1):  # Iterate over possible end points
        dp_j = 0
        for i in range(1, j + 1):  # Iterate over possible start points
            if prefix_a[j] - prefix_a[i - 1] <= prefix_b[j] - prefix_b[i - 1]:
                dp_j = (dp_j + dp[i - 1]) % MOD
        dp[j] = dp_j

    # The result is dp[N], the number of ways to split the first N elements
    return dp[N]

# Input processing
if __name__ == "__main__":
    import sys

    try:
        # For testing manually, uncomment this section:
        # Simulated input:
        data = [
            "5",       # N
            "2 5 1 3 2",   # Array a
            "2 1 5 2 2"    # Array b
        ]

        # Uncomment this for competitive programming environments:
        # input = sys.stdin.read
        # data = input().splitlines()

        print(f"Input data: {data}")  # Debugging input

        N = int(data[0].strip())
        a = list(map(int, data[1].strip().split()))
        b = list(map(int, data[2].strip().split()))

        print(count_valid_splits(N, a, b))
    except IndexError:
        print("Error: Input data is not properly formatted.")
    except Exception as e:
        print(f"Unexpected error: {e}")








