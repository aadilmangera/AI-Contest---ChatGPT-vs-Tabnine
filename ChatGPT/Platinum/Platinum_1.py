# Chatgpt Platinum Problems
# Problem 1

# Prompt 1

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.extra_bits = 0

    def insert(self, bitstring):
        node = self.root
        need_bits = 0
        for bit in bitstring:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        if node.is_end:
            # Resolve conflict by adding extra bits
            need_bits = self.resolve_conflict(node)
        node.is_end = True
        return need_bits

    def resolve_conflict(self, node):
        # Add bits until we find an unused path
        queue = [(node, "")]
        while queue:
            curr, path = queue.pop(0)
            if not curr.is_end:
                # Mark this path as used
                curr.is_end = True
                return len(path)
            for bit in "01":
                if bit not in curr.children:
                    curr.children[bit] = TrieNode()
                queue.append((curr.children[bit], path + bit))
        return 0  # This should never occur

def minimum_time_to_prevent_lockdown(cows):
    trie = Trie()
    total_time = 0
    for cow_id in cows:
        total_time += trie.insert(cow_id)
    return total_time

# Input and Output handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    farm_ids = data[1:]
    print(minimum_time_to_prevent_lockdown(farm_ids))


# Prompt 2


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_count = 0  # Tracks how many IDs end at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_and_count_conflicts(self, bitstring):
        node = self.root
        additional_bits = 0
        for bit in bitstring:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        if node.end_count > 0:
            # Conflict resolution required
            additional_bits = self.resolve_conflict(node)
        node.end_count += 1
        return additional_bits

    def resolve_conflict(self, node):
        # Add bits to resolve conflict
        stack = [(node, "")]
        while stack:
            curr_node, path = stack.pop()
            if curr_node.end_count == 0:
                # Found an unused path
                curr_node.end_count += 1
                return len(path)
            for bit in "01":
                if bit not in curr_node.children:
                    curr_node.children[bit] = TrieNode()
                stack.append((curr_node.children[bit], path + bit))
        return 0  # This should never happen

def minimum_time_to_prevent_lockdown(cows):
    trie = Trie()
    total_time = 0
    for cow_id in cows:
        total_time += trie.insert_and_count_conflicts(cow_id)
    return total_time

# Input and Output handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    farm_ids = data[1:]
    print(minimum_time_to_prevent_lockdown(farm_ids))



# Prompt 3


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    if not data or len(data) < 2:
        print("Error: No input provided or invalid input format.")
        return

    n = int(data[0])  # Number of cows
    farm_ids = data[1:]
    if len(farm_ids) != n:
        print("Error: Number of Farm IDs does not match the specified count.")
        return

    print(minimum_time_to_prevent_lockdown(farm_ids))

if __name__ == "__main__":
    main()


# Testing with other input

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_count = 0  # Tracks how many IDs end at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_and_count_conflicts(self, bitstring):
        node = self.root
        additional_bits = 0
        for bit in bitstring:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        if node.end_count > 0:
            # Conflict resolution required
            additional_bits = self.resolve_conflict(node)
        node.end_count += 1
        return additional_bits

    def resolve_conflict(self, node):
        # Add bits to resolve conflict
        stack = [(node, "")]
        while stack:
            curr_node, path = stack.pop()
            if curr_node.end_count == 0:
                # Found an unused path
                curr_node.end_count += 1
                return len(path)
            for bit in "01":
                if bit not in curr_node.children:
                    curr_node.children[bit] = TrieNode()
                stack.append((curr_node.children[bit], path + bit))
        return 0  # This should never happen

def minimum_time_to_prevent_lockdown(cows):
    trie = Trie()
    total_time = 0
    for cow_id in cows:
        total_time += trie.insert_and_count_conflicts(cow_id)
    return total_time

# Hardcoded input
def main():
    # Example hardcoded input
    n = 5
    farm_ids = [
        "3",
        "1",
        "1",
        "11"
    ]  # Example Farm IDs

    print(minimum_time_to_prevent_lockdown(farm_ids))

if __name__ == "__main__":
    main()





















