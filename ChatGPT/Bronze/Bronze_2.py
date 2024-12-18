# Chatgpt Bronze Problems
# Problem 2

# Prompt 1


def calculate_cow_walk_distances():
    import sys
    input = sys.stdin.read
    data = input().split()

    N, P = int(data[0]), int(data[1])
    index = 2
    fence = []

    # Read the fence posts
    for _ in range(P):
        x, y = int(data[index]), int(data[index + 1])
        fence.append((x, y))
        index += 2

    # Read the cow walks
    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index + 4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Compute distances along the fence
    fence_distances = [0]
    for i in range(1, P):
        x1, y1 = fence[i - 1]
        x2, y2 = fence[i]
        dist = abs(x2 - x1) + abs(y2 - y1)
        fence_distances.append(fence_distances[-1] + dist)

    # Add the closing segment distance
    x1, y1 = fence[-1]
    x2, y2 = fence[0]
    closing_distance = abs(x2 - x1) + abs(y2 - y1)
    total_perimeter = fence_distances[-1] + closing_distance

    # Map position to distance along the fence
    def position_to_distance(position):
        x, y = position
        for i in range(P):
            x1, y1 = fence[i]
            x2, y2 = fence[(i + 1) % P]
            if (x1 == x2 and x1 == x and min(y1, y2) <= y <= max(y1, y2)) or \
               (y1 == y2 and y1 == y and min(x1, x2) <= x <= max(x1, x2)):
                segment_start_distance = fence_distances[i]
                if x1 == x2:  # Vertical segment
                    offset = abs(y - y1)
                else:  # Horizontal segment
                    offset = abs(x - x1)
                return segment_start_distance + offset
        return None

    # Calculate distances for each cow
    result = []
    for start, end in cows:
        start_distance = position_to_distance(start)
        end_distance = position_to_distance(end)
        clockwise_distance = abs(end_distance - start_distance)
        counterclockwise_distance = total_perimeter - clockwise_distance
        result.append(min(clockwise_distance, counterclockwise_distance))

    # Output results
    sys.stdout.write("\n".join(map(str, result)) + "\n")

calculate_cow_walk_distances()



# Prompt 1 a

def calculate_cow_walk_distances():
    # Simulate input for testing
    input = """5 4
    0 0
    2 0
    2 2
    0 2
    0 0 0 2
    0 2 1 0
    2 1 0 2
    1 0 1 2
    1 2 1 0"""
    data = input.split()

    if not data:
        print("Error: No input provided.")
        return

    N, P = int(data[0]), int(data[1])
    index = 2
    fence = []

    # Read the fence posts
    for _ in range(P):
        x, y = int(data[index]), int(data[index + 1])
        fence.append((x, y))
        index += 2

    # Read the cow walks
    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index + 4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Compute distances along the fence
    fence_distances = [0]
    for i in range(1, P):
        x1, y1 = fence[i - 1]
        x2, y2 = fence[i]
        dist = abs(x2 - x1) + abs(y2 - y1)
        fence_distances.append(fence_distances[-1] + dist)

    # Add the closing segment distance
    x1, y1 = fence[-1]
    x2, y2 = fence[0]
    closing_distance = abs(x2 - x1) + abs(y2 - y1)
    total_perimeter = fence_distances[-1] + closing_distance

    # Map position to distance along the fence
    def position_to_distance(position):
        x, y = position
        for i in range(P):
            x1, y1 = fence[i]
            x2, y2 = fence[(i + 1) % P]
            if (x1 == x2 and x1 == x and min(y1, y2) <= y <= max(y1, y2)) or \
               (y1 == y2 and y1 == y and min(x1, x2) <= x <= max(x1, x2)):
                segment_start_distance = fence_distances[i]
                if x1 == x2:  # Vertical segment
                    offset = abs(y - y1)
                else:  # Horizontal segment
                    offset = abs(x - x1)
                return segment_start_distance + offset
        return None

    # Calculate distances for each cow
    result = []
    for start, end in cows:
        start_distance = position_to_distance(start)
        end_distance = position_to_distance(end)
        clockwise_distance = abs(end_distance - start_distance)
        counterclockwise_distance = total_perimeter - clockwise_distance
        result.append(min(clockwise_distance, counterclockwise_distance))

    # Output results
    print("\n".join(map(str, result)))

# Call the function for testing
calculate_cow_walk_distances()



# Test more cases

