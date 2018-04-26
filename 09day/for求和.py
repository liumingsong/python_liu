d = 0
while d <= 0:
	a = int(input("请输入数字:"))
	b = int(input("请输入数字:"))
	sum = 0
	if a < b:
		for i in range(a,b+1):
			print(i)
			sum = sum+i
			print(sum)
		d+=1
	else:
		print("输入有误")
