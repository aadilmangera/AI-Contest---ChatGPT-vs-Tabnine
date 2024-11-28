class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.count = 0

def insert(root, farm_id):
    node = root
    for bit in farm_id:
        bit_index = int(bit)
        if node.children[bit_index] is None:
            node.children[bit_index] = TrieNode()
        node = node.children[bit_index]
        node.count += 1
    node.count += 1  # Increment count for the leaf node

def dfs(node, depth):
    if node.count == 1:
        return depth
    left_count = node.children[0].count if node.children[0] else 0
    right_count = node.children[1].count if node.children[1] else 0
    if left_count == 0 or right_count == 0:
        return dfs(node.children[0] if left_count > 0 else node.children[1], depth + 1)
    return min(dfs(node.children[0], depth + 1), dfs(node.children[1], depth + 1))

def solve():
    n = int(input())
    root = TrieNode()
    for _ in range(n):
        farm_id = input()
        insert(root, farm_id)
    return dfs(root, 0)

print(solve())