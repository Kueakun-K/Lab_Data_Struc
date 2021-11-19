def odd_even(arr, s):
    i=0
    x=[]
    while i < len(s):
        if arr == "Odd":
            if i%2==0:
                if type(s) == list:
                    x.append(s[i])
                else:
                    print(s[i],end="")
        elif arr == "Even":
            if i%2==1:
                if type(s) == list:
                    x.append(s[i])
                else:
                    print(s[i],end="")
        i+=1
    if type(s)==list:
        print(x)
print("*** Odd Even ***")
input = input("Enter Input : ").split(",")
if input[0] == "S":
    odd_even(input[2],input[1])
elif input[0]=="L":
    x = input[1].split(" ")
    odd_even(input[2],x)
 