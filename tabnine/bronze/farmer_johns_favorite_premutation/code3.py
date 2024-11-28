input_str = '''5
2
1
2
2
4
1 1 1
4
2 1 1
4
3 2 1'''

output = []

def input():
    return input_str.split('\n')[0]

def print(x):
    output.append(str(x))

def reconstruct_permutation(N, hints):
    permutation = list(range(1, N + 1))
    for hint in hints:
        if permutation[0] > permutation[-1]:
            permutation.pop(0)
            permutation.insert(hint, permutation[0])
        else:
            permutation.pop()
            permutation.insert(hint, permutation[0])
    return permutation if len(permutation) == 1 else -1

T = int(input())
for _ in range(T):
    N = int(input())
    hints = list(map(int, input().split()))
    result = reconstruct_permutation(N, hints)
    print(result)

'\n'.join(output)