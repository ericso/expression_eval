# Set of allowed operators.
OPERATORS = ("+", "-", "*", "/")

# dict mapping operators to a priority number.
# The lower in value the lower the priority.
OP_PRIORITIES = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1
}


def evaluate(expression):
    """Evaluates a string the represents an arithmetic expression.

    Args:
      expression: str, the expression to evaluate.

    Returns:
      float, the result of the evaulation.
      None, when there is an error in expression evaluation.
    """
    # The stack that holds the expression to be executed
    main_stack = []
    # Temp variable holding the priority of the current operator
    current_priority = None

    # The result to return
    result = 0

    # Iterate over expression to evalute.
    for c in expression:
        if c in OP_PRIORITIES:
            if main_stack and main_stack[-1] in OPERATORS:
                # We have two operators in a row. Error.
                return None
            if current_priority is None:
                # We have not encountered an operator yet.
                current_priority = OP_PRIORITIES[c]
                main_stack.append(c)
            elif OP_PRIORITIES[c] < current_priority:
                # See an operator with priority less then the last one seen.
                # Start evaulating whats on the stack.
                try:
                    local_result = calculate_as_stack(main_stack)
                except ValueError as error:
                    print(error)
                    return None
                main_stack.append(str(local_result))
                main_stack.append(c)
                current_priority = OP_PRIORITIES[c]
            else:
                current_priority = OP_PRIORITIES[c]
                main_stack.append(c)
        elif main_stack and main_stack[-1] not in OP_PRIORITIES:
            # Handle multi-digit numbers.
            temp_c = main_stack.pop()
            temp_c += c
            main_stack.append(temp_c)
        else:
            main_stack.append(c)

    try:
        result = calculate_as_stack(main_stack)
    except ValueError as error:
        print(error)
        return None
    return result

def calculate_as_stack(stack):
    """Calculate result of stack.

    Args:
      stack: list, terms of an arithmetic expression.

    Returns:
      float, the result of the expression represented by the stack.

    Raises:
      ValueError, if the operator is not recognized.
    """
    result = None
    operator = None

    # print(stack)
    while stack:
        # We keep evaluating the stack while there are still elements in it.
        term = stack.pop()
        if term in OPERATORS:
            operator = term
        else:
            term = float(term)
            if result is None:
                result = term
            else:
                # We are evaluating the terms backwards (popping off of stack).
                # Because of this, we need to reverse the order of the operands.
                # Instead of
                #     result = result + term
                #  we do
                #     result = term + result
                if operator == "+":
                    result = term + result
                elif operator == "-":
                    result = term - result
                elif operator == "*":
                    result = term * result
                elif operator == "/":
                    result = term / result
    return result
