def gcd(n,i):
    if n[0] == 0 and n[1] == 0:
        return "Error! must be not all zero."
    elif n[0] == 0 or n[1] == 0:
        return n[0] if n[0] > n[1] else n[1]
    else:
        if i <= n[0] and i <= n[1] and i < 900:
            if n[0] %  i == 0 and n[1] % i == 0:
                n[2] = i
            return gcd(n,i+1)
        else:
            return n[2] 

num = input("Enter Input : ").split()
num[0] = int(num[0])
num[1] = int(num[1])
if num[0] != 0 or num[1] != 0:
    if num[0] < 0 and num[1] < 0:
        if num[0]>=num[1]:
            print(f"The gcd of {num[1]} and {num[0]} is : ",end="")
        else:
            print(f"The gcd of {num[0]} and {num[1]} is : ",end="")
    else:
        if num[0]>=num[1]:
            print(f"The gcd of {num[0]} and {num[1]} is : ",end="")
        else:
            print(f"The gcd of {num[1]} and {num[0]} is : ",end="")
num.append(0)
index = 1
if num[0] < 0:
    num[0] = num[0] * (-1)
if num[1] < 0:
    num[1] = num[1] * (-1)
print(gcd(num,index))