def bsort(l):
    if len(l) <= 1:
        return l
    if  len(l) == 2:
        return l if l[0] > l[1] else [l[1], l[0]]
    a,b = l[0],l[1]
    bs = l[2:]
    sortm = []
    if a > b:
        sortm = [a] + bsort([b]+bs)
    else:
        sortm = [b] + bsort([a]+bs)
    return bsort(sortm[:-1]) + sortm[-1:]

input = input("Enter your List : ").split(",")
input = list(map(int, input))
print(f"List after Sorted : {bsort(input)}")

