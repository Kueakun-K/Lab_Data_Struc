def checksort(input,index):
    if index == 0:
        return "Yes"
    else:
        if input[index] >= input[index-1]:
            return checksort(input,index-1)
        else:
            return "No"

input = [int(i) for i in input("Enter Input : ").split()]
print(checksort(input,len(input)-1))