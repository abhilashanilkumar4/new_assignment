def postfix_to_prefix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(token + ' ' + operand1 + ' ' + operand2)
    
    return stack.pop()
expression = '2 3 + 4 *'
prefix_expression = postfix_to_prefix(expression)
print(prefix_expression)
