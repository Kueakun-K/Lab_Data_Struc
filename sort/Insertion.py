def insertion(l):
    for i in range(1, len(l)): #from index 1 to last index
        iEle = l[i]    #insert element
        for j in range(i, -1, -1):
            if iEle<l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break 


input = [int(i) for i in input("Enter Input : ").split()]
insertion(input)
print(input)