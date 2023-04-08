def reverse_stack(stack):
    aux_stack = []
    
    while stack:
        aux_stack.append(stack.pop())
    
    while aux_stack:
        stack.append(aux_stack.pop())
    
    return stack

stack = [1, 2, 3, 4, 5]
print(stack)
reversed_stack = reverse_stack(stack)
print(reversed_stack)
