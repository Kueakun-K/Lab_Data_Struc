def move(n,A,C,B,maxn):
    if n == 1:
        print(f"move {n} from  {A[0]} to {C[0]}")
        C.append(A.pop())
        show(A,B,C,maxn)
    else:
        move(n-1,A,B,C,maxn)
        print(f"move {n} from  {A[0]} to {C[0]}")
        C.append(A.pop())
        show(A,B,C,maxn)
        move(n-1,B,C,A,maxn)

def show(A,B,C,i):
    if i < 1:
        return
    if A[0] == 'A':
        a = A
    elif B[0] == 'A':
        a = B
    elif C[0] == 'A':
        a = C
    if A[0] == 'B':
        b = A
    elif B[0] == 'B':
        b = B
    elif C[0] == 'B':
        b = C
    if A[0] == 'C':
        c = A
    elif B[0] == 'C':
        c = B
    elif C[0] == 'C':
        c = C

    if len(a)-1 < i:
        print("|  ",end="") 
    else:
        print(a[i],end="  ")

    if len(b)-1 < i:
        print("|  ",end="") 
    else:
        print(b[i],end="  ")

    if len(c)-1 < i:
        print("|") 
    else:
        print(c[i])
    show(A,B,C,i-1)

n = int(input("Enter Input : "))
A = ['A']
B = ['B']
C = ['C']

N = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

A.extend(N[n:0:-1])
show(A,B,C,n+1)
move(n,A,C,B,n+1)