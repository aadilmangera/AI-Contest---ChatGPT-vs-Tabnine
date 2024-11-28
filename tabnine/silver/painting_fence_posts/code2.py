def count_touches(N, P, fence_posts, cows):
    touches = [0] * P

    for cow in cows:
        x1, y1, x2, y2 = cow

        for i in range(P):
            x3, y3 = fence_posts[i]
            x4, y4 = fence_posts[(i + 1) % P]

            # Check if the starting and ending positions are on the same side of the fence segment
            if ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) * ((x4 - x3) * (y2 - y3) - (y4 - y3) * (x2 - x3)) >= 0:
                touches[i] += 1
                touches[(i + 1) % P] += 1
                break

    return touches

# Read input
N, P = map(int, input().split())
fence_posts = []
for _ in range(P):
    x, y = map(int, input().split())
    fence_posts.append((x, y))

cows = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    cows.append((x1, y1, x2, y2))

# Calculate touches
touches = count_touches(N, P, fence_posts, cows)

# Print output
for touch in touches:
    print(touch)