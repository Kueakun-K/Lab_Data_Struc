class MyInt:
    def __init__(self,i):
        self.i = i
        self.j = i
        self.ro = []
    
    def toRoman(self):
        while self.j != 0:
            if self.j >= 1000:
                self.j = self.j - 1000
                self.ro.append("M")
            elif self.j >= 900:
                self.j = self.j - 900
                self.ro.append("CM")
            elif self.j >= 500:
                self.j = self.j - 500
                self.ro.append("D")
            elif self.j >= 400:
                self.j = self.j - 400
                self.ro.append("CD")
            elif self.j >= 100:
                self.j = self.j - 100
                self.ro.append("C")
            elif self.j >= 90:
                self.j = self.j - 90
                self.ro.append("XC")
            elif self.j >= 50:
                self.j = self.j - 50
                self.ro.append("L")
            elif self.j >= 40:
                self.j = self.j - 40
                self.ro.append("XL")
            elif self.j >= 10:
                self.j = self.j - 10
                self.ro.append("X")
            elif self.j >= 9:
                self.j = self.j - 9
                self.ro.append("IX")
            elif self.j >= 5:
                self.j = self.j - 5
                self.ro.append("V")
            elif self.j >= 4:
                self.j = self.j - 4
                self.ro.append("IV")
            elif self.j >= 1:
                self.j = self.j - 1
                self.ro.append("I")
        return self.ro

    def __add__(self,x):
        return int((self.i + x.i)/2) + (self.i + x.i) 


print(" *** class MyInt ***")
x,y = input("Enter 2 number : ").split()
a = MyInt(int(x))
b = MyInt(int(y))

print(f"{x} convert to Roman : ",end="")
for i in a.toRoman():
    print(i,end="")
print()

print(f"{y} convert to Roman : ",end="")
for j in b.toRoman():
    print(j,end="")
print()

print(f"{x} + {y} = ",end="")
print(a+b)