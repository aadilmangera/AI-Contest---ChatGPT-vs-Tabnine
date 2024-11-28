def count_touches(N, P, fence_posts, cows):
    touches = [0] * P

    for cow in cows:
        x1, y1, x2, y2 = cow

        for i in range(P):
            x3, y3 = fence_posts[i]
            x4, y4 = fence_posts[(i + 1) % P]

            # Calculate the direction of the cow's walk around the fence
            cross_product = (x4 - x3) * (y2 - y1) - (y4 - y3) * (x2 - x1)

            # Check if the starting and ending positions are on the same side of the fence segment
            if cross_product == 0:
                touches[i] += 1
                touches[(i + 1) % P] += 1
                break
            elif cross_product > 0:
                if (x3 - x1) * (y4 - y1) - (y3 - y1) * (x4 - x1) > 0 and (x3 - x2) * (y4 - y2) - (y3 - y2) * (x4 - x2) > 0:
                    touches[i] += 1
                    touches[(i + 1) % P] += 1
                    break
            else:
                if (x3 - x1) * (y4 - y1) - (y3 - y1) * (x4 - x1) < 0 and (x3 - x2) * (y4 - y2) - (y3 - y2) * (x4 - x2) < 0:
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