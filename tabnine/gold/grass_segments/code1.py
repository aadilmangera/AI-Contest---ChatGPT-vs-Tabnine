class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, index, left, right, start, end, value):
        if right < start or end < left:
            return
        if left <= start and end <= right:
            self.tree[index] += value
            return
        mid = (start + end) // 2
        self.update(2 * index + 1, left, right, start, mid, value)
        self.update(2 * index + 2, left, right, mid + 1, end, value)

    def query(self, index, start, end, value):
        if start == end:
            return self.tree[index]
        mid = (start + end) // 2
        if self.tree[2 * index + 1] >= value:
            return self.query(2 * index + 1, start, mid, value)
        else:
            return self.query(2 * index + 2, mid + 1, end, value - self.tree[2 * index + 1])

def evaluate_cultivars(cultivars):
    cultivars.sort()
    n = len(cultivars)
    segment_tree = SegmentTree(n)
    result = []

    for i in range(n):
        left, right, growth = cultivars[i]
        overlapping = segment_tree.query(0, 0, n - 1, growth)
        result.append(overlapping)
        segment_tree.update(0, i, i, 0, n - 1, 1)

    return result

# Read input
n = int(input())
cultivars = []
for _ in range(n):
    left, right, growth = map(int, input().split())
    cultivars.append((left, right, growth))

# Evaluate cultivars
result = evaluate_cultivars(cultivars)

# Print results
for overlapping in result:
    print(overlapping)