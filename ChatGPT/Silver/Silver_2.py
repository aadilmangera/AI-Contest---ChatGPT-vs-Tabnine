# Chatgpt Silver Problems
# Problem 2

# Prompt 1

from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    N, P = map(int, data[:2])
    index = 2
    posts = []
    for _ in range(P):
        x, y = map(int, data[index:index+2])
        posts.append((x, y))
        index += 2

    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Sort posts to construct the polygon
    posts = sorted(posts)
    left_side = sorted([p for p in posts if p[0] == posts[0][0]])
    right_side = sorted([p for p in posts if p[0] == posts[-1][0]], reverse=True)
    top_side = sorted([p for p in posts if p[1] == posts[-1][1] and posts[0][0] < p[0] < posts[-1][0]])
    bottom_side = sorted([p for p in posts if p[1] == posts[0][1] and posts[0][0] < p[0] < posts[-1][0]], reverse=True)

    ordered_posts = left_side + top_side + right_side + bottom_side

    # Map positions to indices
    post_indices = {post: i for i, post in enumerate(ordered_posts)}

    # Array to store touch counts
    touch_counts = [0] * P

    # Helper to calculate path distance
    def path_distance(start_idx, end_idx):
        if start_idx <= end_idx:
            return end_idx - start_idx
        return P - (start_idx - end_idx)

    # Process each cow's walk
    for (x1, y1), (x2, y2) in cows:
        if (x1, y1) == (x2, y2):
            continue
        start_idx = post_indices[(x1, y1)]
        end_idx = post_indices[(x2, y2)]

        # Shortest path
        clockwise_dist = path_distance(start_idx, end_idx)
        counterclockwise_dist = path_distance(end_idx, start_idx)

        if clockwise_dist < counterclockwise_dist:
            current_idx = start_idx
            while current_idx != end_idx:
                touch_counts[current_idx] += 1
                current_idx = (current_idx + 1) % P
            touch_counts[end_idx] += 1
        else:
            current_idx = start_idx
            while current_idx != end_idx:
                touch_counts[current_idx] += 1
                current_idx = (current_idx - 1 + P) % P
            touch_counts[end_idx] += 1

    # Print results
    print("\n".join(map(str, touch_counts)))
solve()


# Prompt 1 a

def solve():
    import sys
    from io import StringIO

    # Simulated input for debugging
    sys.stdin = StringIO("""5 4
3 1
1 5
3 5
1 1
2 1 1 5
1 5 3 4
3 1 3 5
2 1 2 1
3 2 3 3""")

    input = sys.stdin.read
    data = input().split()

    N, P = map(int, data[:2])
    index = 2
    posts = []
    for _ in range(P):
        x, y = map(int, data[index:index+2])
        posts.append((x, y))
        index += 2

    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Sort posts to construct the polygon
    posts = sorted(posts)
    left_side = sorted([p for p in posts if p[0] == posts[0][0]])
    right_side = sorted([p for p in posts if p[0] == posts[-1][0]], reverse=True)
    top_side = sorted([p for p in posts if p[1] == posts[-1][1] and posts[0][0] < p[0] < posts[-1][0]])
    bottom_side = sorted([p for p in posts if p[1] == posts[0][1] and posts[0][0] < p[0] < posts[-1][0]], reverse=True)

    ordered_posts = left_side + top_side + right_side + bottom_side

    # Map positions to indices
    post_indices = {post: i for i, post in enumerate(ordered_posts)}

    # Array to store touch counts
    touch_counts = [0] * P

    # Helper to calculate path distance
    def path_distance(start_idx, end_idx):
        if start_idx <= end_idx:
            return end_idx - start_idx
        return P - (start_idx - end_idx)

    # Process each cow's walk
    for (x1, y1), (x2, y2) in cows:
        if (x1, y1) == (x2, y2):
            continue
        start_idx = post_indices[(x1, y1)]
        end_idx = post_indices[(x2, y2)]

        # Shortest path
        clockwise_dist = path_distance(start_idx, end_idx)
        counterclockwise_dist = path_distance(end_idx, start_idx)

        if clockwise_dist < counterclockwise_dist:
            current_idx = start_idx
            while current_idx != end_idx:
                touch_counts[current_idx] += 1
                current_idx = (current_idx + 1) % P
            touch_counts[end_idx] += 1
        else:
            current_idx = start_idx
            while current_idx != end_idx:
                touch_counts[current_idx] += 1
                current_idx = (current_idx - 1 + P) % P
            touch_counts[end_idx] += 1

    # Print results
    print("\n".join(map(str, touch_counts)))

