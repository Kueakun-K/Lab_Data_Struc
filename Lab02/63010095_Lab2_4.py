def hbd(age):
    x= int(age/2)
    if age%2==0:
        print(f"saimai is just 20, in base {x}!")
    else:
        print(f"saimai is just 21, in base {x}!")

year = input("Enter year : ")
hbd(int(year))