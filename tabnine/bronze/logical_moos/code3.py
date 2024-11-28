def evaluate_statement(statement):
    operator_stack = []
    operand_stack = []
    for keyword in statement:
        if keyword == 'true' or keyword == 'false':
            operand_stack.append(keyword)
        elif keyword == 'and' or keyword == 'or':
            operator_stack.append(keyword)
        elif keyword == ')':
            while operator_stack[-1] != '(':
                y = operand_stack.pop()
                x = operand_stack.pop()
                operator = operator_stack.pop()
                if operator == 'and':
                    if x == 'true' and y == 'true':
                        operand_stack.append('true')
                    else:
                        operand_stack.append('false')
                elif operator == 'or':
                    if x == 'true' or y == 'true':
                        operand_stack.append('true')
                    else:
                        operand_stack.append('false')
            operator_stack.pop()  # Remove the opening parenthesis
    while operator_stack:
        y = operand_stack.pop()
        x = operand_stack.pop()
        operator = operator_stack.pop()
        if operator == 'and':
            if x == 'true' and y == 'true':
                operand_stack.append('true')
            else:
                operand_stack.append('false')
        elif operator == 'or':
            if x == 'true' or y == 'true':
                operand_stack.append('true')
            else:
                operand_stack.append('false')
    return operand_stack[0]

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