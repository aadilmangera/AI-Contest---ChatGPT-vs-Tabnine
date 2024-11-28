import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_cow_distance(fence, cow):
    start_x, start_y, end_x, end_y = cow
    dist1 = 0
    dist2 = 0
    for i in range(len(fence)):
        x1, y1 = fence[i]
        x2, y2 = fence[(i + 1) % len(fence)]
        if (x1 == x2 and start_x == x1 and min(y1, y2) <= start_y <= max(y1, y2)) or \
           (y1 == y2 and start_y == y1 and min(x1, x2) <= start_x <= max(x1, x2)):
            dist1 += distance(start_x, start_y, x2, y2)
            start_x, start_y = x2, y2
        elif (x1 == x2 and end_x == x1 and min(y1, y2) <= end_y <= max(y1, y2)) or \
             (y1 == y2 and end_y == y1 and min(x1, x2) <= end_x <= max(x1, x2)):
            dist2 += distance(start_x, start_y, x2, y2)
            start_x, start_y = x2, y2
        else:
            dist1 += distance(x1, y1, x2, y2)
            dist2 += distance(x1, y1, x2, y2)
    return min(dist1, dist2)

n, p = map(int, input().split())
fence = []
for _ in range(p):
    x, y = map(int, input().split())
    fence.append((x, y))
cows = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    cows.append((x1, y1, x2, y2))

for cow in cows:
    print(calculate_cow_distance(fence, cow))