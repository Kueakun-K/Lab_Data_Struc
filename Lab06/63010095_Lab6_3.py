def binary(n,m):
    if n < 0:
        return 0
    else:
        binary(n-1,m)
        x = str(bin(n).replace("0b",""))
        if len(x) < m:
            fill(x,m)
        else:
            print(x)
    
def fill(x,m):
    if len(x) < m:
        x = "0" + x
        fill(x,m)
    else:
        print(x)
    
input = int(input("Enter Number : "))
if input >= 0:
    binary(pow(2,input)-1,input)
else:
    print("Only Positive & Zero Number ! ! !")

