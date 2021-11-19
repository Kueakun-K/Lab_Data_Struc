
input = input("Enter Input : ").replace(","," ").split()
Stack = []
x = 0
while x < len(input):
    if input[x] == "A":
        Stack.append(int(input[x+1]))
        x += 2
    elif input[x] == "B":
        if Stack != []:
            y = 1
            o1 = 1
            o2 = 2
            while o2 <= len(Stack):
                if Stack[-o1] >= Stack[-o2]:
                    o2 += 1
                else:
                    y += 1
                    o1 = o2
                    o2 += 1
            print(y)

        else:
            print("0")
        x += 1
    elif input[x] == "S":
        for i in range(0,len(Stack)):
            if Stack[i] % 2 == 0:
                Stack[i] -= 1
            else:
                Stack[i] += 2
        x += 1

