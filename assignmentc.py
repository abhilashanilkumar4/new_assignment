def rotate(A,B ):
    if len(A) != len(B):
        return False
    AB = A + B
    if B in AB:
        return True
    else:
        return False

A = 'hello'
B = 'llohe'
if rotate(A,B):
    print("The strings are rotating.")
else:
    print("The strings are not rotating.")
