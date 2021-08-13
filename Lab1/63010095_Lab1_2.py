x = input("Enter your High and Weight : ").split()
h = float(x[0])
w = float(x[1])
bmi = w / (h*h)
if bmi >= 30:
    print("Fat")
elif bmi >=25:
    print("Getting Fat")
elif bmi >=23:
    print("More than Normal Weight")
elif bmi >18.5:
    print("Normal Weight")
else:
    print("Less Weight")
