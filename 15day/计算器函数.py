def aa(x,y,f):
	if f == "+":
		return x+y 
	elif f == "-":
		return x-y
	elif f == "*":
		return x*y
	elif f == "/":
		if y != 0:
			return x/y
		else:
			print("输入有误")
	elif f == "**":
		return x**y
	else:
		print("输入有误")
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请再输入一个数字"))
	f = input("请输入+,-,*,/,**,")
	aa = aa(x,y,f)
	print(aa)
