# Chatgpt Gold Problems
# Problem 2

from sortedcontainers import SortedList

def count_overlaps(N, intervals):
    # Sort intervals by start time (and use index for stable processing)
    indexed_intervals = [(l, r, k, idx) for idx, (l, r, k) in enumerate(intervals)]
    indexed_intervals.sort()

    # Active intervals: stores (end, index)
    active_intervals = SortedList()
    results = [0] * N

    for l, r, k, idx in indexed_intervals:
        # Remove intervals that are no longer active
        while active_intervals and active_intervals[0][0] < l:
            active_intervals.pop(0)

        # Count valid overlaps for the current interval
        for end, j in active_intervals:
            if min(r, end) - max(l, intervals[j][0]) >= k:
                results[idx] += 1
                results[j] += 1  # Increment for both sides

        # Add the current interval to active list
        active_intervals.add((r, idx))

    return results

# Input reading and output
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    intervals = [tuple(map(int, line.split())) for line in data[1:]]

    results = count_overlaps(N, intervals)
    print("\n".join(map(str, results)))


from sortedcontainers import SortedList

def count_overlaps(N, intervals):
    events = []  # To store start and end events
    for idx, (l, r, k) in enumerate(intervals):
        events.append((l, 1, idx))  # Start of interval
        events.append((r, -1, idx))  # End of interval

    # Sort events by position, then by type (-1 before 1 to process ends first)
    events.sort()

    active_intervals = SortedList()
    results = [0] * N

    for pos, event_type, idx in events:
        l, r, k = intervals[idx]

        if event_type == 1:  # Start of interval
            # Check overlap with all active intervals
            for aj in active_intervals:
                al, ar, ak, aidx = aj
                overlap_length = min(r, ar) - max(l, al)
                if overlap_length >= k:
                    results[idx] += 1
                if overlap_length >= ak:
                    results[aidx] += 1

            # Add current interval to active intervals
            active_intervals.add((l, r, k, idx))

        elif event_type == -1:  # End of interval
            # Remove interval from active intervals
            active_intervals.remove((l, r, k, idx))

    return results

# Input reading and output
if __name__ == "__main__":
    data = [
        "4",
        "3 6 1",
        "2 5 1",
        "4 10 1",
        "1 4 1",
    ]
    N = int(data[0])
    intervals = [tuple(map(int, line.split())) for line in data[1:]]


    results = count_overlaps(N, intervals)
    print("\n".join(map(str, results)))


# Prompt 1a

from sortedcontainers import SortedList

def count_overlaps(N, intervals):
    events = []  # To store start and end events
    for idx, (l, r, k) in enumerate(intervals):
        events.append((l, 1, idx))  # Start of interval
        events.append((r, -1, idx))  # End of interval

    # Sort events by position, then by type (-1 before 1 to process ends first)
    events.sort()

    active_intervals = SortedList()
    results = [0] * N

    for pos, event_type, idx in events:
        l, r, k = intervals[idx]

        if event_type == 1:  # Start of interval
            # Check overlap with all active intervals
            for aj in active_intervals:
                al, ar, ak, aidx = aj
                overlap_length = min(r, ar) - max(l, al)
                if overlap_length >= k:
                    results[idx] += 1
                if overlap_length >= ak:
                    results[aidx] += 1

            # Add current interval to active intervals
            active_intervals.add((l, r, k, idx))

        elif event_type == -1:  # End of interval
            # Remove interval from active intervals
            active_intervals.remove((l, r, k, idx))

    return results

# Input reading and output
if __name__ == "__main__":
    data = [
        "4",
        "3 6 1",
        "2 5 1",
        "4 10 1",
        "1 4 1",
    ]
    N = int(data[0])
    intervals = [tuple(map(int, line.split())) for line in data[1:]]


    results = count_overlaps(N, intervals)
    print("\n".join(map(str, results)))



# Test more cases


from sortedcontainers import SortedList

def count_overlaps(N, intervals):
    events = []  # To store start and end events
    for idx, (l, r, k) in enumerate(intervals):
        events.append((l, 1, idx))  # Start of interval
        events.append((r, -1, idx))  # End of interval

    # Sort events by position, then by type (-1 before 1 to process ends first)
    events.sort()

    active_intervals = SortedList()
    results = [0] * N

    for pos, event_type, idx in events:
        l, r, k = intervals[idx]

        if event_type == 1:  # Start of interval
            # Check overlap with all active intervals
            for aj in active_intervals:
                al, ar, ak, aidx = aj
                overlap_length = min(r, ar) - max(l, al)
                if overlap_length >= k:
                    results[idx] += 1
                if overlap_length >= ak:
                    results[aidx] += 1

            # Add current interval to active intervals
            active_intervals.add((l, r, k, idx))

        elif event_type == -1:  # End of interval
            # Remove interval from active intervals
            active_intervals.remove((l, r, k, idx))

    return results

# Input reading and output
if __name__ == "__main__":
    data = [
        "5",
        "8 10 2",
        "4 9 2",
        "3 7 4",
        "5 7 1",
        "2 7 1"
    ]
    N = int(data[0])
    intervals = [tuple(map(int, line.split())) for line in data[1:]]


    results = count_overlaps(N, intervals)
    print("\n".join(map(str, results)))





