def fair_split_haybales():
    n = int(input())
    haybales = list(map(int, input().split()))
    q = int(input())

    # Calculate prefix sum for Bessie and Elsie
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + haybales[i]

    for _ in range(q):
        l, r, x = map(int, input().split())
        bessie_sum = prefix_sum[r] - prefix_sum[l - 1]
        ellie_sum = (r - l + 1) - bessie_sum
        difference = bessie_sum + x - ellie_sum
        print(difference)

fair_split_haybales()