def matrix_A(U, X):
    print("  ", end="")
    for i in range(1, len(U)+1):
        print(i, end=" ")
    print()
    for i in X:
        print(i, end=" ")
        for j in U:
            if i in j:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
