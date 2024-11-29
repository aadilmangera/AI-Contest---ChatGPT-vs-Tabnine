# Chatgpt Silver Problems
# Problem 3

# Prompt 1


def count_winning_gene_candidates(N, S):
    result = [0] * (N + 1)

    # Iterate over all possible (K, L) pairs
    for K in range(1, N + 1):  # K: length of k-mers
        for L in range(1, K + 1):  # L: length of l-mers
            # To store positions of the lexicographically minimal substrings
            positions = set()

            # Iterate over all K-mers
            for i in range(N - K + 1):
                k_mer = S[i:i + K]
                # Find the lexicographically smallest L-mer within the K-mer
                min_l_mer = None
                min_l_index = None
                for j in range(K - L + 1):
                    l_mer = k_mer[j:j + L]
                    if min_l_mer is None or l_mer < min_l_mer:
                        min_l_mer = l_mer
                        min_l_index = i + j  # Position in original string
                # Add the position of the smallest L-mer to the set
                positions.add(min_l_index)

            # Update the result based on the size of the set
            result[len(positions)] += 1

    # Print the results for |P| = 1 to N
    for v in range(1, N + 1):
        print(result[v])

# Input reading
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
S = data[1]

# Run the function
count_winning_gene_candidates(N, S)


# Prompt 1 a


def count_winning_gene_candidates(N, S):
    # Result array to store counts for each |P| = v (v ranges from 1 to N)
    result = [0] * (N + 1)

    # Iterate over all possible (K, L) pairs
    for K in range(1, N + 1):  # K: length of k-mers
        for L in range(1, K + 1):  # L: length of l-mers
            # Set to track unique starting indices of minimal substrings
            positions = set()

            # Iterate over all K-mers
            for i in range(N - K + 1):  # Start of the K-mer in S
                k_mer = S[i:i + K]

                # Find the lexicographically smallest L-mer in this K-mer
                min_l_mer = None
                min_l_index = None
                for j in range(K - L + 1):  # Start of the L-mer in K-mer
                    l_mer = k_mer[j:j + L]
                    if min_l_mer is None or l_mer < min_l_mer:
                        min_l_mer = l_mer
                        min_l_index = i + j  # Position in original string

                # Add the position of the minimal L-mer to the set
                positions.add(min_l_index)

            # Update the result array based on the size of the set
            result[len(positions)] += 1

    # Print the results for |P| = 1 to N
    for v in range(1, N + 1):
        print(result[v])


# Simulated input for testing
data = [
    "8",      # Length of the string
    "AGTCAACG"  # The string S
]
N = int(data[0])
S = data[1]

# Run the function
count_winning_gene_candidates(N, S)



# Test More Cases


def count_winning_gene_candidates(N, S):
    # Result array to store counts for each |P| = v (v ranges from 1 to N)
    result = [0] * (N + 1)

    # Iterate over all possible (K, L) pairs
    for K in range(1, N + 1):  # K: length of k-mers
        for L in range(1, K + 1):  # L: length of l-mers
            # Set to track unique starting indices of minimal substrings
            positions = set()

            # Iterate over all K-mers
            for i in range(N - K + 1):  # Start of the K-mer in S
                k_mer = S[i:i + K]

                # Find the lexicographically smallest L-mer in this K-mer
                min_l_mer = None
                min_l_index = None
                for j in range(K - L + 1):  # Start of the L-mer in K-mer
                    l_mer = k_mer[j:j + L]
                    if min_l_mer is None or l_mer < min_l_mer:
                        min_l_mer = l_mer
                        min_l_index = i + j  # Position in original string

                # Add the position of the minimal L-mer to the set
                positions.add(min_l_index)

            # Update the result array based on the size of the set
            result[len(positions)] += 1

    # Print the results for |P| = 1 to N
    for v in range(1, N + 1):
        print(result[v])


# Simulated input for testing
data = [
    "100",      # Length of the string
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  # The string S
]
N = int(data[0])
S = data[1]

# Run the function
count_winning_gene_candidates(N, S)
















