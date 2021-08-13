def odd_list(al):
    olist = []
    for i in range(0,len(al)):
        if al[i] % 2 == 1:
            olist.append(al[i])
    return olist


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
# print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)