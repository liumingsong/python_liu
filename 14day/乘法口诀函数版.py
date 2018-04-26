def a():
	x = int(input("请输入数字"))
	y = int(input("请输入数字"))
	for i in range(x,y):
		for h in range(1,i+1):
			print("%d*%d=%d\t"%(x,y,x*y),end = "")
		print("")
while True:
	a()
