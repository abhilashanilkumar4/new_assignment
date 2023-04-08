def reverse(a):
    n = len(a)

    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    return a

a = [1, 2, 3, 4, 5]
reverse(a)
print(a)

