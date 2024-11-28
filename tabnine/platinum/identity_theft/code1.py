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

def calculate_min_bits(root, depth):
    if root.is_leaf:
        return depth
    min_bits = float('inf')
    for child in root.children:
        if child is not None:
            min_bits = min(min_bits, calculate_min_bits(child, depth + 1))
    return min_bits

def main():
    n = int(input())
    root = TrieNode()
    for _ in range(n):
        farm_id = input()
        insert(root, farm_id)
    min_bits = calculate_min_bits(root, 0)
    print(min_bits)

main()