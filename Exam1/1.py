print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))

if x >= 209:
    print("Wind classification is Super Typhoon.")
elif x >= 102:
    print("Wind classification is Typhoon.")
elif x >= 56:
    print("Wind classification is Tropical Storm.")
elif x >= 52:
    print("Wind classification is Depression.")
elif x >= 0:
    print("Wind classification is Breeze.")
else:
    print("!!!Wrong value can't classify.")