def selection(l):
	for last in range(len(l)-1, -1, -1):# จาก last ind ถึง  ind 0
		biggest = l[0]  # ค่าใหญ่สุด
		biggest_i = 0   # ตำแหน่ง ของค่าใหญ่สุด
		for i in range(1, last+1): # จากตำแหน่ง 1 ถึง last หาค่าใหญ่สุด
			if l[i] > biggest:       # if ที่ i ใหญ่กว่าค่าเดิม
				 biggest = l[i]	        # เปลี่ยน ค่าใหญ่ที่สุด เป็น ค่าใหม่ที่ i
				 biggest_i = i             # เก็บ index ค่าใหญ่อันใหม่ 
		#swap elements biggest and last element
		l[last], l[biggest_i ] = l[biggest_i], l[last]

input = [int(i) for i in input("Enter Input : ").split()]
selection(input)
print(input)