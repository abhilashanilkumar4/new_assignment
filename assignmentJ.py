def find_smallest_number(stack):
    min_num = float('inf')
    
    for num in stack:
        if num < min_num:
            min_num = num
    
    return min_num
stack = [5, 3, 8, 2, 10]
smallest_num = find_smallest_number(stack)
print(smallest_num)
