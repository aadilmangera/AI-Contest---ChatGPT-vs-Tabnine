def count_winning_genes(N, S):
    result = []
    for K in range(1, N + 1):
        for L in range(1, K + 1):
            positions = set()
            for i in range(N - K + 1):
                substring = S[i:i + K]
                min_substring = substring[:L]
                for j in range(i + K - L + 1):
                    if substring[j:j + L] < min_substring:
                        min_substring = substring[j:j + L]
                positions.add(substring.index(min_substring))
            result.append(len(positions))
    return result

N = 8
S = 'AGTCAACG'
results = count_winning_genes(N, S)
for v in results:
    print(v)