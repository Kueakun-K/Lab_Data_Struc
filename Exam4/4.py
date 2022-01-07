def shell(l, dIncrements):
	global compare, compare1
	for inc in dIncrements:
		for i in range(inc,len(l)): 
			iEle = l[i]
			for j in range(i, -1, -inc):
				if iEle<l[j-inc] and j >= inc:
					l[j] = l[j-inc]
					compare += 1
				else:
					l[j] = iEle
					compare1 += 1
					break

print(" *** Shell sort ***")
input = [int(i) for i in input("Enter some numbers : ").split()]
dIncrements = [3,1]
compare = 0
compare1 = 0
shell(input,dIncrements)
print()
print(input)
# print(f"Data comparison =  {compare}")
print(compare, compare1)