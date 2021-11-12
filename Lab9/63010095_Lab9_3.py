def checkDROME(inp,i):
    if Repdrome(inp,i):
        return "Repdrome"
    elif Metadrome(inp,i):
        return "Metadrome"
    elif Plaindrome(inp,i):
        return "Plaindrome"
    elif Katadrome(inp,i):
        return "Katadrome"
    elif Nialpdrome(inp,i):
        return "Nialpdrome"
    else:
        return "Nondrome"

def Metadrome(inp,i):
    if i == 0:
        return True
    else:
        if inp[i] >= inp[i-1] and inp[i] != inp[i-1]:
            return Metadrome(inp,i-1)
        else:
            return False
        
def Plaindrome(inp,i):
    if i == 0:
        return True
    else:
        if inp[i] >= inp[i-1]:
            return Plaindrome(inp,i-1)
        else:
            return False

def Katadrome(inp,i):
    if i == 0:
        return True
    else:
        if inp[i] <= inp[i-1] and inp[i] != inp[i-1]:
            return Katadrome(inp,i-1)
        else:
            return False

def Nialpdrome(inp,i):
    if i == 0:
        return True
    else:
        if inp[i] <= inp[i-1]:
            return Nialpdrome(inp,i-1)
        else:
            return False

def Repdrome(inp,i):
    if i == 0:
        return True
    else:
        if inp[i] == inp[i-1]:
            return Repdrome(inp,i-1)
        else:
            return False

input = input("Enter Input : ")
inp = [int(i) for i in input]
print(checkDROME(inp,len(inp)-1))