# Call the function
solve()



# Prompt 1 b

from collections import defaultdict

def solve():
    import sys
    from io import StringIO

    # Simulated input for debugging
    sys.stdin = StringIO("""5 4
3 1
1 5
3 5
1 1
2 1 1 5
1 5 3 4
3 1 3 5
2 1 2 1
3 2 3 3""")

    input = sys.stdin.read
    data = input().split()

    N, P = map(int, data[:2])
    index = 2
    posts = []
    for _ in range(P):
        x, y = map(int, data[index:index+2])
        posts.append((x, y))
        index += 2

    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Sort posts to construct the polygon
    posts = sorted(posts)
    left_side = sorted([p for p in posts if p[0] == posts[0][0]])
    right_side = sorted([p for p in posts if p[0] == posts[-1][0]], reverse=True)
    top_side = sorted([p for p in posts if p[1] == posts[-1][1] and posts[0][0] < p[0] < posts[-1][0]])
    bottom_side = sorted([p for p in posts if p[1] == posts[0][1] and posts[0][0] < p[0] < posts[-1][0]], reverse=True)

    ordered_posts = left_side + top_side + right_side + bottom_side

    # Map positions to indices
    post_indices = {post: i for i, post in enumerate(ordered_posts)}
    touch_counts = [0] * P

    # Helper function to compute path between two points
    def walk_and_count(start, end):
        start_idx = post_indices.get(start)
        end_idx = post_indices.get(end)

        if start_idx is None or end_idx is None:
            # If either point is not a vertex, we skip them
            return

        # Calculate path lengths
        clockwise_dist = (end_idx - start_idx + P) % P
        counterclockwise_dist = (start_idx - end_idx + P) % P

        # Walk the shortest path
        if clockwise_dist <= counterclockwise_dist:
            i = start_idx
            while i != end_idx:
                touch_counts[i] += 1
                i = (i + 1) % P
            touch_counts[end_idx] += 1
        else:
            i = start_idx
            while i != end_idx:
                touch_counts[i] += 1
                i = (i - 1 + P) % P
            touch_counts[end_idx] += 1

    # Process each cow's walk
    for (x1, y1), (x2, y2) in cows:
        walk_and_count((x1, y1), (x2, y2))

    # Print results
    print("\n".join(map(str, touch_counts)))

# Call the function
solve()



# Prompt 2

from collections import defaultdict

