A = int(input())
B = int(input())
C = int(input())
if A>B and A>C:
    print(A)
    if B>C:
        print(B)
        print(C)
    else:
        print(C)
        print(B)
else:
    if B>A and B>C:
        print(B)
        if A>C:
            print(A)
            print(C)
        else:
            print(C)
            print(A)
    else:
        print(C)
        if A>B:
            print(A)
            print(B)
        else:
            print(B)
            print(A)
