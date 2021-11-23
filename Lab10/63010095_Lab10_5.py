def MinWeigth(inp,box,weigth):
    index = 0
    for i in range(box):
        weigthinbox = 0
        while True:
            if index == len(inp):
                return True
            if weigth >= inp[index] + weigthinbox:
                weigthinbox += inp[index]
                index += 1
            else:
                break
    return False 

input = input("Enter Input : ").split("/")
inp = [int(i) for i in input[0].split()]
box = int(input[1])
weigth = 0
for j in inp:
    if j > weigth:
        weigth = j

while MinWeigth(inp,box,weigth) is False:
    weigth += 1

print(f"Minimum weigth for {box} box(es) = {weigth}")