def solve():
    import sys
    from io import StringIO

    # Simulated input for debugging
    sys.stdin = StringIO("""5 4
3 1
1 5
3 5
1 1
2 1 1 5
1 5 3 4
3 1 3 5
2 1 2 1
3 2 3 3""")

    input = sys.stdin.read
    data = input().split()

    N, P = map(int, data[:2])
    index = 2
    posts = []
    for _ in range(P):
        x, y = map(int, data[index:index+2])
        posts.append((x, y))
        index += 2

    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Sort posts to construct the polygon
    posts = sorted(posts)
    left_side = sorted([p for p in posts if p[0] == posts[0][0]])
    right_side = sorted([p for p in posts if p[0] == posts[-1][0]], reverse=True)
    top_side = sorted([p for p in posts if p[1] == posts[-1][1] and posts[0][0] < p[0] < posts[-1][0]])
    bottom_side = sorted([p for p in posts if p[1] == posts[0][1] and posts[0][0] < p[0] < posts[-1][0]], reverse=True)

    ordered_posts = left_side + top_side + right_side + bottom_side

    # Map positions to indices
    post_indices = {post: i for i, post in enumerate(ordered_posts)}
    touch_counts = [0] * P

    # Create edges from ordered posts
    edges = []
    for i in range(P):
        edges.append((ordered_posts[i], ordered_posts[(i + 1) % P]))

    # Helper to find the index of a point on an edge
    def find_index(point):
        if point in post_indices:
            return post_indices[point]
        for i, (start, end) in enumerate(edges):
            if start[0] == end[0]:  # Vertical edge
                if start[0] == point[0] and min(start[1], end[1]) <= point[1] <= max(start[1], end[1]):
                    return i
            elif start[1] == end[1]:  # Horizontal edge
                if start[1] == point[1] and min(start[0], end[0]) <= point[0] <= max(start[0], end[0]):
                    return i
        return None

    # Helper to walk along the polygon
    def walk_and_count(start, end):
        start_idx = find_index(start)
        end_idx = find_index(end)

        if start_idx is None or end_idx is None:
            return

        # Calculate path lengths
        clockwise_dist = (end_idx - start_idx + P) % P
        counterclockwise_dist = (start_idx - end_idx + P) % P

        # Walk the shortest path
        if clockwise_dist <= counterclockwise_dist:
            i = start_idx
            while i != end_idx:
                touch_counts[i] += 1
                i = (i + 1) % P
            touch_counts[end_idx] += 1
        else:
            i = start_idx
            while i != end_idx:
                touch_counts[i] += 1
                i = (i - 1 + P) % P
            touch_counts[end_idx] += 1

    # Process each cow's walk
    for (x1, y1), (x2, y2) in cows:
        walk_and_count((x1, y1), (x2, y2))

    # Print results
    print("\n".join(map(str, touch_counts)))

# Call the function
solve()


# Prompt 3

from collections import defaultdict

def solve():
    import sys
    from io import StringIO

    # Simulated input for debugging
    sys.stdin = StringIO("""5 4
3 1
1 5
3 5
1 1
2 1 1 5
1 5 3 4
3 1 3 5
2 1 2 1
3 2 3 3""")

    input = sys.stdin.read
    data = input().split()

    N, P = map(int, data[:2])
    index = 2
    posts = []
    for _ in range(P):
        x, y = map(int, data[index:index+2])
        posts.append((x, y))
        index += 2

    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Sort posts to construct the polygon
    posts = sorted(posts)
    left_side = sorted([p for p in posts if p[0] == posts[0][0]])
    right_side = sorted([p for p in posts if p[0] == posts[-1][0]], reverse=True)
    top_side = sorted([p for p in posts if p[1] == posts[-1][1] and posts[0][0] < p[0] < posts[-1][0]])
    bottom_side = sorted([p for p in posts if p[1] == posts[0][1] and posts[0][0] < p[0] < posts[-1][0]], reverse=True)

    ordered_posts = left_side + top_side + right_side + bottom_side

    # Map positions to indices
    post_indices = {post: i for i, post in enumerate(ordered_posts)}
    touch_counts = [0] * P

    # Helper to calculate shortest path
    def shortest_path(start_idx, end_idx):
        if start_idx <= end_idx:
            return list(range(start_idx, end_idx + 1))
        else:
            return list(range(start_idx, P)) + list(range(0, end_idx + 1))

    # Process each cow's walk
    for (x1, y1), (x2, y2) in cows:
        if (x1, y1) not in post_indices or (x2, y2) not in post_indices:
            continue  # Skip invalid points
        start_idx = post_indices[(x1, y1)]
        end_idx = post_indices[(x2, y2)]

        # Determine clockwise and counterclockwise paths
        clockwise = shortest_path(start_idx, end_idx)
        counterclockwise = shortest_path(end_idx, start_idx)

        # Select the shorter path
        if len(clockwise) <= len(counterclockwise):
            path = clockwise
        else:
            path = counterclockwise

        # Increment touch counts
        for idx in path:
            touch_counts[idx] += 1

    # Print results
    print("\n".join(map(str, touch_counts)))

# Call the function
solve()






