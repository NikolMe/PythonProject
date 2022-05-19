from operator import contains


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


def matrix_B(U, X):
    


print("Enter:")
U = input().split(" ")
X = []
for i in U:
    if i[1] not in X:
        X.append(i[1])
    if i[3] not in X:
        X.append(i[3])
X = sorted(X)
print(X)
matrix_A(U, X)
