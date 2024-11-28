import heapq

lines = input().splitlines()
(N, K) = map(int, lines[0].split())
times = list(map(int, lines[1].split()))

# Initialize priority queue with farmers and their interview times
pq = [(times[i], i) for i in range(K)]
heapq.heapify(pq)

# Initialize list to store finish times of farmers
finish_times = [0] * K

# Find the time Bessie's interview will begin
bessie_time = 0
for i in range(N):
    (time, farmer) = heapq.heappop(pq)
    bessie_time = max(bessie_time, time)
    if i == N - 1:
        bessie_time += times[N]
    finish_times[farmer] = bessie_time
    # Add the next cow to the priority queue
    if i + K < N:
        heapq.heappush(pq, (bessie_time + times[i + K], farmer))

print(bessie_time)

# Find which farmers could potentially interview Bessie
bessie_interviewers = [1 if finish_times[i] >= bessie_time else 0 for i in range(K)]
print(''.join(map(str, bessie_interviewers)))