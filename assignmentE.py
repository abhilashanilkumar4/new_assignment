def tower_of_hanoi(n, A,B, C):
    if n == 1:
        print("Move disk 1 from", A, "to", B)
        return
    
    tower_of_hanoi(n-1, A, C, B)
    print("Move disk", n, "from", A, "to", C)
    tower_of_hanoi(n-1, B, A, C)
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')

