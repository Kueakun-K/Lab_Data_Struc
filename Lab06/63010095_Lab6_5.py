def staircase(n,k):
    if n == 0 and k == 1:
        print("Not Draw!")
        return
    else:
        if n > 0:
            display("_",n-1)
            display("#",k)
            print()
            return staircase(n-1,k+1)
        elif n < 0:
            display("_",k-1)
            display("#",-n)
            print()
            return staircase(n+1,k+1)

def display(a,b):
    if b > 0:
        print(a,end="")
        return display(a,b-1)

staircase(int(input("Enter Input : ")),1)