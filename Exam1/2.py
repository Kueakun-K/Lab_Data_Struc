print(" *** Divisible number ***")
x = int(input("Enter a positive number : "))
y = []

if x <= 0:
    print(f"{x} is OUT of range !!!")
else:
    for i in range(1,x+1):
        if x % i == 0:
            y.append(i)
        
    print("Output ==>",end="")
    for j in y:
        print(f" {j}",end="")
    print()
    
    print(f"Total ==> {len(y)}")