def calculate_cow_walk_distances():
    # Simulate input for testing
    input = """100 994
0 0
1 0
1 4
6 4
6 3
7 3
7 5
9 5
9 4
10 4
10 3
12 3
12 5
16 5
16 3
17 3
17 4
23 4
23 2
28 2
28 3
31 3
31 5
34 5
34 1
37 1
37 3
39 3
39 5
43 5
43 3
44 3
44 2
48 2
48 3
49 3
49 2
52 2
52 1
56 1
56 5
62 5
62 3
67 3
67 2
69 2
69 3
71 3
71 2
72 2
72 4
82 4
82 3
83 3
83 5
93 5
93 2
96 2
96 3
97 3
97 1
100 1
100 6
1 6
1 9
2 9
2 7
12 7
12 10
16 10
16 7
18 7
18 9
19 9
19 11
29 11
29 8
32 8
32 10
35 10
35 11
42 11
42 9
50 9
50 10
56 10
56 7
57 7
57 9
58 9
58 11
59 11
59 9
60 9
60 8
63 8
63 10
64 10
64 9
66 9
66 7
67 7
67 8
70 8
70 9
71 9
71 11
72 11
72 10
73 10
73 8
83 8
83 9
85 9
85 8
88 8
88 10
94 10
94 7
97 7
97 9
98 9
98 7
100 7
100 12
1 12
1 17
2 17
2 16
10 16
10 15
13 15
13 17
15 17
15 13
18 13
18 14
24 14
24 16
25 16
25 17
28 17
28 15
29 15
29 14
32 14
32 15
33 15
33 17
35 17
35 15
43 15
43 16
48 16
48 17
51 17
51 14
52 14
52 16
54 16
54 17
56 17
56 13
65 13
65 17
66 17
66 15
67 15
67 14
81 14
81 13
87 13
87 14
89 14
89 13
90 13
90 16
91 16
91 15
93 15
93 14
95 14
95 15
98 15
98 14
100 14
100 18
1 18
1 21
6 21
6 20
15 20
15 19
16 19
16 23
19 23
19 19
21 19
21 20
25 20
25 22
27 22
27 23
28 23
28 24
29 24
29 20
31 20
31 19
32 19
32 21
47 21
47 20
52 20
52 24
54 24
54 20
57 20
57 24
58 24
58 19
60 19
60 24
61 24
61 19
63 19
63 24
64 24
64 20
65 20
65 22
67 22
67 19
69 19
69 20
70 20
70 19
75 19
75 22
79 22
79 23
85 23
85 21
94 21
94 23
97 23
97 19
100 19
100 25
1 25
1 30
9 30
9 28
15 28
15 29
17 29
17 28
20 28
20 29
21 29
21 26
26 26
26 28
30 28
30 29
32 29
32 26
33 26
33 28
37 28
37 29
38 29
38 27
40 27
40 30
42 30
42 28
44 28
44 30
50 30
50 28
51 28
51 29
56 29
56 27
58 27
58 28
61 28
61 30
66 30
66 28
68 28
68 29
75 29
75 30
87 30
87 27
91 27
91 26
92 26
92 27
94 27
94 30
95 30
95 27
96 27
96 29
98 29
98 30
100 30
100 31
1 31
1 36
2 36
2 33
5 33
5 32
10 32
10 36
20 36
20 32
22 32
22 33
23 33
23 34
26 34
26 36
28 36
28 34
29 34
29 33
30 33
30 32
32 32
32 36
34 36
34 32
41 32
41 34
42 34
42 36
44 36
44 33
46 33
46 36
50 36
50 33
54 33
54 34
55 34
55 35
59 35
59 36
62 36
62 34
65 34
65 35
69 35
69 33
70 33
70 32
71 32
71 34
76 34
76 32
90 32
90 33
93 33
93 32
95 32
95 36
100 36
100 37
1 37
1 39
3 39
3 42
8 42
8 40
9 40
9 42
10 42
10 41
12 41
12 40
23 40
23 39
32 39
32 40
37 40
37 38
38 38
38 39
39 39
39 41
41 41
41 39
47 39
47 38
48 38
48 40
51 40
51 38
56 38
56 40
58 40
58 41
59 41
59 42
60 42
60 39
61 39
61 40
66 40
66 41
67 41
67 39
75 39
75 38
77 38
77 41
78 41
78 38
80 38
80 42
87 42
87 39
88 39
88 42
94 42
94 39
98 39
98 38
100 38
100 43
1 43
1 48
6 48
6 47
9 47
9 44
11 44
11 49
21 49
21 47
24 47
24 48
34 48
34 49
36 49
36 45
39 45
39 46
40 46
40 49
43 49
43 46
46 46
46 47
47 47
47 48
49 48
49 45
50 45
50 46
52 46
52 45
53 45
53 47
56 47
56 46
57 46
57 45
59 45
59 44
73 44
73 45
74 45
74 47
75 47
75 46
79 46
79 45
85 45
85 49
89 49
89 47
91 47
91 46
93 46
93 44
94 44
94 45
98 45
98 44
100 44
100 50
1 50
1 53
2 53
2 55
3 55
3 53
8 53
8 55
10 55
10 53
11 53
11 54
14 54
14 51
17 51
17 55
19 55
19 53
22 53
22 51
25 51
25 52
29 52
29 54
37 54
37 53
39 53
39 55
47 55
47 52
49 52
49 55
50 55
50 53
64 53
64 54
67 54
67 52
71 52
71 55
72 55
72 53
73 53
73 54
74 54
74 53
76 53
76 54
78 54
78 53
80 53
80 52
83 52
83 55
85 55
85 54
86 54
86 55
95 55
95 53
100 53
100 56
1 56
1 60
2 60
2 59
4 59
4 57
5 57
5 58
6 58
6 59
8 59
8 57
13 57
13 59
15 59
15 57
17 57
17 61
21 61
21 58
23 58
23 60
24 60
24 59
30 59
30 57
33 57
33 60
39 60
39 57
40 57
40 60
43 60
43 59
44 59
44 61
46 61
46 59
51 59
51 61
57 61
57 58
60 58
60 60
64 60
64 58
65 58
65 60
67 60
67 61
68 61
68 58
69 58
69 61
84 61
84 59
95 59
95 61
97 61
97 57
100 57
100 62
1 62
1 67
3 67
3 64
5 64
5 66
6 66
6 64
12 64
12 65
13 65
13 67
14 67
14 63
16 63
16 64
19 64
19 66
23 66
23 65
24 65
24 66
25 66
25 63
27 63
27 65
29 65
29 66
31 66
31 64
34 64
34 63
43 63
43 64
49 64
49 65
52 65
52 67
59 67
59 64
62 64
62 67
69 67
69 64
70 64
70 65
71 65
71 66
72 66
72 67
76 67
76 66
83 66
83 63
85 63
85 64
90 64
90 63
91 63
91 65
100 65
100 68
1 68
1 69
2 69
2 70
6 70
6 74
7 74
7 69
10 69
10 74
11 74
11 71
14 71
14 72
15 72
15 71
24 71
24 73
30 73
30 69
32 69
32 70
36 70
36 71
37 71
37 72
38 72
38 69
43 69
43 74
44 74
44 73
45 73
45 72
50 72
50 74
51 74
51 70
55 70
55 74
59 74
59 71
62 71
62 73
66 73
66 70
72 70
72 74
75 74
75 72
78 72
78 73
79 73
79 71
82 71
82 72
88 72
88 70
91 70
91 74
100 74
100 75
1 75
1 76
2 76
2 78
4 78
4 80
5 80
5 76
10 76
10 78
14 78
14 76
19 76
19 77
20 77
20 78
26 78
26 77
29 77
29 79
32 79
32 76
36 76
36 77
40 77
40 76
46 76
46 77
49 77
49 79
53 79
53 77
57 77
57 79
58 79
58 78
60 78
60 77
74 77
74 80
76 80
76 76
79 76
79 80
81 80
81 79
85 79
85 77
90 77
90 78
92 78
92 80
93 80
93 77
95 77
95 79
96 79
96 77
98 77
98 79
100 79
100 81
1 81
1 82
2 82
2 85
10 85
10 86
11 86
11 82
12 82
12 84
13 84
13 86
14 86
14 85
24 85
24 82
28 82
28 85
29 85
29 84
30 84
30 85
31 85
31 86
33 86
33 85
35 85
35 82
39 82
39 86
41 86
41 85
43 85
43 86
44 86
44 82
55 82
55 84
65 84
65 85
69 85
69 84
75 84
75 86
78 86
78 83
81 83
81 84
83 84
83 82
86 82
86 83
89 83
89 84
92 84
92 83
94 83
94 82
95 82
95 84
100 84
100 87
1 87
1 90
5 90
5 88
6 88
6 92
7 92
7 88
8 88
8 91
10 91
10 89
20 89
20 91
24 91
24 92
27 92
27 91
33 91
33 90
44 90
44 92
48 92
48 88
52 88
52 91
54 91
54 92
55 92
55 91
61 91
61 88
62 88
62 90
64 90
64 91
68 91
68 92
69 92
69 90
71 90
71 92
73 92
73 90
76 90
76 91
78 91
78 89
79 89
79 91
81 91
81 90
84 90
84 88
86 88
86 91
91 91
91 92
96 92
96 88
100 88
100 93
1 93
1 98
4 98
4 95
10 95
10 97
12 97
12 95
15 95
15 99
17 99
17 96
22 96
22 99
25 99
25 97
39 97
39 95
42 95
42 94
43 94
43 97
48 97
48 99
50 99
50 96
57 96
57 95
59 95
59 96
64 96
64 99
67 99
67 97
69 97
69 96
70 96
70 98
71 98
71 95
76 95
76 99
81 99
81 95
83 95
83 96
84 96
84 95
85 95
85 98
86 98
86 99
87 99
87 94
89 94
89 96
91 96
91 99
95 99
95 95
100 95
100 100
0 100
76 53 39 5
9 4 49 53
80 91 44 39
95 30 19 11
1 39 27 82
58 10 83 61
24 65 90 78
39 95 2 48
97 21 47 75
55 74 31 20
40 55 10 41
51 46 85 98
2 59 54 6
2 67 47 12
47 54 98 7
36 71 70 70
100 87 51 33
28 35 69 84
57 9 88 59
15 99 15 71
65 58 37 11
17 97 85 72
81 98 47 48
57 35 100 87
32 19 55 74
55 73 96 7
67 53 29 3
87 98 52 46
58 79 16 29
85 64 55 17
22 26 59 78
97 81 5 66
37 90 8 37
57 7 82 61
82 3 42 35
45 39 77 91
93 27 63 81
76 67 40 57
8 42 51 88
29 65 51 61
29 22 13 67
8 47 56 27
1 89 59 44
88 8 72 62
51 74 27 23
60 77 52 2
70 97 24 15
24 85 42 10
87 99 20 29
45 2 47 72
62 4 98 9
28 17 59 19
55 35 97 87
11 15 2 16
38 53 83 96
90 77 47 30
9 5 45 46
90 78 44 30
64 90 94 7
5 90 54 37
79 71 6 4
17 3 57 53
88 91 18 61
67 2 5 65
17 59 25 6
48 39 49 88
49 48 81 96
24 99 11 43
6 3 47 55
80 41 71 11
69 58 42 11
43 59 12 9
1 76 28 28
81 79 2 16
25 17 54 67
71 65 41 15
96 79 14 77
16 3 54 53
30 20 53 70
22 97 16 7
33 36 78 85
72 95 40 49
70 84 1 69
85 64 57 13
71 32 78 87
81 52 27 23
100 37 13 5
20 34 54 82
66 73 51 20
7 3 39 55
67 91 9 40
95 96 74 45
65 59 7 3
70 9 32 5
61 21 86 91
59 9 92 59
41 33 65 85
88 83 51 28
51 15 83 66
1 14 26 63
"""
    data = input.split()

    if not data:
        print("Error: No input provided.")
        return

    N, P = int(data[0]), int(data[1])
    index = 2
    fence = []

    # Read the fence posts
    for _ in range(P):
        x, y = int(data[index]), int(data[index + 1])
        fence.append((x, y))
        index += 2

    # Read the cow walks
    cows = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, data[index:index + 4])
        cows.append(((x1, y1), (x2, y2)))
        index += 4

    # Compute distances along the fence
    fence_distances = [0]
    for i in range(1, P):
        x1, y1 = fence[i - 1]
        x2, y2 = fence[i]
        dist = abs(x2 - x1) + abs(y2 - y1)
        fence_distances.append(fence_distances[-1] + dist)

    # Add the closing segment distance
    x1, y1 = fence[-1]
    x2, y2 = fence[0]
    closing_distance = abs(x2 - x1) + abs(y2 - y1)
    total_perimeter = fence_distances[-1] + closing_distance

    # Map position to distance along the fence
    def position_to_distance(position):
        x, y = position
        for i in range(P):
            x1, y1 = fence[i]
            x2, y2 = fence[(i + 1) % P]
            if (x1 == x2 and x1 == x and min(y1, y2) <= y <= max(y1, y2)) or \
               (y1 == y2 and y1 == y and min(x1, x2) <= x <= max(x1, x2)):
                segment_start_distance = fence_distances[i]
                if x1 == x2:  # Vertical segment
                    offset = abs(y - y1)
                else:  # Horizontal segment
                    offset = abs(x - x1)
                return segment_start_distance + offset
        return None

    # Calculate distances for each cow
    result = []
    for start, end in cows:
        start_distance = position_to_distance(start)
        end_distance = position_to_distance(end)
        clockwise_distance = abs(end_distance - start_distance)
        counterclockwise_distance = total_perimeter - clockwise_distance
        result.append(min(clockwise_distance, counterclockwise_distance))

    # Output results
    print("\n".join(map(str, result)))

# Call the function for testing
calculate_cow_walk_distances()

