# Chatgpt Platinum Problems
# Problem 2

# Prompt 1

def solve_haybales():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    haybales = list(map(int, data[1:N + 1]))
    Q = int(data[N + 1])
    queries = data[N + 2:]

    # Precompute prefix sums of haybales
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + haybales[i - 1]

    results = []
    for q in range(Q):
        l, r, x = map(int, queries[q * 3:q * 3 + 3])
        l -= 1  # Convert to 0-based index
        r -= 1  # Convert to 0-based index

        bessie_hay = x
        elsie_hay = 0

        # Simulate hay distribution
        for i in range(l, r + 1):
            if bessie_hay <= elsie_hay:
                bessie_hay += haybales[i]
            else:
                elsie_hay += haybales[i]

        results.append(bessie_hay - elsie_hay)

    sys.stdout.write("\n".join(map(str, results)) + "\n")


# Prompt 2


def solve_haybales():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    haybales = list(map(int, data[1:N + 1]))
    Q = int(data[N + 1])
    queries = data[N + 2:]

    # Precompute prefix sums and parity sums
    prefix_sum = [0] * (N + 1)
    parity_sum = [0] * (N + 1)
    bessie_total = 0
    elsie_total = 0

    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + haybales[i - 1]
        if bessie_total <= elsie_total:
            bessie_total += haybales[i - 1]
            parity_sum[i] = parity_sum[i - 1] + haybales[i - 1]
        else:
            elsie_total += haybales[i - 1]
            parity_sum[i] = parity_sum[i - 1] - haybales[i - 1]

    # Process queries
    results = []
    for q in range(Q):
        l, r, x = map(int, queries[q * 3:q * 3 + 3])

        # Adjust for 0-based indexing
        l -= 1

        # Total hay difference in range [l, r]
        range_diff = parity_sum[r] - parity_sum[l]

        # Adjust for starting difference x
        final_diff = x + range_diff

        results.append(final_diff)

    # Output results
    sys.stdout.write("\n".join(map(str, results)) + "\n")


# Prompt 3

def solve_haybales():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Input parsing
    N = int(data[0])  # Number of haybales
    haybales = list(map(int, data[1:N + 1]))  # Haybale sizes
    Q = int(data[N + 1])  # Number of queries
    queries = data[N + 2:]  # Query data

    # Precompute prefix sums and parity sums
    prefix_sum = [0] * (N + 1)
    parity_sum = [0] * (N + 1)
    bessie_total = 0
    elsie_total = 0

    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + haybales[i - 1]
        if bessie_total <= elsie_total:
            bessie_total += haybales[i - 1]
            parity_sum[i] = parity_sum[i - 1] + haybales[i - 1]
        else:
            elsie_total += haybales[i - 1]
            parity_sum[i] = parity_sum[i - 1] - haybales[i - 1]

    # Process queries
    results = []
    for q in range(Q):
        l, r, x = map(int, queries[q * 3:q * 3 + 3])

        # Adjust for 1-based indexing to 0-based
        l -= 1

        # Total hay difference in range [l, r]
        range_diff = parity_sum[r] - parity_sum[l]

        # Adjust for starting difference x
        final_diff = x + range_diff

        results.append(final_diff)

    # Output results
    sys.stdout.write("\n".join(map(str, results)) + "\n")





