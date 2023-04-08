def prefix_to_infix(expression):
    stack = []
    
    for token in reversed(expression.split()):
        if token.isdigit():
            stack.append(token)
        else:
            o2 = stack.pop()
            o1 = stack.pop()
            stack.append('(' + o1 + ' ' + token + ' ' + o2 + ')')
    
    return stack.pop()
expression = '+ * 2 3 4'
infix_expression = prefix_to_infix(expression)
print(infix_expression)
