def evaluate_statement(statement):
    stack = []
    for keyword in statement:
        if keyword == 'true' or keyword == 'false':
            stack.append(keyword)
        elif keyword == 'and':
            if len(stack) < 2:
                return 'Error: Not enough operands for "and" operator'
            y = stack.pop()
            x = stack.pop()
            if x == 'true' and y == 'true':
                stack.append('true')
            else:
                stack.append('false')
        elif keyword == 'or':
            if len(stack) < 2:
                return 'Error: Not enough operands for "or" operator'
            y = stack.pop()
            x = stack.pop()
            if x == 'true' or y == 'true':
                stack.append('true')
            else:
                stack.append('false')
    return stack[0]

def solve_queries(N, Q, statement, queries):
    result = ''
    for query in queries:
        l, r, target = query
        statement[l-1:r] = [target]
        evaluation = evaluate_statement(statement)
        if evaluation == target:
            result += 'Y'
        else:
            result += 'N'
    return result

# Read input
(N, Q) = map(int, input().split())
statement = input().split()
queries = []
for _ in range(Q):
    (l, r, target) = input().split()
    queries.append((int(l), int(r), target))

# Solve queries
result = solve_queries(N, Q, statement, queries)
print(result)