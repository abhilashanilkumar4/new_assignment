def check_brackets(code):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            elif opening_brackets.index(stack[-1]) == closing_brackets.index(char):
                stack.pop()
            else:
                return False
    
    return not stack
code = "def func():\n    if x == (3 * (4 + 5)):\n        print('Hello, world!')"
brackets_closed = check_brackets(code)
print(brackets_closed)
