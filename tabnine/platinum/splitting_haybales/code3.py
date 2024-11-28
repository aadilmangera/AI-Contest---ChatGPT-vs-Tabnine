def fair_split_haybales():
    n = int(input())
    haybales = list(map(int, input().split()))
    q = int(input())

    # Calculate prefix sum for Bessie and Elsie
    bessie_prefix_sum = [0] * (n + 1)
    ellie_prefix_sum = [0] * (n + 1)
    for i in range(n):
        bessie_prefix_sum[i + 1] = bessie_prefix_sum[i] - haybales[i]
        ellie_prefix_sum[i + 1] = ellie_prefix_sum[i] + haybales[i]

    for _ in range(q):
        l, r, x = map(int, input().split())
        bessie_sum = bessie_prefix_sum[l - 1] - bessie_prefix_sum[r]
        ellie_sum = ellie_prefix_sum[r] - ellie_prefix_sum[l - 1]
        difference = bessie_sum + x - ellie_sum
        print(difference)

fair_split_haybales()