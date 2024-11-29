# Chatgpt Bronze Problems
# Problem 1

# Prompt 1

def evaluate_expression(expression):
    """Evaluate a boolean expression considering operator precedence."""
    stack = []
    operators = []

    def apply_operator():
        """Apply the operator on top of the operator stack to the top two elements of the value stack."""
        if len(stack) < 2 or not operators:
            return
        b = stack.pop()
        a = stack.pop()
        op = operators.pop()
        if op == "and":
            stack.append(a and b)
        elif op == "or":
            stack.append(a or b)

    for token in expression:
        if token in {"true", "false"}:
            stack.append(token == "true")
        elif token in {"and", "or"}:
            while (operators and operators[-1] == "and" and token == "or"):
                apply_operator()
            operators.append(token)

    while operators:
        apply_operator()

    return stack[0]

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, q = map(int, data[0].split())
    tokens = data[1].split()

    queries = []
    for i in range(q):
        l, r, desired = data[2 + i].split()
        l, r = int(l) - 1, int(r) - 1  # Convert to 0-based indexing
        queries.append((l, r, desired == "true"))

    results = []
    for l, r, desired in queries:
        # Create a copy of the expression with the range [l, r] replaced by the desired value
        new_expression = tokens[:l] + ["true" if desired else "false"] + tokens[r + 1:]
        # Evaluate the new expression
        if evaluate_expression(new_expression) == desired:
            results.append("Y")
        else:
            results.append("N")

    print("".join(results))
solve()


# Prompt 1 a

def solve():
    # Simulated input for testing
    data = [
        "13 4",
        "false or true and false and false and true or true and false",
        "1 5 false",
        "3 11 true",
        "3 11 false",
        "13 13 true"
    ]

    n, q = map(int, data[0].split())
    tokens = data[1].split()

    queries = []
    for i in range(q):
        l, r, desired = data[2 + i].split()
        l, r = int(l) - 1, int(r) - 1  # Convert to 0-based indexing
        queries.append((l, r, desired == "true"))

    def evaluate_expression(expression):
        """Evaluate a boolean expression considering operator precedence."""
        stack = []
        operators = []

        def apply_operator():
            """Apply the operator on top of the operator stack to the top two elements of the value stack."""
            if len(stack) < 2 or not operators:
                return
            b = stack.pop()
            a = stack.pop()
            op = operators.pop()
            if op == "and":
                stack.append(a and b)
            elif op == "or":
                stack.append(a or b)

        for token in expression:
            if token in {"true", "false"}:
                stack.append(token == "true")
            elif token in {"and", "or"}:
                while (operators and operators[-1] == "and" and token == "or"):
                    apply_operator()
                operators.append(token)

        while operators:
            apply_operator()

        return stack[0]

    results = []
    for l, r, desired in queries:
        # Create a copy of the expression with the range [l, r] replaced by the desired value
        new_expression = tokens[:l] + ["true" if desired else "false"] + tokens[r + 1:]
        # Evaluate the new expression
        if evaluate_expression(new_expression) == desired:
            results.append("Y")
        else:
            results.append("N")

    print("".join(results))

solve()


# Test more cases

def solve():
    # Simulated input for testing
    data = [
        "5 7",
        "false and true or true",
        "1 1 false",
        "1 3 true",
        "1 5 false",
        "3 3 true",
        "3 3 false",
        "5 5 false",
        "5 5 true"
    ]

    n, q = map(int, data[0].split())
    tokens = data[1].split()

    queries = []
    for i in range(q):
        l, r, desired = data[2 + i].split()
        l, r = int(l) - 1, int(r) - 1  # Convert to 0-based indexing
        queries.append((l, r, desired == "true"))

    def evaluate_expression(expression):
        """Evaluate a boolean expression considering operator precedence."""
        stack = []
        operators = []

        def apply_operator():
            """Apply the operator on top of the operator stack to the top two elements of the value stack."""
            if len(stack) < 2 or not operators:
                return
            b = stack.pop()
            a = stack.pop()
            op = operators.pop()
            if op == "and":
                stack.append(a and b)
            elif op == "or":
                stack.append(a or b)

        for token in expression:
            if token in {"true", "false"}:
                stack.append(token == "true")
            elif token in {"and", "or"}:
                while (operators and operators[-1] == "and" and token == "or"):
                    apply_operator()
                operators.append(token)

        while operators:
            apply_operator()

        return stack[0]

    results = []
    for l, r, desired in queries:
        # Create a copy of the expression with the range [l, r] replaced by the desired value
        new_expression = tokens[:l] + ["true" if desired else "false"] + tokens[r + 1:]
        # Evaluate the new expression
        if evaluate_expression(new_expression) == desired:
            results.append("Y")
        else:
            results.append("N")

    print("".join(results))

solve()






























