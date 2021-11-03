def Max(list,index,max):
    if index <len(list):
        if int(list[index])>max:
            max=int(list[index])
        index+=1
        return Max(list,index,max)
    else:
        return max


num = input("Enter Input : ").split()
print("Max :",Max(num,0,-9999999))