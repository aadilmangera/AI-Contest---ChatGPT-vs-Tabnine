def evaluate_expression(x, operator, y):
    if operator == 'and':
        return x and y
    elif operator == 'or':
        return x or y

def evaluate_statement(statement, l, r, target):
    stack = []
    for i in range(len(statement)):
        if i % 2 == 0:
            if i < l or i > r:
                stack.append(statement[i] == 'true')
        else:
            if len(stack) >= 2:
                y = stack.pop()
                operator = statement[i]
                x = stack.pop()
                stack.append(evaluate_expression(x, operator, y))
    while len(stack) > 1:
        y = stack.pop()
        operator = stack.pop()
        x = stack.pop()
        stack.append(evaluate_expression(x, operator, y))
    return stack[0] == target

(N, Q) = map(int, input().split())
statement = input().split()

for _ in range(Q):
    (l, r, target) = input().split()
    l = int(l) - 1
    r = int(r) - 1
    target = target == 'true'
    if evaluate_statement(statement, l, r, target):
        print('Y', end='')
    else:
        print('N', end='')