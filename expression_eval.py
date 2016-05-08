
def evaluate(expression):
    """Evaluates a string the represents an arithmetic expression.

    Args:
      expression: str, the expression to evaluate.

    Returns:
      float, the result of the evaulation.
      None, when there is an error in expression evaluation.
    """
    # dict mapping operators to a priority number.
    # The lower in value the lower the priority.
    op_priorities = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1
    }
    # The stack that holds the expression to be executed
    main_stack = []
    # Temp variable holding the priority of the current operator
    current_priority = None

    # The result to return
    result = 0

    for c in expression:
        if c in op_priorities:
            if current_priority is None:
                current_priority = op_priorities[c]
                main_stack.append(c)
            elif op_priorities[c] < current_priority:
                # Start evaulating whats on the stack
                try:
                    local_result = calculate_as_stack(main_stack)
                except ValueError as error:
                    return None
                main_stack.append(str(local_result))
                main_stack.append(c)
                current_priority = op_priorities[c]
            else:
                current_priority = op_priorities[c]
                main_stack.append(c)
        elif main_stack and main_stack[-1] not in op_priorities:
            temp_c = main_stack.pop()
            temp_c += c
            main_stack.append(temp_c)
        else:
            main_stack.append(c)

    try:
        result = calculate_as_stack(main_stack)
    except ValueError as error:
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
    operators = ("+", "-", "*", "/")
    result = None
    operator = None

    while stack:
        term = stack.pop()
        if term in operators:
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
