# Chatgpt Silver Problems
# Problem 1

# Prompt 1

import heapq

def find_bessie_interview(N, K, t):
    # Min-heap to store (finish_time, farmer_id)
    heap = []

    # Initialize heap with first K cows
    for i in range(K):
        heapq.heappush(heap, (t[i], i))

    # Process the remaining cows
    for i in range(K, N):
        finish_time, farmer_id = heapq.heappop(heap)
        heapq.heappush(heap, (finish_time + t[i], farmer_id))

    # Now the heap contains the times when Bessie could be interviewed
    bessie_time = heap[0][0]
    candidates = [0] * K
    for finish_time, farmer_id in heap:
        if finish_time == bessie_time:
            candidates[farmer_id] = 1

    # Convert candidates to a bit string
    candidate_bit_string = ''.join(map(str, candidates))

    # Output results
    print(bessie_time)
    print(candidate_bit_string)

# Input reading
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N, K = map(int, data[:2])
    t = list(map(int, data[2:]))
    find_bessie_interview(N, K, t)



# Prompt 1 a


import sys
from io import StringIO

# Mock the input
mock_input = """6 3
3 1 4159 2 6 5"""
sys.stdin = StringIO(mock_input)

# Code from before, unaltered
def find_bessie_interview(N, K, t):
    import heapq

    heap = []
    for i in range(K):
        heapq.heappush(heap, (t[i], i))

    for i in range(K, N):
        finish_time, farmer_id = heapq.heappop(heap)
        heapq.heappush(heap, (finish_time + t[i], farmer_id))

    bessie_time = heap[0][0]
    candidates = [0] * K
    for finish_time, farmer_id in heap:
        if finish_time == bessie_time:
            candidates[farmer_id] = 1

    candidate_bit_string = ''.join(map(str, candidates))

    print(bessie_time)
    print(candidate_bit_string)

# Input handling as before
input = sys.stdin.read
data = input().split()
N, K = map(int, data[:2])
t = list(map(int, data[2:]))
find_bessie_interview(N, K, t)


# Prompt 2


# Simulate inputs in Jupyter
def find_bessie_interview(N, K, t):
    import heapq

    # Min-heap to store (finish_time, farmer_id)
    heap = []

    # Initialize heap with the first K farmers and cows
    for i in range(K):
        heapq.heappush(heap, (t[i], i))

    # Process the remaining cows
    for i in range(K, N):
        finish_time, farmer_id = heapq.heappop(heap)
        heapq.heappush(heap, (finish_time + t[i], farmer_id))

    # After all cows before Bessie are processed, heap contains finish times
    bessie_time = heap[0][0]
    candidates = [0] * K

    # Identify all farmers who could interview Bessie
    for finish_time, farmer_id in heap:
        if finish_time == bessie_time:
            candidates[farmer_id] = 1

    # Convert candidates list to a bit string
    candidate_bit_string = ''.join(map(str, candidates))

    # Output results
    print(bessie_time)
    print(candidate_bit_string)


# Testing in Jupyter
N = 6
K = 3
t = [3, 1, 4159, 2, 6, 5]
find_bessie_interview(N, K, t)



# Prompt 3

def find_bessie_interview(N, K, t):
    import heapq

    # Min-heap to store (finish_time, farmer_id)
    heap = []

    # Initialize heap with the first K farmers and their first assigned cows
    for i in range(K):
        heapq.heappush(heap, (t[i], i))

    # Process the remaining cows
    for i in range(K, N):
        finish_time, farmer_id = heapq.heappop(heap)
        heapq.heappush(heap, (finish_time + t[i], farmer_id))

    # After processing all cows, determine when Bessie will be interviewed
    bessie_time = heap[0][0]  # Bessie is interviewed when the first farmer finishes
    candidates = [0] * K

    # Mark all farmers who could interview Bessie
    for finish_time, farmer_id in heap:
        if finish_time == bessie_time:
            candidates[farmer_id] = 1

    # Convert the candidates list to a bit string
    candidate_bit_string = ''.join(map(str, candidates))

    # Output the results
    print(bessie_time)
    print(candidate_bit_string)


# Test input
N, K = 6, 3
t = [3, 1, 4159, 2, 6, 5]
find_bessie_interview(N, K, t)
















