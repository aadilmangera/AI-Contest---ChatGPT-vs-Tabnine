# Chatgpt Gold Problems
# Problem 1

# Prompt 1


def minimum_moves(N, K, start, end):
    # Extract positions of 1s in both strings
    positions_start = [i for i, bit in enumerate(start) if bit == '1']
    positions_end = [i for i, bit in enumerate(end) if bit == '1']

    # Both must have the same number of 1s
    if len(positions_start) != len(positions_end):
        return -1  # Invalid input (shouldn't occur based on constraints)

    # Initialize variables
    moves = 0

    # Calculate the number of moves to align the positions
    for i in range(len(positions_start)):
        moves += abs(positions_start[i] - positions_end[i])

    return moves

# Input handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    # Read inputs
    N, K = map(int, data[0:2])
    start = data[2]
    end = data[3]

    # Output the result
    print(minimum_moves(N, K, start, end))


# Prompt 1 a

from collections import deque

def minimum_moves(N, K, start, end):
    # Extract positions of '1's
    positions_start = [i for i, bit in enumerate(start) if bit == '1']
    positions_end = [i for i, bit in enumerate(end) if bit == '1']

    # Validate input (should be guaranteed by problem)
    if len(positions_start) != len(positions_end):
        return -1

    # Deque to track current valid positions for moves
    dq = deque()
    total_moves = 0

    # Iterate through matching positions
    for i, pos in enumerate(positions_end):
        # Maintain valid window of positions within K distance
        while dq and dq[0] < pos - K:
            dq.popleft()

        # Add the current position from positions_start
        dq.append(positions_start[i])

        # Choose the best position within the window
        closest = dq.popleft()
        total_moves += abs(closest - pos)

    return total_moves

# Input handling
if __name__ == "__main__":

    N, K = 4, 1
    start = "0111"
    end = "1110"

    # Call the function
    print(minimum_moves(N, K, start, end))


# Test more cases


from collections import deque

def minimum_moves(N, K, start, end):
    # Extract positions of '1's
    positions_start = [i for i, bit in enumerate(start) if bit == '1']
    positions_end = [i for i, bit in enumerate(end) if bit == '1']

    # Validate input (should be guaranteed by problem)
    if len(positions_start) != len(positions_end):
        return -1

    # Deque to track current valid positions for moves
    dq = deque()
    total_moves = 0

    # Iterate through matching positions
    for i, pos in enumerate(positions_end):
        # Maintain valid window of positions within K distance
        while dq and dq[0] < pos - K:
            dq.popleft()

        # Add the current position from positions_start
        dq.append(positions_start[i])

        # Choose the best position within the window
        closest = dq.popleft()
        total_moves += abs(closest - pos)

    return total_moves

# Input handling
if __name__ == "__main__":

    N, K = 5, 2
    start = "11000"
    end = "00011"

    # Call the function
    print(minimum_moves(N, K, start, end))


# Prompt 2a

def minimum_moves(N, K, start, end):
    # Step 1: Extract positions of '1' in both strings
    positions_start = [i for i, bit in enumerate(start) if bit == '1']
    positions_end = [i for i, bit in enumerate(end) if bit == '1']

    # Step 2: Validate if transformation is possible
    if len(positions_start) != len(positions_end):
        return -1  # This should not happen as per problem constraints

    # Step 3: Calculate minimum moves required
    moves = 0
    for i in range(len(positions_start)):
        moves += abs(positions_start[i] - positions_end[i])

    return moves


# Input handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Parse inputs
    N, K = map(int, data[0].split())
    start = data[1]
    end = data[2]

    # Compute and output result
    print(minimum_moves(N, K, start, end))

def minimum_moves(N, K, start, end):
    # Step 1: Extract positions of '1' in both strings
    positions_start = [i for i, bit in enumerate(start) if bit == '1']
    positions_end = [i for i, bit in enumerate(end) if bit == '1']

    # Step 2: Validate if transformation is possible
    if len(positions_start) != len(positions_end):
        return -1  # This should not happen as per problem constraints

    # Step 3: Calculate minimum moves required
    moves = 0
    for i in range(len(positions_start)):
        moves += abs(positions_start[i] - positions_end[i])

    return moves


if __name__ == "__main__":
    import sys

    try:
        # Read input
        input = sys.stdin.read
        data = input().splitlines()

        if len(data) < 3:
            raise ValueError("Insufficient input provided.")

        # Parse inputs
        N, K = map(int, data[0].split())
        start = data[1]
        end = data[2]

        # Compute and output result
        print(minimum_moves(N, K, start, end))

    except Exception as e:
        # For debugging, provide a fallback mechanism
        print(f"Error: {e}")
        # Example fallback input for local testing
        N, K = 5, 2
        start = "11000"
        end = "00011"
        print(minimum_moves(N, K, start, end))


# Prompt 3

def minimum_moves(N, K, start, end):
    # Extract the positions of '1's in both strings
    positions_start = [i for i, bit in enumerate(start) if bit == '1']
    positions_end = [i for i, bit in enumerate(end) if bit == '1']

    # Check that transformation is possible
    if len(positions_start) != len(positions_end):
        return -1  # Not possible to transform (guaranteed not to happen in this problem)

    # Calculate the minimum moves to align
    moves = 0
    for s, e in zip(positions_start, positions_end):
        moves += abs(s - e)

    return moves


# Input handling
if __name__ == "__main__":
    N, K = 5, 2
    start = "11000"
    end = "00011"

    # Call the function
    print(minimum_moves(N, K, start, end))
