class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.is_leaf = False

def insert(root, farm_id):
    node = root
    for bit in farm_id:
        bit_index = int(bit)
        if node.children[bit_index] is None:
            node.children[bit_index] = TrieNode()
        node = node.children[bit_index]
    node.is_leaf = True

def calculate_min_bits(root, depth, max_depth):
    if root.is_leaf:
        return depth
    min_bits = float('inf')
    for bit_index in range(2):
        if root.children[bit_index] is not None:
            min_bits = min(min_bits, calculate_min_bits(root.children[bit_index], depth + 1, max_depth))
    return max(min_bits, max_depth[depth])

def main():
    n = int(input())
    root = TrieNode()
    farm_ids = []
    for _ in range(n):
        farm_id = input()
        farm_ids.append(farm_id)
        insert(root, farm_id)
    max_depth = [0] * len(farm_ids[0])
    for farm_id in farm_ids:
        for i, bit in enumerate(farm_id):
            max_depth[i] = max(max_depth[i], int(bit))
    min_bits = calculate_min_bits(root, 0, max_depth)
    print(min_bits)

main()