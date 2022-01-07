def insertion(l):
    global comp
    for i in range(1, len(l)):
        iEle = l[i]
        tmp1  = 0
        for j in range(i, -1, -1):
            if iEle<l[j-1] and j > 0:
                l[j] = l[j-1]
                tmp1 += 1
            else:
                l[j] = iEle
                if tmp1 == 0:
                    comp += 1
                else:
                    comp += tmp1
                break

print(" *** Insertion sort ***")
input = [int(i) for i in input("Enter some numbers : ").split()]
comp = 0
insertion(input)
print()
print(input)
print(f"Data comparison =  {comp}")

