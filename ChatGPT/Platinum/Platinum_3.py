# Chatgpt Platinum Problems
# Problem 3

# Prompt 1

def min_time_to_align(L, R, N, K, activation_points):
    from math import gcd

    # Compute target positions modulo L
    target_positions = [(i * (L // R)) % L for i in range(R)]
    target_positions.sort()
    activation_points.sort()

    # Helper to calculate time to move between two points on the circle
    def travel_time(start, end):
        return min((end - start) % L, (start - end) % L)

    min_time = float('inf')

    # Try placing the first robot at each activation point
    for first_robot_pos in activation_points:
        # Calculate the initial time to reach this activation point
        move_time = travel_time(0, first_robot_pos)
        first_robot_time = move_time

        # Synchronize the robots' movement
        valid = True
        max_time = 0
        for i, target in enumerate(target_positions):
            # Desired position of the i-th robot at time t
            desired_pos = (first_robot_pos + i * (L // R)) % L

            # Find the closest activation point to this desired position
            closest_activation = min(
                activation_points,
                key=lambda p: travel_time(desired_pos, p)
            )

            # Time to wait for the i-th robot to align
            align_time = travel_time(desired_pos, closest_activation) * K
            max_time = max(max_time, first_robot_time + align_time)

        # Update minimum time
        min_time = min(min_time, max_time)

    return min_time

# Read input
L, R, N, K = map(int, input().split())
activation_points = list(map(int, input().split()))

# Solve and print result
print(min_time_to_align(L, R, N, K, activation_points))



# Testing with another test input and expected output


def min_time_to_align(L, R, N, K, activation_points):
    from math import gcd

    # Compute target positions modulo L
    target_positions = [(i * (L // R)) % L for i in range(R)]
    target_positions.sort()
    activation_points.sort()

    # Helper to calculate time to move between two points on the circle
    def travel_time(start, end):
        return min((end - start) % L, (start - end) % L)

    min_time = float('inf')

    # Try placing the first robot at each activation point
    for first_robot_pos in activation_points:
        # Calculate the initial time to reach this activation point
        move_time = travel_time(0, first_robot_pos)
        first_robot_time = move_time

        # Synchronize the robots' movement
        valid = True
        max_time = 0
        for i, target in enumerate(target_positions):
            # Desired position of the i-th robot at time t
            desired_pos = (first_robot_pos + i * (L // R)) % L

            # Find the closest activation point to this desired position
            closest_activation = min(
                activation_points,
                key=lambda p: travel_time(desired_pos, p)
            )

            # Time to wait for the i-th robot to align
            align_time = travel_time(desired_pos, closest_activation) * K
            max_time = max(max_time, first_robot_time + align_time)

        # Update minimum time
        min_time = min(min_time, max_time)

    return min_time

# Read input
L, R, N, K = map(int, input().split())
activation_points = list(map(int, input().split()))

# Solve and print result
print(min_time_to_align(L, R, N, K, activation_points))


# Prompt 2

def min_time_to_align(L, R, N, K, activation_points):
    from math import gcd

    # Debug input values
    print(f"L: {L}, R: {R}, N: {N}, K: {K}")
    print(f"Activation Points: {activation_points}")

    # Compute target positions modulo L
    target_positions = [(i * (L // R)) % L for i in range(R)]
    target_positions.sort()
    activation_points.sort()

    # Helper to calculate time to move between two points on the circle
    def travel_time(start, end):
        return min((end - start) % L, (start - end) % L)

    min_time = float('inf')

    # Try placing the first robot at each activation point
    for first_robot_pos in activation_points:
        move_time = travel_time(0, first_robot_pos)
        first_robot_time = move_time

        valid = True
        max_time = 0
        for i, target in enumerate(target_positions):
            desired_pos = (first_robot_pos + i * (L // R)) % L
            closest_activation = min(
                activation_points,
                key=lambda p: travel_time(desired_pos, p)
            )
            align_time = travel_time(desired_pos, closest_activation) * K
            max_time = max(max_time, first_robot_time + align_time)

        min_time = min(min_time, max_time)

    return min_time

# Test with debug-friendly input
try:
    L, R, N, K = map(int, input("Enter L, R, N, K: ").split())
    activation_points = list(map(int, input(f"Enter {N} activation points: ").split()))
    result = min_time_to_align(L, R, N, K, activation_points)
    print(f"Minimum time to align: {result}")
except Exception as e:
    print(f"Error: {e}")


# Prompt 3


def min_time_to_align(L, R, N, K, activation_points):
    from math import gcd

    activation_points.sort()

    # Helper to calculate time to move between two points on the circle
    def travel_time(start, end):
        return min((end - start) % L, (start - end) % L)

    min_time = float('inf')

    # Try placing the first robot at each activation point
    for first_robot_pos in activation_points:
        # Time for the first robot to reach its initial position
        first_robot_time = travel_time(0, first_robot_pos)

        # Calculate the maximum time required for all robots
        max_time = 0
        for i in range(R):
            # Desired position of the i-th robot
            desired_pos = (first_robot_pos + i * (L // R)) % L

            # If there's only one activation point, all robots must use it
            closest_activation = activation_points[0] if N == 1 else min(
                activation_points,
                key=lambda p: travel_time(desired_pos, p)
            )

            # Calculate the time for the i-th robot to align
            align_time = travel_time(desired_pos, closest_activation) * K
            max_time = max(max_time, first_robot_time + align_time)

        # Update the minimum time
        min_time = min(min_time, max_time)

    return min_time

# Example Input
L, R, N, K = 24, 3, 1, 2
activation_points = [16]

# L, R, N, K = 10, 2, 1, 2
# activation_points = [7]

# Output the result
result = min_time_to_align(L, R, N, K, activation_points)
print(f"Minimum time to align: {result}")




























