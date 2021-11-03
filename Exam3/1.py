def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)
    
def show(i):
    if i == 2:
        print("+ 1/2",end=" ")
        return
    else:
        show(i-1)
        i = str(i)
        print("+ 1/"+i,end=" ")
        return
    
print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print("1",end=" ")
if num > 1:
    show(num)
print("=",end=" ")
print("%.8f" %(harmonic_sum(num)))