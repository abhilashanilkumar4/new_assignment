def character(s):

    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

s = 'hello world'
result = character(s)
if result is not None:
    print("The first non-repeated character is:", result)
else:
    print("There are no non-repeated characters in the string.")
