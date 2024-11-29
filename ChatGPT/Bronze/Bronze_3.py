# Chatgpt Bronze Problems
# Problem 3

# Prompt 1


def reconstruct_permutations(test_cases):
    results = []
    for N, h in test_cases:
        # Initialize possible numbers and result array
        candidates = set(range(1, N + 1))
        p = []

        # Attempt to reconstruct p in reverse
        for i in range(N - 1, 0, -1):
            if not candidates:
                results.append(-1)
                break

            if h[i - 1] in candidates:
                # Add the hinted number to p
                p.append(h[i - 1])
                candidates.remove(h[i - 1])
            else:
                results.append(-1)
                break
        else:
            # Add the final remaining number
            if len(candidates) == 1:
                p.append(candidates.pop())
                p.reverse()
                results.append(p)
            else:
                results.append(-1)
    return results

# Input Parsing
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    h = list(map(int, input().split()))
    test_cases.append((N, h))

# Solve and Output
results = reconstruct_permutations(test_cases)
for res in results:
    if res == -1:
        print(-1)
    else:
        print(" ".join(map(str, res)))


# Prompt 1 a


def reconstruct_permutations(test_cases):
    results = []

    for N, h in test_cases:
        # Start with the full range of numbers
        candidates = list(range(1, N + 1))  # sorted numbers 1 to N
        p = []

        # Reverse-simulate Farmer Nhoj's process
        is_valid = True
        for i in range(len(h) - 1, -1, -1):
            if len(candidates) < 2:
                is_valid = False
                break

            if h[i] == candidates[0]:
                # Case 1: h[i] matches the first element, remove it
                p.append(candidates.pop(0))
            elif h[i] == candidates[-1]:
                # Case 2: h[i] matches the last element, remove it
                p.append(candidates.pop(-1))
            else:
                # Invalid hint
                is_valid = False
                break

        # Add the remaining element if valid
        if is_valid:
            p.append(candidates[0])
            p.reverse()  # Reverse to correct order
            results.append(p)
        else:
            results.append(-1)

    return results

input_data = """5
2
1
2
2
4
1 1 1
4
2 1 1
4
3 2 1
"""
input_lines = input_data.splitlines()
def input():
    return input_lines.pop(0)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    h = list(map(int, input().split()))
    test_cases.append((N, h))

# Solve and Output
results = reconstruct_permutations(test_cases)
for res in results:
    if res == -1:
        print(-1)
    else:
        print(" ".join(map(str, res)))




# Prompt

def reconstruct_permutations(test_cases):
    results = []
    for N, h in test_cases:
        # Initialize the list of possible numbers and simulate the process
        candidates = list(range(1, N + 1))
        left, right = 0, N - 1
        output = []

        valid = True
        for hint in h:
            if candidates[left] > candidates[right]:
                if candidates[left + 1] == hint:
                    output.append(candidates[left])
                    left += 1
                else:
                    valid = False
                    break
            else:
                if candidates[right - 1] == hint:
                    output.append(candidates[right])
                    right -= 1
                else:
                    valid = False
                    break

        if not valid:
            results.append(-1)
        else:
            output.extend(candidates[left:right + 1])  # Add remaining numbers
            results.append(output)
    return results


# Input Handling
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        h = list(map(int, data[idx + 1].split()))
        test_cases.append((N, h))
        idx += 2

    # Solve
    results = reconstruct_permutations(test_cases)
    for res in results:
        if res == -1:
            print(-1)
        else:
            print(" ".join(map(str, res)))


# Run the function
if __name__ == "__main__":
    main()



# Prompt 2 a

from io import StringIO
import sys
def reconstruct_permutations(test_cases):
    results = []
    for N, h in test_cases:
        # Initialize the list of possible numbers and simulate the process
        candidates = list(range(1, N + 1))
        left, right = 0, N - 1
        output = []

        valid = True
        for hint in h:
            if candidates[left] > candidates[right]:
                if candidates[left + 1] == hint:
                    output.append(candidates[left])
                    left += 1
                else:
                    valid = False
                    break
            else:
                if candidates[right - 1] == hint:
                    output.append(candidates[right])
                    right -= 1
                else:
                    valid = False
                    break

        if not valid:
            results.append(-1)
        else:
            output.extend(candidates[left:right + 1])  # Add remaining numbers
            results.append(output)
    return results
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        h = list(map(int, data[idx + 1].split()))
        test_cases.append((N, h))
        idx += 2

    # Solve
    results = reconstruct_permutations(test_cases)
    for res in results:
        if res == -1:
            print(-1)
        else:
            print(" ".join(map(str, res)))
# Hardcoded test input
test_input = """5
2
1
2
2
4
1 1 1
4
2 1 1
4
3 2 1
"""
sys.stdin = StringIO(test_input)

# Call main function
main()



# Prompt 3

def reconstruct_permutations(test_cases):
    results = []

    for N, h in test_cases:
        candidates = list(range(1, N + 1))  # Numbers from 1 to N
        output = []
        left, right = 0, N - 1  # Start from both ends of the permutation

        valid = True
        for hint in h:
            if candidates[left] > candidates[right]:  # First element > Last element
                if left + 1 < len(candidates) and candidates[left + 1] == hint:
                    output.append(candidates[left])
                    left += 1
                else:
                    valid = False
                    break
            else:  # First element <= Last element
                if right - 1 >= 0 and candidates[right - 1] == hint:
                    output.append(candidates[right])
                    right -= 1
                else:
                    valid = False
                    break

        if not valid:
            results.append(-1)
        else:
            # Add remaining elements in lexicographical order
            output.extend(candidates[left:right + 1])
            results.append(output)

    return results


# Input Handling
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        h = list(map(int, data[idx + 1].split()))
        test_cases.append((N, h))
        idx += 2

    # Solve
    results = reconstruct_permutations(test_cases)
    for res in results:
        if res == -1:
            print(-1)
        else:
            print(" ".join(map(str, res)))


# Run the function
if __name__ == "__main__":
    main()




# Prompt 3 a


def reconstruct_permutations(test_cases):
    results = []

    for N, h in test_cases:
        candidates = list(range(1, N + 1))  # Numbers from 1 to N
        output = []
        left, right = 0, N - 1  # Start from both ends of the permutation

        valid = True
        for hint in h:
            if candidates[left] > candidates[right]:  # First element > Last element
                if left + 1 < len(candidates) and candidates[left + 1] == hint:
                    output.append(candidates[left])
                    left += 1
                else:
                    valid = False
                    break
            else:  # First element <= Last element
                if right - 1 >= 0 and candidates[right - 1] == hint:
                    output.append(candidates[right])
                    right -= 1
                else:
                    valid = False
                    break

        if not valid:
            results.append(-1)
        else:
            # Add remaining elements in lexicographical order
            output.extend(candidates[left:right + 1])
            results.append(output)

    return results


# Input Handling
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()

    if not data:  # If no input data is provided
        print("No input provided.")
        return

    T = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        h = list(map(int, data[idx + 1].split()))
        test_cases.append((N, h))
        idx += 2

    # Solve
    results = reconstruct_permutations(test_cases)
    for res in results:
        if res == -1:
            print(-1)
        else:
            print(" ".join(map(str, res)))


# Fallback for Testing in Non-stdin Environments
if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("No valid input detected. Using fallback test data.")
        from io import StringIO
        import sys

        # Example test input
        test_input = """5
2
1
2
2
4
1 1 1
4
2 1 1
4
3 2 1
"""
        sys.stdin = StringIO(test_input)

















