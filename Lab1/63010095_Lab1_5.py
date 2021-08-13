x = int(input("Enter Input : "))
y = (x+2)*2
x1 = x
y2 = y
for a in range(0,y):
    if a in range(0,1):
        for b in range(0,y):
            if b in range(0,x+1):
                print(".",end="")                    
            elif b in range(x+1,x+2):
                print("#",end="")             
            elif b in range(x+2,y):
                print("+",end="")           
        print()
    elif a in range(1,x+1):
        for c in range(0,y):
            if c in range(0,x1):
                print(".",end="")
            elif c in range(x1,x+2):
                print("#",end="")
            elif c == x+2 or c == y-1:
                print("+",end="")
            elif c in range(x+2,y-1):
                print("#",end="")
        x1 = x1-1   
        print()  
    elif a in range(x+1,x+3):
        for d in range(0,x+2):
            print("#",end="")
            d = d+1
        for d in range(x+2,y):
            print("+",end="")
            d = d+1
        print()
    elif a in range(x+3,y-1):
        for e in range(0,y):
            if e == 0 or e == x+1:
                print("#",end="")
            elif e in range(1,x+1):
                print("+",end="")
            elif e  in range(x+2,y2-1):
                print("+",end="")
            elif e in range(y2-1,y):
                print(".",end="")
        y2 = y2-1
        print()
    elif a in range(y-1,y):
        for f in range(0,y):
            if f in range(0,x+2):
                print("#",end="")                    
            elif f in range(x+2,x+3):
                print("+",end="")             
            elif f in range(x+3,y):
                print(".",end="")
