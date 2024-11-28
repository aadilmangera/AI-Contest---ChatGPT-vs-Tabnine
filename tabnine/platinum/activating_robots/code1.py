def is_possible(time):
    robots = [0] * (R - 1)
    robots[0] = L / R

    for i in range(1, R - 1):
        robots[i] = robots[i - 1] + L / R

    for activation in activations:
        for i in range(R - 1):
            if activation >= robots[i] and activation <= robots[i] + time * K:
                robots[i] = activation + L / R
                break

    return all(robots[i] - robots[i - 1] <= time * K for i in range(1, R - 1))

(L, R, N, K) = map(int, input().split())
activations = list(map(int, input().split()))

left = 0
right = L / R

while right - left > 1e-9:
    mid = (left + right) / 2
    if is_possible(mid):
        right = mid
    else:
        left = mid

print(right)